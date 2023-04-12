# Python 代码指南

遵从代码指南以实现以下目的：

✅ 为代码创建一致的外观，确保审阅代码（Code Review）时专注于内容而非布局

✅ 使大语言模型（LLM, Large Language Model）可以基于既有内容更准确理解与辅助编写代码

✅ 提高代码复用性，便于复制、更改和维护代码

✅ 展现 Python 最佳写法（Code Pride）

## 目录

- [Python 代码指南](#python-代码指南)
  - [目录](#目录)
  - [前言](#前言)
  - [注释](#注释)
    - [缩进](#缩进)
    - [语言](#语言)
    - [符号](#符号)
    - [行管理](#行管理)
    - [Docstring](#docstring)
    - [标识](#标识)
    - [commit](#commit)
    - [避免过度注释](#避免过度注释)
  - [代码](#代码)
    - [符号](#符号-1)
    - [学科规范](#学科规范)
    - [函数](#函数)
    - [命名](#命名)
    - [缓存](#缓存)
    - [计算精度](#计算精度)
    - [异常处理](#异常处理)
    - [日志捕获](#日志捕获)
  - [集成开发环境增强](#集成开发环境增强)
    - [Docstring (函数)](#docstring-函数)
    - [Docstring (脚本)](#docstring-脚本)
    - [TypeHint](#typehint)
  - [附录](#附录)
    - [参考](#参考)
    - [Code插件](#code插件)

## 前言

- 项目优于具体语言

> 项目涉及多语言编程时，其他语言代码指南可能与本指南冲突。如果有确定的项目指南，冲突时，项目指南优先级更高

- 包含约定（Convention）和规范（Standard）

> 约定（Convention）为一致的外观服务
>
> 规范（Standard）为实际功能服务，按照规范编写有助于集成开发环境增强及AI补全

- 是否遵循指南与程序失败无关

- 更新，以保持先进性

> 指南不完美，有补充就开Issue
>
> 每隔固定时间（暂定半年）或出现较大技术进步时，适时发布更新

- 使用较新且包兼容性较好的Python大版本，小版本保持最新

> 比如最新大版本是3.11，考虑包兼容性的问题，建议大版本使用3.10或3.9，小版本保持最新

- AI不一定正确且准确

> 使用大语言模型作代码补全后，需再检查一遍AI生成内容是否正确且准确

## 注释
### 缩进

缩进距离建议采用制表符（或4个空格）

单行不宜过短、也不宜过长，建议以现代化分辨率 `(1920×1080, 2560×1440)` 下达到约一半屏幕宽时另起一行

不鼓励完全参照PEP8进行缩进管理，它往往对一些不必换行的代码进行换行（console、低分辨率显示器编辑代码已经是过去式了！）另外，在不影响运行的情况下，它的规则也太多太难记了！

### 语言

统一注释语言，使用中文注释，必要时辅以英文

> 我们有 120% 把握确定，基于目前发展阶段，使用中文注释有利于提高全流程协作效率
>
> 我们仍希望协作者拥有良好英文读写能力，代码请使用英文编写

对于英文缩写、专有名词，附英文缩写全称，例

```Python
# DEF (违约因子, default) ✔️
# DEF (违约因子) ❌ 仅附了中文名称，没有附英文缩写全称
DEF = complicated_function_returning_a_matrix(args, kargs)
```

英文注释时，以大写字母开始注释正文

对标点符号没有语言要求，灵活度较高，但原则上要求与前后文语境语言一致。中英混杂标点语法示例（草稿）

- 这是一<font color=red>份 "Hello</font> World" 的注释范例

> 左中文字符和右英文符号之间空一格
>
> 英文符号和英文正文间无空格

- <font color=red>它（即</font> Hello <font color=red>World）</font>是每位编程者入门时，或早或晚、或多或少都会接触到的内容，不是吗？

> 前后文语境是中文时，采用中文标点符号
>
> 左英文字符和右中文符号之间不空格

使用英文时，请正确拼写单词（见附录 `spell check`）

### 符号

结束注释文本不需标点符号

避免多余空格

```Python
open(f'{python_path}\\zipped_chrome_driver.zip', 'wb').write(package.content)
# 二进制格式写入 (wb, write binary) ✔️
# 二进制格式写入 ( wb, write binary ) ❌
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
```
---

脚本换行见下例

```Python
'''脚本描述''' # `Docstring` 与其他代码间不需空行
__all__ = [
    'something', 'and', 'something'
    ]

import numpy as np
import pandas as pd

import statsmodels.api as sm

from utils.functions import some_function
from utils.evaluate import something


GROUPS = 5 # 函数、类、脚本全局变量、导入模块之间空两行


@cache_wrapper(expire=60 * 60 * 24 * 30) # 函数、类、脚本全局变量、导入模块之间空两行
def group_and_statistic(α_matrix: pd.DataFrame | pd.Series, **kargs) -> None:
    '''函数描述''' # `Docstring` 与其他代码间不需空行
    pass


def α_na_ratio(any_matrix: pd.DataFrame) -> pd.Series: # 函数、类、脚本全局变量、导入模块之间空两行
    '''函数描述''' # `Docstring` 与其他代码间不需空行
    pass
    return pd.Series(None)


class BackTest(something):
    def __init__(self, *args, **kargs):
        super().__init__(self)
        pass # 类内部的方法定义前后空一行，类定义和__init__不空行

    def some_func(self, *args, **kargs):
        pass # 脚本结束以新空行结尾

```

- 在函数内部可以使用空行（尽量少）来分割逻辑上的代码块

- `Docstring` 与其他代码间不需空行，双下划线语句与导入包之间空一行（__future__除外），函数、类、脚本全局变量、导入模块之间空两行，类内部的方法定义前后空一行

- 不同的组别的包应用一个空行分隔，并考虑命名空间的覆写。使用相对路径导入本地包

1. 标准库导入
2. 相关的第三方包导入
3. 本地导入

> 当然，这里对空行的建议也有些繁文缛节的感觉，不过为了格式规整，还是遵循吧！

---

矩阵等多行结构进行换行

```Python
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
### Docstring

`Docstring` 中不需添加编码格式、作者信息

> IDE对 `Docstring` 进行自动提示，提示的开头应侧重对脚本的概述，而非编码与作者信息

> 根据 PEP3131，Python3 默认使用 utf-8（Python2 为ASCII），在文件中不需要进行编码声明。作者信息已包含在 `.git` 中

常规内容使用井号符 #，脚本描述与函数描述 (不包括类声明) 使用 `Docstring` (''' ''' 或 """ """，建议使用单引号) 进行注释

### 标识

- 对重要内容、警示内容、疑问内容、待开发内容作特殊标识（见附录 Better Comments），例

```Python
# 常规注释
# * 重要内容
# ! 警示内容
# ? 疑问内容
# TODO 待开发内容
```

### commit

格式

```
<type>(<scope>): <subject>
```

1. type用于说明commit的类别，使用以下标识（参考commitlint）

- feat：新功能（feature）

- fix：说明bug并修复bug

- stage：说明bug但不（完全）修复bug，适用于多次提交。最终修复时使用fix

- perf：优化（performance）

- refactor：重构

- docs：文档（documentation）

- revert：版本回滚

- style：风格

- test：测试

- chore：构建过程变动或辅助工具变动等

2. scope(可选)

scope用于说明commit影响的范围，比如 `level0, level1, 全局` 等等，视项目不同而不同

3. subject

subject是commit的简短描述，不超过50个字符。使用中文，结尾不加句号或其他标点符号

### 避免过度注释

一般情况下，消耗在理解代码的时间大于代码被编写的时间，也存在简短且达到 `代码即 (英文) 注释` 的代码，以至于简单到不需注释

## 代码
### 符号

避免多余空格

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

逗号后面右括号

```Python
# PEP8 建议
foo = (0,)

# 但我们建议
foo = (0, )
```

逗号，分号，和冒号之后加空格

```Python
if x == 4: print x, y; x, y = y, x ✔️
if x == 4 : print x , y ; x , y = y , x ❌
```

不同于PEP8，我们建议对冒号采用标准英文符号语法，不必遵循新订的条条框框

---

对于运算符空格，见下例

```Python
i = i + 1 # 不存在优先级
submitted += 1 # 不存在优先级
x = x*2 - 1 # 存在两种优先级
c = ((a+b) * (a-b)) ** 2 # 存在两种优先级
1+1 == 3 # 运算符左侧是一个整体，不需空格
factorial(n=5) # 参数赋值不需加空格
a = 6 # 变量赋值需要加空格

# 涉及到多行运算时，运算符写在变量前面 ✔️
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# ❌
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

- 运算符不存在优先级时，运算符两边增加空格

- 存在不同优先级的运算符时，在不同优先级运算符之间加空格

- *存在复杂运算时，将它拆为多个简短的、含两种或以下优先级的算式，并使用有意义的单词声明中间变量*

- 运算符两侧是一个整体时不需空格

- 参数赋值不需加空格，变量赋值需要加空格

- 涉及到多行运算时，运算符写在变量前面

---

表示默认参数或关键字参数时，等号两边不加空格。默认参数有参数注解时加空格

```Python
def complex(real, imag=0.0, modify: list = [1, 2]): # 默认参数
  return magic(r=real, i=imag) # 关键字参数
```

`if not` 优于 `not if`

```Python
# 建议 ✔️
if foo is not None:
    
# 不建议 ❌
if not foo is None:
```

### 学科规范

PEP3131 不建议使用非 `ASCII` 编码，但某些学科规范习惯使用非 `ASCII` 字符。以学科规范为准

> 金融学规范，如超额收益使用 `α` `alpha` 来表示，而非 `a` (如使用拉丁符 `α` 见附录 accent 部分)

> 数学规范，如二维矩阵 (常见于 `pd.core.DataFrame, np.ndarray` 等) 使用 `X` `Y` `Z` 等大写形式来表示，一维向量 (常见于 `pd.core.Series, np.ndarray` 等) 使用 `x` `y` `z` 等小写形式来表示

对于金融数据，无论怎样处理，总存在两个往往会被调整的量——标的和时间，在编写脚本时不应将这两个量写死

### 函数

不使用lambda，lambda需转换为普通函数

> lambda的写法虽然很Pythonic，但是它只对写的人很Pythonic。它是代码审阅人的噩梦，即使是未来的你！

函数以 `return` 结尾，即使 `return None`

处理字符串，优先使用 `''.startswith()` 或 `''.endswith()`

```Python
# 建议 ✔️
if foo.startswith('bar'):

# 不建议 ❌
if foo[:3] == 'bar':
```

处理类型匹配，优先使用 `isinstance()` 而不是 `type`

```Python
# 建议 ✔️
if isinstance(obj, int):

# 不建议 ❌
if type(obj) is type(1):

# 不建议 ❌
if type(obj) is int:
```

### 命名

定义类时采用大驼峰命名法 (Pascal Case)，例

```Python
class BackTest():
    pass
```

定义函数、变量时采用下划线命名法 (Underscore Case)，例

```Python
def get_α(return_data: pd.DataFrame | pd.Series) -> None:
    pass
```

定义常量时采用全大写

另外，建议将常量单独建立脚本并采用模块导入方式使用，或使用数据库来流式调用

> 常量往往会被调整，而开发者需要快速调整并在全局应用调整

脚本命名使用下划线命名法 (Underscore Case)

脚本命名不要用自定义缩写，约定俗成缩写的除外

> 脚本命名无法补写英文全称，仅看缩写会让人感到困扰，例如 `kbm.py (keyboard_marco)` 等
>
> 约定俗成的，例如 `db.py (database), cmd.py (command)` 等。例，以谷歌搜索 `what is db in computer programming` 能得到正确结果（database）为约定俗成的判断标准

### 缓存

对于复用性高、计算量大的部分，可考虑将其整合成一个缓存文件（中间量等），或建立数据库（因子等）

缓存文件示例

```Python
import hashlib
from diskcache import Cache
from functools import wraps

def cache_wrapper(directory: str = 'cache', expire: int = 60 * 60 * 24):
    cache = Cache(directory=directory)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = func.__name__ + ':' + hashlib.md5((func.__name__ + str(args) + str(kwargs)).encode('utf-8')).hexdigest()
            result = cache.get(key)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            cache.set(key, result, expire)
            return result
        return wrapper
    return decorator

# 以函数名及函数参数为键，函数返回值为值，缓存该结果到指定目录，并保存指定秒数
@cache_wrapper('/tmp/project_name/function_name', 60 * 60 * 24)
def big_calculation(x, y, z, a, b, c, d, e, α, β):
    pass
    return something

```

### 计算精度

在计算资源允许的情况下，计算时精度保留到最高，仅展示时允许降低精度

### 异常处理

捕获异常时，尽可能考虑到、明确出将出现的异常，并给出建议

> 建议使用较新版本Python，老版本Python没有异常链等特性

```Python
>>> try:
...     print(1 / 0)
... except ZeroDivisionError: # 建议 ✔️
...     print('Something bad happened, check the denominator may help')
...
Something bad happened, check the denominator may help
```

异常处理使用简短的英文撰写，参考注释格式

> 每次只会出现一个异常链，阅读量小
> 
> 与通用包的异常保持风格统一

### 日志捕获

日志应包含——时间和该代码在项目中的大致位置

日志应划分等级，比如

- debug（一般开发环境）

- info（协同开发及代码审查）

- critical（严重错误，应立即修正）

日志建议使用 `logging` 模块，或考虑把 `print`、报错和 `stdout`, `stderr` 整合

建立通过微信/邮件等提醒渠道，以在出现严重错误时及时修正

日志使用简短的中文撰写

> 阅读量大
> 
> 不需考虑通用包的风格统一

## 集成开发环境增强

集成开发环境 (IDE, Integrated Development Environment) 一般均可识别此处注释规范，并为开发带来便利

### Docstring (函数)

> `Docstring` 分为脚本 (script) 及函数 (function)，此处以函数为例
>
> 注释后，对象 (Object) 会出现 `__doc__` 属性，用于存储注释内容
>
> 不需对每个函数都进行 `Docstring` 编写，只需编写复用度高的函数即可

函数 `Docstring` 例子

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

以下是一个范例：假设我们有一个 `error_handler.py` 脚本，它自定义了新的异常，允许用户自定义 `info` 级别的异常内容，并提供了一个函数式调用接口

> 不需对每个脚本都进行 `Docstring` 编写，只需编写复用度高的脚本即可

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
    raise ReadError(error)
```

> `Docstring` 可以与声明符（三个引号）之间不换行。另外，此处 `RaiseReadError` 函数功能过于简单，达到了 `代码即 (英文) 注释` 的程度，此时 `简洁优于复杂` ，删除 `RaiseReadError` 函数的 `Docstring`

> 如果脚本复用度高，但是内容较少，可简要书写 `Docstring`，不必采用大小标题等工具

### TypeHint

`TypeHint` 一般用于声明函数参数数据类型及返回值类型

加入 `TypeHint` 以助于静态（未来可能动态）类型检查

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

函数注解中的冒号一般加空格，如果有箭头，要在其两边加空格

```Python
# 建议 ✔️
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

# 不建议 ❌
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

`__init__` 的返回值类型一般为 `None`

## 附录

### 参考

Python-Community:

- [PEP8](https://peps.python.org/pep-0008/)
- [PEP257](https://peps.python.org/pep-0257/)
- [PEP484](https://peps.python.org/pep-0484/)
- [PEP526](https://peps.python.org/pep-0526/)
- [PEP3107](https://peps.python.org/pep-3107/)
- [PEP3131](https://peps.python.org/pep-3131/)
- [Annotations Practice](https://docs.python.org/3/howto/annotations.html)

Third-Party-Official:

- [Numpy](https://github.com/numpy/numpy)
- [Google Python Guide](https://google.github.io/styleguide/pyguide.html)
- [Microsoft C Guide](https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/coding-style/coding-conventions)

Third-Party-Dev:

- [commitlint](https://marketplace.visualstudio.com/items?itemName=joshbolduc.commitlint)
- [better-comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- [code-spell-checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Accent, mac](https://www.w3.org/Amaya/User/doc/ShortCuts-MacOSX.html#:~:text=M%20Ctrl%20Z-,Alphabet%20grec,-alpha%20%3A%20%CE%B1%2C%20%CE%91)
- [Accent, windows](https://learn.microsoft.com/en-us/windows/powertoys/quick-accent)

### Code插件

除参考外，建议使用的Code插件

- [intellicode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- [copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilotvs)
- [copilot-labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs)
- [github-markdown-preview](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview)
- [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [themeswitch](https://marketplace.visualstudio.com/items?itemName=Fooxly.themeswitch)
- [markdown-all-in-one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [database-client](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-database-client2)
