# 后端 (Python) 代码规范
(Backend Code Style Guide)

## 来源声明 (Source Declaration)

本文档严格遵循 **Google Python Style Guide** (谷歌 Python 风格指南) 作为核心规范。

**官方链接:** [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)

---

## 关键规范摘要

### 1. 缩进与行长
* **缩进:** 必须使用 **4 个空格** 进行缩进。禁止使用 Tab。
* **行长:** 每行代码最大长度不应超过 **80 个字符**。

### 2. 命名规范 (Naming Conventions)
* **模块/文件名:** `lowercase_with_underscores.py` (小写+下划线), 例如 `people.py`。
* **函数/变量:** `lowercase_with_underscores` (小写+下划线), 例如 `fetch_contacts`。
* **类名:** `CapWords` (大驼峰命名法), 例如 `class Contact(db.Model)`。
* **常量:** `ALL_CAPS` (全大写+下划线), 例如 `API_BASE_URL`。

### 3. 导入 (Imports)
* 禁止使用通配符导入 (`from module import *`)。
* 导入应按“标准库”、“第三方库”、“本项目库”的顺序分组，组间空一行。

### 4. 注释与文档字符串 (Docstrings)
* 所有公共模块、函数、类和方法都必须有文档字符串 (`""" ... """`)。
* 遵循 Google Docstring 格式，清晰描述 `Args:` (参数) 和 `Returns:` (返回值)。

### 5. 空格使用
* 在操作符 (`=`, `==`, `+=`) 两侧各使用一个空格。
* 在逗号 (`,`) 后面使用一个空格。
* 函数定义的括号 `def my_func(arg1, arg2)` 和函数调用的括号 `my_func(1, 2)` 内部不加空格。
