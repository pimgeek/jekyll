---
layout: post
title: 正则表达式理解检验程序（Python3.2）
permalink: 1423195210.html
date: 2014/01/01
---

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
    print("匹配结果: ", end=""), print(search_result)
    if search_result:
        print("匹配子串: '%s'" % search_result.group())
    else:
        print("匹配子串: ''")
    print("按回车键进行下一项理解检验......")
    input()

def run_verification_series():
    # 正则表达式的 . 字符理解检验 1
    verify_understanding(r'.', "a")

    # 正则表达式的 . 字符理解检验 2
    verify_understanding(r'.', "好")

    # 正则表达式的 . 字符理解检验 3
    verify_understanding(r'.', "\n")

    # 正则表达式的 \ 字符理解检验 1
    verify_understanding(r'\.', ".")

    # 正则表达式的 \ 字符理解检验 2
    verify_understanding(r'\.', "a")

    # 正则表达式的 \ 字符理解检验 3
    verify_understanding(r'\n', "n")

    # 正则表达式的 \ 字符理解检验 4
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

# 开始运行理解检验序列
run_verification_series()
```