'''
'''
import numpy as np
import pandas as pd

import utils.p_to_sql
from settings.database import host0_database0

# 模拟数据
data = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
data = data.reset_index()
data = data.rename(columns={'index': 'id'})

# 上传数据
data.p_to_sql('test', host0_database0, index=['id'], partitions=10, n_workers=1, threads_per_worker=1)
