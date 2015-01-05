---
layout: post
title: ACT-R 建模语言基本用法 Cheatsheet
permalink: 1419948120.html
tag: 认知科学, cheatsheet
date: 2014/12/31
---

## 运行环境相关

```(clear-all)``` 清除 ACT-R 运行环境中的所有模型

## 模型定义相关

```(define-model model-name ...)``` 在当前运行环境中定义一个认知模型
```(sgp :key1 value1 :key2 value2 ...)``` 设置当前认知模型的各项参数
```:v <t|path>``` 将模型输出打印到什么地方，t 为标准输出，path 为文件