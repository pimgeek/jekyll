---
layout: post
title: Python 学习任务：理解这段代码，并设法让它给出预期的输出
permalink: 1422000527.html
date: 2015/01/23
---

```python
#!/usr/bin/python

def transfer(s):
    length=len(s)
    n=1

    newstring=" " * (length + 2)
    s = s + "  "

    # newstring[0]=s[0].upper
    newstring=str_modify(newstring, 0, s[0].upper())

    while length - n>0:
        if s[n]=="-":
            # newstring[n]=""
            newstring=str_modify(newstring, n, "")

            # newstring[n+1]=s[n+1].upper
            newstring=str_modify(newstring, n+1, s[n+1].upper())
            n=n+2
        else:
            # newstring[n]=s[n].lower
            newstring=str_modify(newstring, n, s[n].lower())
            n=n+1

    print newstring

def str_modify(s,m,elem):
    charlst = list(s)
    charlst[m] = elem
    return "".join(charlst)

# expected output = BorderBottomColor
transfer("border-bottom-color")
```