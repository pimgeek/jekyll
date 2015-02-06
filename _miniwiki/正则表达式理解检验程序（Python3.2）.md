---
layout: post
title: 正则表达式理解检验程序（Python3.2）
permalink: 1423195210.html
date: 2014/01/01
---

下面是一个用 Python 写成的脚本程序。我们用它来检验一位程序员对正则表达式基本语法的理解是否准确。

使用方法：把以下源码完整地复制粘贴到一个 Python 源码文件中，例如 ```regex_test.py``` ，然后在 linux 环境下执行 ```/path_to_your_python_source_dir/regex_test.py``` 命令把它运行起来。

先需条件：你的系统上必须首先安装了 Python3.2

```python
#!/usr/bin/python3.2

import re
import time
import sys

# 定义按下任意键继续函数
def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

# 定义理解检验函数
def verify_understanding(regex_string, target_string):
    print("----------------------------------------")
    regex_compiled = re.compile(regex_string)
    print("尝试用 r'%s' 匹配 '%s' 的任意子串" % (regex_string, target_string))
    search_result = regex_compiled.search(target_string)
    print("你觉得能否匹配? [y\\n]: ", end="")
    sys.stdout.flush(), getch(), print("")
    if search_result:
        print("能匹配吗?: 可以匹配 √")
        print("具体匹配到什么?: '%s'" % search_result.group())
    else:
        print("能匹配吗?: 不能匹配 ×")
    print("按回车键进行下一项理解检验......")
    input()

def run_verification_series_001():
    # 正则表达式的 . 字符理解检验 1
    verify_understanding(r'.', "a")

    # 正则表达式的 . 字符理解检验 2
    verify_understanding(r'.', "好")

    # 正则表达式的 . 字符理解检验 3
    print("注意：这里的 '\n' 表示换行符 \\n ")
    verify_understanding(r'.', "\n")

    # 正则表达式的 \ 字符理解检验 1
    verify_understanding(r'\.', ".")

    # 正则表达式的 \ 字符理解检验 2
    verify_understanding(r'\.', "a")

    # 正则表达式的 \ 字符理解检验 3
    print("注意：这里的 '\n' 表示换行符 \\n ")
    verify_understanding(r'\n', "n")

    # 正则表达式的 \ 字符理解检验 4
    print("注意：这里的 '\n' 表示换行符 \\n ")
    verify_understanding(r'\n', "\n")

    # 正则表达式的 \ 字符理解检验 5
    verify_understanding(r'\\', "\\")

    # 正则表达式的 \ 字符理解检验 6
    verify_understanding(r'\(', "(")

    # 正则表达式的 [] 字符理解检验 1
    verify_understanding(r'[ab]', "a")

    # 正则表达式的 [] 字符理解检验 2
    verify_understanding(r'[ab]', "b")

    # 正则表达式的 [] 字符理解检验 3
    verify_understanding(r'[ab]', "zzza")

    # 正则表达式的 [] 字符理解检验 4
    verify_understanding(r'[ab]', "dadd")

    # 正则表达式的 [] 字符理解检验 5
    verify_understanding(r'[ab]', " b ")

    # 正则表达式的 [] 字符理解检验 6
    verify_understanding(r'[a-z]', "fox")

    # 正则表达式的 [] 字符理解检验 7
    verify_understanding(r'[0-9]', "z863b")

    # 正则表达式的 [] 字符理解检验 8
    verify_understanding(r'[a-z0-9]', ".")

    # 正则表达式的 [] 字符理解检验 9
    verify_understanding(r'[ab09]', "rgb")

def run_verification_series_002():
    # 正则表达式的 . 字符理解检验 1
    print("注意：这里的 '\t' 表示制表符 \\t ")
    verify_understanding(r'.', "\t")

    # 正则表达式的 . 字符理解检验 2
    verify_understanding(r'.', "\\")

    # 正则表达式的 [] 字符理解检验 1
    verify_understanding(r'[ab]{2}', "a")

    # 正则表达式的 [] 字符理解检验 2
    verify_understanding(r'[ab]{1}', "b")

    # 正则表达式的 [] 字符理解检验 3
    verify_understanding(r'[abyz]{3}', "zzza")

    # 正则表达式的 [] 字符理解检验 4
    verify_understanding(r'[ab]{4}', "dadb")

    # 正则表达式的 [] 字符理解检验 5
    verify_understanding(r'[ab]{1}', " b ")

    # 正则表达式的 [] 字符理解检验 6
    verify_understanding(r'[a-z]{3}', "fox")

    # 正则表达式的 [] 字符理解检验 7
    verify_understanding(r'[0-9]{3}', "z863b")

    # 正则表达式的 [] 字符理解检验 8
    verify_understanding(r'[a-z0-9]{0}', ".")

    # 正则表达式的 [] 字符理解检验 9
    verify_understanding(r'[a-z09]{5}', "0rgb9")

# 开始运行理解检验序列
# run_verification_series_001()
run_verification_series_002()
```