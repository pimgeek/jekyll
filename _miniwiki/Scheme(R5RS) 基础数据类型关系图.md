---
layout: post
title: Scheme(R5RS) 基础数据类型关系图
permalink: 1421029752.html
date: 2014/05/24
---

前段时间，我在研究和学习 [scheme](http://zh.wikipedia.org/zh-cn/Scheme) 这门 [lisp 家族的编程语言](http://zh.wikipedia.org/wiki/Category:LISP%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80%E5%AE%B6%E6%97%8F)。所谓的 [R5RS](http://www.schemers.org/Documents/Standards/R5RS/HTML/) 是一份被广泛接受的 scheme 的语言标准(在国内，有北大数学科学学院的人 [尝试翻译了这份文稿](http://www.math.pku.edu.cn/teachers/qiuzy/progtech/scheme/r5rscn.pdf))。

绘制这张信息图的上下文是：我在编程实践中经常需要思考 scheme 语言各种基础数据类型之间的关系，以便在对输入数据做类型判断时，排除某些特定的情况。为了自己查阅方便，我利用 [yEd 绘图工具](http://www.yworks.com/en/products_yed_about.html) 动手绘制了一张基础数据类型之间的相互关系图。

因为担心自己的理解有误，所以我特意到 [Stackoverflow.com](http://stackoverflow.com/) 这个编程开发者经常去做互动问答的网站上 [咨询了一番](http://stackoverflow.com/questions/20824054/could-this-diagram-illustrate-the-relations-between-r5rs-scheme-primitive-data-t)。经过多次反复讨论，我得到了一张经过两次改进的关系图（这里我要感谢 Stackoverflow.com 的用户 [Chris Jester-Young](http://stackoverflow.com/users/13/chris-jester-young) 提供耐心讲解)：

![image](https://cloud.githubusercontent.com/assets/1609306/3074019/b0368792-e31d-11e3-8263-c9ebac33c591.png)

希望这张图对我自己有用，若能帮到其他学习 scheme 语言的新手，那就再好不过了。

如果你还没有接触过 scheme 语言，我推荐你阅读这个知识点 [知识分享：向编程爱好者推荐《The Little Schemer》](https://github.com/pimgeek/we-learn/issues/12)

