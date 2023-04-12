'''
数据库设置
----------------
存储数据库账号密码地址端口库名等信息，并进行数据库引擎创建
'''

import urllib.parse

from sqlalchemy import create_engine

USER0 = 'pass'
PASSWD0 = urllib.parse.quote_plus("pass")

HOST0 = '0.0.0.0'
HOST1 = '1.1.1.1'

PORT0 = '1234'
PORT1 = '4321'

DATABASE0 = 'pass'
DATABASE1 = 'pass'

host0_database0 = create_engine(f'mysql://{USER0}:{PASSWD0}@{HOST0}:{PORT0}/{DATABASE0}')
host0_database1 = create_engine(f'mysql://{USER0}:{PASSWD0}@{HOST0}:{PORT0}/{DATABASE1}')
host1_database0 = create_engine(f'mysql://{USER0}:{PASSWD0}@{HOST1}:{PORT1}/{DATABASE0}')
host1_database1 = create_engine(f'mysql://{USER0}:{PASSWD0}@{HOST1}:{PORT1}/{DATABASE1}')
