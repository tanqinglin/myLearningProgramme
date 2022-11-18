# Python3

### 一、格式化字符串：  

1、
```python
print('Hi, %s, you have $%d.' %('Michael', 10000))
```

2、format()
```python
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
```

3、f-string
```python
r = 2
s = 3.14 * r ^^ 2
print(f'The area of the circle with radius {r} is {s:.2f}')
```

---

### 二、list

```python
name = ['Bob', 'Trace']
print(len(name), name[0], name[-1])
```
- append
- insert
- pop( `name.pop()`、`name.pop(0)` )

---

### 三、tuple

```python
t = tuple(1,)
# 区别于小括号
```
- `tuple` 具有不变性，内嵌的 `list` 可以改变。

---

### 四、range
```python
for person in list(range(100)):
    print('Hi, {person}')
```

---

### 五、break & continue

- `break` 的作用是提前结束循环。
- `continue` 的作用是跳过当前循环。

---

### 六、dict

```python
d = {'Michael': 95, 'Bob': 89, 'Tracy': 93}
if 'Michael' in d:
    print(d[Michael])
```
- pop( `'key'`)

- `dict` 中的 `key` 必须为不可变对象。

---

### 七、set

```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(f's1 & s2 = {s1 & s2}, s1 | s2 = {s1 | s2}')
```

- add()
- remove()

---

### 八、函数

- 检查函数类型并在类型错误时抛出异常：

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad oprand type')
    if x >= 0:
        print(x)
    else:
        print(-x)
```

- 从终端调入 `func.py` 文件中的函数：

```python
import my_abs(x) from func
```

---

### 九、参数

- 可变参数：
```python
def sum(*numbers):
    for i in numbers:
        print(i)
```

- 关键字参数： 
```python
def sum(**kw):
```
关键字参数允许你传入0个或任意个含参数名的参数， `kw` 是一个 `dict` 。

- 命名关键字参数：
```python
def person(name, age, *, city, job):
```

---

### 十、列表生成式

```python
[x * x for x in range(1,11) if x % 2 ==0]
[m + n for m in 'ABC' for n in 'XYZ']

dict = {'a': 1, 'b': 2, 'c': 3}
for x,y in dict.items():
    print(x, '=', y)

[x if x % 2 == 0 else -x for x in range(1,11)]
```

---

### 十一、生成器

`generator` 是可迭代对象。

把函数的输出如 `print(b)` 变为 `yield(b)` 能够变成 `generator` 函数。

这里，最难理解的就是 `generator` 函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到 `return` 语句或者最后一行函数语句就返回。而变成 `generator` 的函数，在每次调用 `next()` 的时候执行，遇到 `yield` 语句返回，再次执行时从上次返回的 `yield` 语句处继续执行。

---

### 十二、`map` / `reduce` / `filter` / `sorted`

```python
from functools import reduce
L1 = list(map(abs, [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]))
L2 = reduce(sum, [1, 2, 3, 4, 5])
```

`filter` 用于筛选：
```python
def is_odd(val):
    return val % 2 == 1
L1 = filter(is_odd, [1, 2, 3, 5, 44, 49, 79])
```

`sorted` 可包含 `key` 函数 、 `reverse` 参数

---

### 十三、函数对象与装饰器

- 函数对象有一个 `__name__` 属性，通过 `实例.__name__` 可以返回函数的名字。

装饰器：
```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__ )
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2022-08-03')

now()
```

为防止函数装饰器更改了函数的 `__name__` ，需要导入 `functools` ，并在定义 `wrapper()` 的前面加上 `@functools.wraps(func)` 

---

### 十四、模块

- 每一个包目录下面都会有一个 `__init__.py` 的文件，这个文件是必须存在的，否则， `Python` 就把这个目录当成普通目录，而不是一个包。

- 作用域：在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在 `Python` 中，是通过 `_` 前缀来实现的。

1. 公开变量，如： `abc` 、 `m` 、 `n`
2. 特殊变量，如： `__name__` 、 `__author__`
3. 非公开变量，如：`_abc`

- 2 和 3 都是非公开对象（包括变量和函数）。

---

### 十五、类型判断

```python
import types

def fn():
    pass

type(fn) == types.FunctionType

type(abs) == types.BuiltinFuntionType

type(lambda x: x) == types.LambdaType

type((x for x in range(10))) == types.GeneratorType

isinstance(h, Animal) # 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
```

---

### 十六、操作类的状态

```python

class MyObject(object):
    
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x ** 2

j1 = hasattr(obj, 'x')
print(obj.x)
j2 = hasattr(obj, 'y') # false
setattr(obj, 'y', 19)
val = getattr(obj, 'y', 404) # 如果不存在相应的查找属性，则返回默认值404

```

实例属性优先级比类属性高。

- `class` 内部的变量不是简单的引用关系，试图用 `global` 或 `nonlocal` 声明，但无效，回头再看一遍教程发现类属性调用使用 `类名.属性名` 进行调用，无论是在封装的内部还是在外部都一概如此。

---

### 十七、使用 `__slots__`

给实例绑定一个方法：

```python
class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
getattr(s, 'age', 404)
```

`__slot__` 用于限制实例绑定属性，比如，只允许 `Student` 实例绑定 `name` 和 `age` 属性：

```python
class Student(object):
    __slots__ = ('name', 'age')
```

使用 `__slots__` 要注意，`__slots__` 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。  

除非在子类中也定义 `__slots__` ，这样，子类实例允许定义的属性就是自身的 `__slots__` 加上父类的 `__slots__` 。

---

### 十八、使用 `@property`

`Python` 内置的 `@property` 装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        elif value < 0 or value > 100 :
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score = value
```

把一个 `getter` 方法变成属性，只需要加上 `@property` 就可以了，此时，`@property` 本身又创建了另一个装饰器 `@score.setter`，负责把一个 `setter` 方法变成属性赋值，于是，我们就拥有一个可控的属性操作。

练习：请利用 `@property` 给一个 `Screen` 对象加上 `width` 和 `height` 属性，以及一个只读属性 `resolution`：

```python
class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
```

---

### 十九、枚举

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

### 二十、正则表达式

- 精确匹配：用 `\d` 可以匹配一个数字，`\w` 可以匹配一个字母或数字，`.` 可以匹配任意字符。`\-` 匹配`-`。`\s`匹配空格。

- 匹配变长字符：用 `*` 表示任意个字符（包括`0`个），用 `+` 表示至少一个字符，用 `?` 表示`0`个或`1`个字符，用 `{n}` 表示`n`个字符，用 `{n,m}` 表示`n-m`个字符。

例子：`\d{3}\s+\d{3,8}`

#### ___进阶：___

- `[0-9a-zA-Z\_]` 可以匹配一个数字、字母或者下划线；
- `[0-9a-zA-Z\_]+` 可以匹配至少由一个数字、字母或者下划线；
- `[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}` 更精确地限制了变量的长度是 `1-20` 个字符（前面`1`个字符+后面最多`19`个字符）。
- `A|B` 可以匹配`A`或`B`，所以`(P|p)ython`可以匹配`Python`或者`python`。
- `^` 表示行的开头，`^\d` 表示必须以数字开头。
- `$` 表示行的结束，`\d$` 表示必须以数字结束。

#### ___re模块：___

```python
import re
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')
else:
    print('failed')
```

#### ___切分字符串：___

```python
re.split(r'\s+', '   a  b  _ c')
```

### ___分组：___

```python
import re
m = re.match('^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups)
```

- 预编译：

```python
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('020-95596').groups)
```
---

### 二十一、常见内置模块

- `datetime`

```python
from datetime import datetime
now = datetime.now()
print(now)
dt = datetime(2022, 8, 4, 16, 55, 30)
t = dt.timestamp()
print(datetime.timestamp(t))
```


