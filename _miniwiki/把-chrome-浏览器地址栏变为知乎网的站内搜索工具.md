---
layout: post
title: 把-chrome-浏览器地址栏变为知乎网的站内搜索工具
permalink: 1421029618.html
date: 2014/05/28
---


我最近发现一个 chrome 浏览器的 URL 地址栏使用小技巧.

![image](https://cloud.githubusercontent.com/assets/1609306/3100132/7a51eb58-e610-11e3-9998-012d3d75191c.png)

![image](https://cloud.githubusercontent.com/assets/1609306/3100128/6c6c965a-e610-11e3-84dc-2c4dbbf0bc09.png)

其实不仅可以输入 zhihu.com ，还可以输入其它网站的域名，实现类似的效果，比如：

* 输入 github.com 并敲空格, 可以直接搜索 github 站内的资源
* 输入 stackexchange.com 并敲空格, 可以直接搜索 stackexchange 站内的资源.

但是并非所有网站都可以这样做，比如输入 stackoverflow.com 敲空格 就没有效果。

这背后的技术原理是什么呢？请参考 [技术资料：opensearch](https://github.com/mindpin/tech-exp/issues/20)
