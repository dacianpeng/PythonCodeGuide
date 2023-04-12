'''
本脚本提供了一个多线程写入MySQL数据库的方法
在需要使用多线程写入MySQL数据库的时候，需要先导入本脚本，再调用pd.DataFrame.p_to_sql方法
'''
import MySQLdb
import numpy as np
import pandas as pd
from dask import delayed


def p_to_sql(dataframe, table_name: str, con : str, index : list=False, partitions : int=1, n_workers : int=1, threads_per_worker : int=1, **to_sql_kargs) -> None:
    '''
    多线程写入MySQL数据库
    ---------
    :param dataframe: pd.DataFrame, 需要写入数据库的数据，必须为 `reset_index()` 后的数据
    :param table_name: str, 写入数据库的表名
    :param con: str, 数据库引擎，见 `setting.database.py`
    :param index: list, 需要建立索引的列
    :param partitions: int, 将写入的dataframe分成几个部分
    :param n_workers: int, 调度核心数
    :param threads_per_worker: int, 每个核心线程数
    :param to_sql_kargs: dict, 其他将被传递给原生 `pd.DataFrame.to_sql` 的字典参数
    :return: None
    '''
    dataframe.iloc[0: 0].to_sql(table_name, con, if_exists='append', index=False) # 在数据库中预创建表
    dataframe = dataframe.fillna('NULL') # 将空值填充为字符串'NULL'
    all_parts = np.array_split(dataframe, partitions) # 将dataframe等分成几个部分
    
    def partly_insert(part_sequence):
        '''
        对一个part写入数据库的操作
        ---------
        :param part_sequence: int, 需要写入数据库的部分序号
        :return: int, 0
        '''
        part= all_parts[part_sequence]
        engine = MySQLdb.connect(host=con.url.host, user=con.url.username, password=con.url.password, database=con.url.database, port=con.url.port, charset='utf8')
        cursor = engine.cursor()
        insert_sql = f"insert into\
    {table_name}(`{'`, `'.join(part.columns.values)}`)\
    values\
        {str(list(part.itertuples(index=False, name=None))).strip('[').strip(']')}"

        cursor.execute(insert_sql)
        engine.commit()
        engine.close()
        return 0

    results = []
    # 将写入数据库的任务使用dask进行调度
    for part_sequence in np.arange(partitions):
        results.append(delayed(partly_insert)(part_sequence))

    if type(dataframe) != pd.Series:
        # 如果dataframe为pd.DataFrame，则使用dask进行调度
        delayed(sum)(results).compute(n_workers=n_workers, threads_per_worker=threads_per_worker)
    else:
        # 如果dataframe为pd.Series，则直接写入数据库，不进行多线程调度
        series = dataframe
        series.to_sql(table_name, con, **to_sql_kargs)

    if index:
        # 如果需要建立索引，则建立索引
        engine = MySQLdb.connect(host=con.url.host, user=con.url.username, password=con.url.password, database=con.url.database, port=con.url.port, charset='utf8')
        cursor = engine.cursor()
        cursor.execute(f'ALTER TABLE `{table_name}` ADD INDEX ({", ".join(index)})')
        engine.close()

# 将p_to_sql方法添加到pd.DataFrame类中
pd.DataFrame.p_to_sql = p_to_sql
