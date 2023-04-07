# Python 编码指南

遵从编码指南以实现以下目的：

✅ 为代码创建一致的外观，确保合作者审阅代码（Code Review）时专注于内容而非布局

✅ 使大语言模型（LLM, Large Language Model）可以基于既有内容理解与辅助编写代码

✅ 提高代码复用性，便于复制、更改和维护代码

✅ 展现 Python 最佳写法（Code Pride）

## 目录

- [Python 编码指南](#python-编码指南)
  - [目录](#目录)
  - [前言](#前言)
  - [注释约定](#注释约定)
    - [缩进](#缩进)
    - [语言](#语言)
    - [注释符号管理](#注释符号管理)
    - [行管理](#行管理)
    - [包（模块）管理](#包模块管理)
    - [Docstring](#docstring)
    - [特殊标志](#特殊标志)
    - [代码即注释](#代码即注释)
  - [注释规范](#注释规范)
    - [Docstring (函数)](#docstring-函数)
    - [Docstring (脚本)](#docstring-脚本)
    - [Doctest (SKIP)](#doctest-skip)
    - [TypeHint](#typehint)
  - [代码约定](#代码约定)
    - [代码符号管理](#代码符号管理)
    - [学科规范](#学科规范)
    - [函数约定](#函数约定)
    - [命名约定](#命名约定)
    - [异常处理](#异常处理)
  - [附录](#附录)

## 前言

- 项目优于具体语言

> 项目涉及到多语言编程时，其他语言代码指南可能与本指南冲突。如果有确定的项目指南，当冲突时，项目编码指南优先级更高

- 编码 = 代码 + 注释

> 本指南中，编码两个字的含义更偏向编程（Programming），包含代码（Code）与注释（Comment）

- 约定 ≠ 规范

> 约定（Convention）为一致的外观服务，实际编写时有较高灵活度

> 规范（Standard）为实际功能服务，按照规范编写有助于集成开发环境理解编码

- 约定、规范不导致程序失败

> 程序正常运行与是否遵守此指南中内容无关（除缩进部分外）

- 灵活

> 指南总有考虑不周的情况

> 按照指南编码时，如感到繁琐、困扰或发现遗漏，可以制定新的格式并提交工单（Issue）或发起和并请求（Pull Request）

- 更新

> 我们希望编码指南可以保持先进性（State-of-Art），采取轮动发布 (Release) 制度

> （暂定）每隔固定时间或出现重大技术进步时发布。预计完成初版修订后，2023-4发布第一版


## 注释约定

本部分主要模仿与推测了 `numpy` 包的注释写法

### 缩进

统一缩进，缩进距离建议采用制表符（或4个空格）

一行拆两行时，例

```Python
# 参数起始点平行（垂直对齐写法） ✔️
foo = long_long_long_function_name(var_one, var_two,
                         var_three, var_four)

# 括号后换行，且参数起始点平行（悬挂缩进） ✔️
def long_long_long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 如果后边有代码行，悬挂缩进增加一级 ✔️
def long_long_long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 缩进并非制表符（或4个空格）也可以接受，但不建议这么做 ✔️
foo = long_long_long_function_name(
  var_one, var_two,
  var_three, var_four)

# 参数放在第一行而没有垂直对齐 ❌
foo = long_long_long_function_name(var_one, var_two,
    var_three, var_four)

# 后边有代码行时没有增加缩进 ❌
def long_long_long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

涉及到 `if` 从句时，`if` 和单个空格以及左括号正好是 4 个空格缩进，这可能与嵌套在 `if` 语句中的代码块产生冲突

```Python
# 我们建议对条件行的续行增加缩进 ✔️
if (long_long_long_long_long_condition_1
        and long_long_long_long_long_condition_2):
    do_something()
```

多行结构的右括号（包括圆括号，中括号和花括号）可以置于最后一行代码的第一个非空白字符下面，也可以放在第一个字符的位置

```Python
# 以下示例均正确
some_matrix = [
    1, 2, 3,
    4, 5, 6,
    ]
some_matrix = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_have_long_name_or_takes_matrix_like_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
result = some_function_that_have_long_name_or_takes_matrix_like_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### 语言

统一注释语言，使用中文注释，必要时辅以英文

> 我们有 120% 把握确定，基于目前发展阶段，使用中文注释有利于提高全流程协作效率

> 代码是基于英文编写的，高可读性的代码和注释并无差别，我们仍希望协作者拥有良好英文读写能力

对于英文缩写、专有名词，附英文缩写全称，例

```Python
# DEF (违约因子, default) ✔️
# DEF, 违约因子, default ✔️
# DEF (DEFault) ✔️
# DEF (default) ✔️
# DEF, DEFault ✔️
# DEF, default ✔️
# DEF (违约因子) ❌
# DEF, 违约因子 ❌
# TERM (期限因子, term) ✔️
# PP (预付款因子, pre-payment) ✔️
regressors = [
    ['α'],
    ['α', 'DEF', 'TERM'],
    ['α', 'DEF', 'TERM', 'PP']
    ]
```

英文注释时，以大写字母开始注释正文

标点符号的语言没有要求，灵活度较高，原则上要求与前后文语境语言一致

> 注意：如果使用英文标点符，需遵守英文标点语法，非行尾处标点符号与中文正文间空一格

> 参考以下范例中标点符号的运用

```Python
# 这是一份 "Hello World" 的注释范例
# 它（即 Hello World）是每位编程者入门时，或早或晚、或多或少都会接触到的内容，不是吗?
# This is a comment with "Hello World"
# Every programmer knows it (Hello World), isn't it?
```

使用英文时，请正确拼写单词（参见附录 `spell check` 链接）

### 注释符号管理

结束注释文本不需标点符号

避免多余的空格

> 括号内部紧挨括号的地方，包括圆括号、方括号和花括号，例

```Python
open(f'{python_path}\\zipped_chrome_driver.zip', 'wb').write(package.content)
# 二进制格式写入 (wb, write binary) ✔️
# 二进制格式写入 ( wb, write binary ) ❌
```

逗号后面右括号

```Python
# PEP8 建议
foo = (0,)

# 我们建议
foo = (0, )
```

逗号，分号，和冒号之后加空格

```Python
if x == 4: print x, y; x, y = y, x ✔️
if x == 4 : print x , y ; x , y = y , x ❌
```

冒号作为二元运算符，两边应该具有相同数目的空格（可将其视作最低优先级的运算符）。在扩展切片操作中，两个冒号左右两边的空格数都应该相等。当然，如果切片操作省略了参数，那么空白也应该省略

```Python
# 建议 ✔️
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```

```Python
# 不建议 ❌
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

左括号前面无空格

```Python
# 建议 ✔️
dct['key'] = lst[index] # 字典取值
spam(1) # 函数

# 不建议 ❌
dct ['key'] = lst[index] # 字典取值
spam (1) # 函数
```

对齐并不重要

```Python
# 建议 ✔️
x = 1
y = 2
long_variable = 3

# 不建议 ❌
x             = 1
y             = 2
long_variable = 3
```

混用不同优先级的运算符时，在低优先级运算符两边增加空格。但不要超过一个，并且保持二元运算符两边的空格数量相同

```Python
# 建议 ✔️
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# 不建议 ❌
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

表示关键字参数或者默认参数时，等号两边不加空格

```Python
# 建议 ✔️
def complex(real, imag=0.0):
  return magic(r=real, i=imag)

# 不建议 ❌
def complex(real, imag = 0.0):
  return magic(r = real, i = imag)
```

当函数定义使用参数注解（见下文 `TypeHint`）和参数默认值时，赋值号两边要加空格

```Python
# 建议 ✔️
def complex(real, imag: np.array = 0.0):
  return magic(r=real, i=imag)

# 不建议 ❌
def complex(real, imag: np.array=0.0):
  return magic(r = real, i = imag)
```

避免行末空格

注释分隔符 (#) 与注释文本间插入一个空格

### 行管理

注释过长时，将注释放在单独的行上，而非代码行末尾，例

```Python
# 如果当前驱动版本不是最新版本，抛出过期警告并更新驱动 ✔️
if current_version != latest_version: # 如果当前驱动版本不是最新版本，抛出过期警告并更新驱动（过长）❌
    # 此处注释 ✔️
    warnings.warn('webdriver outdated') # 抛出驱动已升级警告（不过长）✔️
    get_latest_chrome_driver() # 升级驱动（不过长）✔️
    # ✔️
# ✔️
```

单行不宜过短、也不宜过长，建议以现代化分辨率 `(1920×1080, 2560×1440)` 下达到约一半屏幕宽时另起一行为标准

`.py` 脚本应以新空行结尾

在函数内部可以使用空行（尽量少）来分割逻辑上的代码块

`Docstring` 与其他编码间不需空行，双下划线语句与导入包之间空一行（__future__除外），函数、类、脚本全局变量、导入模块之间空两行，类内部的方法定义前后空一行。例

```Python
'''脚本描述''' # `Docstring` 与其他编码间不需空行
__all__ = [
    'something', 'and', 'something'
    ]

import numpy as np
import pandas as pd

import statsmodels.api as sm

from utils.functions import *
from utils.my_cache import cache_wrapper # 函数、类、脚本全局变量、导入模块之间空两行 (此处应换行，为阐明空两行而特地不换行)


GROUPS = 5 # 函数、类、脚本全局变量、导入模块之间空两行


@cache_wrapper(expire=60 * 60 * 24 * 30) # 函数、类、脚本全局变量、导入模块之间空两行
def group_and_statistic(α_matrix: pd.DataFrame | pd.Series, **kargs) -> None:
    '''函数描述''' # `Docstring` 与其他编码间不需空行
    pass


def α_na_ratio(any_matrix: pd.DataFrame) -> pd.Series: # 函数、类、脚本全局变量、导入模块之间空两行
    '''函数描述''' # `Docstring` 与其他编码间不需空行
    pass
    return pd.Series(None)

class BackTest(something):
    def __init__(self, *args, **kargs):
        super().__init__(self)
        pass # 类内部的方法定义前后空一行

    def some_func(self, *args, **kargs):
        pass # 以新空行结尾

```

### 包（模块）管理

与 PEP8 不同，如果有极简短的导入，我们建议合并为一行

> 我们建议

```Python
import os, sys
```

> 而非

```Python
import os
import sys
```

导入包应遵循一定规则，且不同的组应使用空行分隔，并考虑命名空间的覆写

1. 标准库导入
2. 相关的第三方包导入
3. 本地应用或库的特定导入

```Python
import numpy as np
import pandas as pd

import statsmodels.api as sm

from utils.functions import *
from utils.my_cache import cache_wrapper # 函数、类、脚本全局变量、导入模块之间空两行 (此处应换行，为阐明空两行而特地不换行)
```

使用相对路径导入包

### Docstring

`Docstring` 中不需添加编码格式、作者信息

> IDE将对 `Docstring` 进行自动提示，提示的开头应侧重对脚本的概述，而非编码与作者信息

> 根据 PEP3131，Python2 使用 ASCII，Python3 使用 utf-8，在文件中不需要进行编码声明。作者信息已包含在 `git` 中

`Docstring` 使用单引号声明

常规内容使用井号符 #，脚本描述与函数描述 (不包括类声明) 使用 `Docstring` (''' ''' 或 """ """，建议使用单引号) 进行注释

### 特殊标志

- 对重要内容、警示内容、疑问内容、待开发内容作特殊标识（参考附录中有关 Better Comments 的部分），例

```Python
# 常规注释
# * 重要内容
# ! 警示内容
# ? 疑问内容
# TODO: 待开发内容
```

### 代码即注释

避免过度注释

> 一般情况下，消耗在理解代码的时间大于代码被编写的时间，也存在简短且达到 `代码即 (英文) 注释` 的代码，以至于简单到不需注释

## 注释规范

集成开发环境 (IDE, Integrated Development Environment) 一般均可识别此处 `注释规范`，并为开发带来便利

### Docstring (函数)

> `Docstring` 分为脚本 (script) 及函数 (function)，此处以函数为例

> 注释后，对象 (Object) 会出现 `__doc__` 属性，用于存储注释内容

请参照以下例子进行函数 `Docstring` 编写

```Python
def intersect1d(ar1, ar2, assume_unique=False, return_indices=False):
    """
    此处概述函数的功能

    参数（二级标题，脚本的 `Docstring` 开头采用一级标题）
    ----------
    ar1, ar2 : array_like (数据类型)
        对参数的进一步描述
    assume_unique : bool
        对参数的进一步描述
    return_indices : bool
        对参数的进一步描述

        .. versionadded:: 首次加入该功能的包版本

    返回值
    -------
    intersect1d (返回的第一个参数) : ndarray (数据类型)
        对返回值的进一步描述
    comm1 (返回的第二个参数，该函数中有触发多返回值的操作): ndarray
        对返回值的进一步描述
    comm2 : ndarray
        对返回值的进一步描述

    相似实现方法
    --------
    numpy.lib.arraysetops : 对该方法的概述

    例子
    --------
    >>> np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1])
    array([1, 3])

    多个对象进行取交集时, 考虑使用 `functools.reduce`:

    >>> from functools import reduce
    >>> reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))
    array([3])

    当目的是获取交集的索引时:

    >>> x = np.array([1, 1, 2, 3, 4])
    >>> y = np.array([2, 1, 4, 6])
    >>> xy, x_ind, y_ind = np.intersect1d(x, y, return_indices=True)
    >>> x_ind, y_ind
    (array([0, 2, 4]), array([1, 0, 2]))
    >>> xy, x[x_ind], y[y_ind]
    (array([1, 2, 4]), array([1, 2, 4]), array([1, 2, 4]))
    """
```

### Docstring (脚本)

> 以下是一个范例：假设我们有一个 `error_handler.py` 脚本，它自定义了新的异常，允许用户自定义 `info` 级别的异常内容，并提供了一个函数式调用接口

请参照以下例子进行脚本 `Docstring` 编写

```Python
'''
自定义异常
============

这是用于自定义异常的模块
它包含了以下几类异常

1. 读取异常 `ReadError`
2. 处理异常 `HandleError`
3. 上传异常 `UploadError`

除此之外，还允许用户自定义 `info` 级别的异常内容，并通过 `RaiseReadError` 调用

ReadError 
---------
详细描述

...

RaiseReadError
---------
详细描述

示例
---------
'''
class ReadError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


def RaiseReadError(error: string) -> None:
    '''
    抛出内容为 `error` 的 `ReadError` 异常
    '''
    raise ReadError(error)
```

> `Docstring` 可以与声明符（三个引号）之间不换行。另外，此处 `RaiseReadError` 函数功能过于简单，达到了 `代码即 (英文) 注释` 的程度，此时应遵照 `简洁优于复杂` 原则，删除 `RaiseReadError` 函数的 `Docstring`

> 如果文档的内容较少，也可简要书写 `Docstring`，不必采用大小标题等划分工具

### Doctest (SKIP)

在 `Docstring` 中，我们使用三个大于号 `>>>` 来声明输入，并在下一行写入预期输出

对于函数的 `Docstring` 来说，此时 `Docstring` 包含 `Doctest`，可以预验证函数正确性

对于适应使用 `Jupyter NoteBook` 及不需进行自动化开发的开发者来说，这个功能较鸡肋以致不必遵守（SKIP）

以下为 `Doctest` 的例子

```Python
'''
Example 模块提供了一个函数 `factorial()` 例如

>>> factorial(5)
120
'''

def factorial(n: int | float):
    '''
    返回n的阶乘，n是一个大于等于0的精确整数

    参数与返回值
    ---------
    :param n: int | float, 大于等于0的精确整数
    :return: int, 数值上等于n的阶乘

    >>> [factorial(n) for n in range(6)] # `>>>` 来声明输入，并在下一行写入预期输出
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    浮点数的阶乘是可以的，但浮点数必须是一个精确的整数：
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    它也不能是一个非常大的数：
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    '''
    import math
    if not n >= 0:
        raise ValueError('n must be >= 0')
    if math.floor(n) != n:
        raise ValueError('n must be exact integer')
    if n+1 == n:
        raise OverflowError('n too large')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

执行 `python example.py -v` 可以得到函数正确性的预验证

```Shell
$ python example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
```

### TypeHint

`TypeHint` 用于声明函数参数数据类型及返回值类型

加入 `TypeHint` 以助于静态（未来可能有动态）类型检查，以及大语言模型的自动补全

我们在函数中加入参数注解、返回值后，函数的 `__annotations__` 属性会相应出现，例

```Python
def foo(a: 'x', b: 5 + 6 = 2, c: list = [3, 4]) -> max(2, 9):
    '''
    参数与返回值
    ---------
    :param a: 'x', 一般在此处作数据类型注解，但这里不是数据类型注解，此处参数 `a` 的注解为 `'x'`
    :param b: 11, `b` 的注解为 '11'，`b` 的默认值为 `2`)
    :param c: list, `c` 的注解为数据类型 `list`，默认值为 `[3, 4]`
    :return: 9, 返回值注解是9，根据下面函数定义，实际返回值固定为8`
    '''
    return 8

print(foo.__annotations__)

{'a': 'x',
 'b': 11,
 'c': list,
 'return': 9}
```

函数注释中的冒号遵循一般的加空格的规则，如果有箭头，要在其两边加空格

```Python
# 建议 ✔️
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

# 不建议 ❌
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

`__init__` 的返回值类型应为 `None`

请在 `Signature` 与 `TypeHint` 中选择 `TypeHint` 进行适配

## 代码约定

### 代码符号管理

`if not` 优于 `not if`

```Python
# 建议 ✔️
if foo is not None:
    
# 不建议 ❌
if not foo is None:
```

运算符需空一格

当运算符两侧是一个整体时不需空格、参数赋值不需加空格，变量赋值需要加空格

```Python
1 + 1 # 运算符需空一格
a *= 6 # 运算符需空一格
1+1 == 3 # 运算符左侧是一个整体，不需空格
factorial(n=5) # factorial为上述阶乘函数，参数赋值不需加空格
a = 6 # 变量赋值需要加空格
```

涉及到多行运算时，运算符写在变量前面，例

```Python
# 建议 ✔️
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# 不建议 ❌
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

### 学科规范

PEP3131 不建议使用非 `ASCII` 编码，但某些学科规范习惯使用非 `ASCII` 字符。以学科规范为准

> 金融学规范，如超额收益使用 `α` `alpha` 来表示，而非 `a` (如使用拉丁符 `α` 参考附录中有关 accent 的部分)

> 数学规范，如二维矩阵 (常见于 `pd.core.DataFrame` 等) 使用 `X` `Y` `Z` 等大写形式来表示，一维向量 (常见于 `pd.core.Series` 等) 使用 `x` `y` `z` 等小写形式来表示

### 函数约定

使用 `TypeHint`（见上一节：注释规范——TypeHint）

不使用lambda，lambda需转换为普通函数

函数以 `return` 结尾，即使 `return None`

优先使用 `''.startswith()` 或 `''.endswith()`

```Python
# 建议 ✔️
if foo.startswith('bar'):

# 不建议 ❌
if foo[:3] == 'bar':
```

优先使用 `isinstance()` 而不是 `type`

```Python
# 建议 ✔️
if isinstance(obj, int):

# 不建议 ❌
if type(obj) is type(1):

# 不建议 ❌
if type(obj) is int:
```

### 命名约定

定义类时采用大驼峰命令法 (Pascal Case)，例

```Python
class BackTest(): 建议 ✔️
    pass


class backtest(): 不建议 ❌
    pass
```

定义函数、变量时采用下划线命令法 (Underscore Case)，例

```Python
def get_α(return_data: pd.DataFrame | pd.Series) -> None:
    pass
```

定义常量时采用全大写; 常量单独建立脚本并采用模块导入方式使用，或使用数据库来流式存储使用

> 常量往往会被调整，而开发者需要快速定位调整位置并在全局应用调整

### 异常处理

捕获异常时，尽可能使用明确的异常或异常链，而不是使用空except，例

```Python
>>> try:
...     print(1 / 0)
... except Exception as caught_exception: # 建议 ✔️
...     raise RuntimeError("Something bad happened") from caught_exception
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: int division or modulo by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
```

```Python
>>> try:
...     print(1 / 0)
... except: # 不建议 ❌
...     raise RuntimeError("Something bad happened") # 不建议 ❌
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: int division or modulo by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
```

```Python
>>> try:
...     print(1 / 0)
... except ZeroDivisionError: # 建议 ✔️
...     print('Something bad happened')
...
Something bad happened
```

## 附录

Python-Community:

- [PEP8](https://peps.python.org/pep-0008/)
- [PEP257](https://peps.python.org/pep-0257/)
- [PEP484](https://peps.python.org/pep-0484/)
- [PEP526](https://peps.python.org/pep-0526/)
- [PEP3107](https://peps.python.org/pep-3107/)
- [PEP3131](https://peps.python.org/pep-3131/)
- [Doctest Practice](https://docs.python.org/3/library/doctest.html)
- [Annotations Practice](https://docs.python.org/3/howto/annotations.html)

Third-Party-Official:

- [Numpy](https://github.com/numpy/numpy)
- [Google Python Guide](https://google.github.io/styleguide/pyguide.html)
- [Microsoft C Guide](https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/coding-style/coding-conventions)

Third-Party-Dev:

- [Pylance](https://github.com/microsoft/pylance-release)
- [Better-Comments](https://github.com/aaron-bond/better-comments)
- [Intellicode](https://github.com/MicrosoftDocs/intellicode)
- [Spell Check](https://github.com/streetsidesoftware/vscode-spell-checker)
- [Mac Accent](https://www.w3.org/Amaya/User/doc/ShortCuts-MacOSX.html)
- [Windows Accent](https://learn.microsoft.com/en-us/windows/powertoys/quick-accent)
