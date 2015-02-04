---
layout: post
title: 文章翻译：开始使用 Sass 和 Compass
permalink: 1421032360.html
date: 2014/01/01
---

原文地址  - http://thesassway.com/beginner/getting-started-with-sass-and-compass

开始使用 Sass 和 Compass
=====================================

看起来，你的朋友，同事，网上好友或某些别的人已经向你讲过关于 Sass 或 Compass 的事了 … 甚至是两样东西同时讲的。很好！但接下来该做些什么？在这篇针对初学者的入门指南中，我们将引导你完成上手使用 Sass 和 Compass 的头几步。具体说来，我们将助你完成工具安装，测试项目创建，编译第一段 Sass 与 Compass 代码等任务，甚至稍稍 "混杂" 一些 Sass 的历史。

安装 Sass 和 Compass
------------------------

Sass 和 Compass 是通过 Ruby gem 的方式安装的，所以，你首先需要在自己的机器上安装 Ruby。

如果你在 Windows 系统中，可以运行 [Ruby Installer](http://rubyinstaller.org/)。如果你在 Linux 系统中，那么 [Rails Ready](https://github.com/joshfng/railsready) 为你提供了许多 Ruby 的基本组件。如果你在 OS X 中，那么默认情况下 Ruby 应该已经安装好了，直接使用就 OK。

让 Ruby 正常工作并不在本文的主要讨论范围内。所以，如果你碰到了任何障碍，请访问 [Sass 相关的邮件列表](http://groups.google.com/group/sass-lang)，找到对路的资源，让 Ruby 在你的机器上正常工作。

### 安装 Sass

OK，让我们开始安装 Sass 吧！首先打开你的命令控制台 / 虚拟终端 (比如 [Terminal.app](http://en.wikipedia.org/wiki/Apple_Terminal)) 并敲入以下命令：

#### Windows:

```
gem install compass
```

#### Linux / OS X:

```
sudo gem install compass
```

对于 Linux 和 OS X 的朋友而言，是否要以 `sudo` 用户安装 gem 取决于你的具体情况。比如说，如果你正在使用 [RVM](https://rvm.io/)，就不需要以 `sudo` 用户安装 gem。

OK，我了解你在想什么。先前说过我们要安装 Sass，但从前面的命令行看来，我们实际上在安装 Compass。为什么呢？情况是这样：Compass 依赖于 Sass （译者注：所以会自动安装 Sass），在运行这条命令时，你将会看到类似于下面的屏幕显示：

```
$ sudo gem install compass
Fetching: sass-3.1.3.gem (100%)
Fetching: compass-0.11.3.gem (100%)
Successfully installed sass-3.1.3
Successfully installed chunky_png-1.2.0
Successfully installed fssm-0.2.7
Successfully installed compass-0.11.3
4 gems installed
```

如果运行命令之后，你看到的不是类似上面这样的输出，那么你机器上的 Ruby 或者 Ruby Gems 可能并没有正确安装。有关安装问题的过多细节在这里不便展开，不然就会超出本文的讨论范围。总之，遇到这种问题，还是建议你去 [Sass 相关的邮件列表](http://groups.google.com/group/sass-lang) 寻求帮助。

如果你感觉自己被 [命令行操作](http://en.wikipedia.org/wiki/Command-line_interface) 给吓住了，不必紧张。[John Long](http://twitter.com/johnwlong) 写过一篇非常棒的入门文章，标题是：["写给设计师的 OS X 命令行提示符操作入门"](http://wiseheartdesign.com/articles/2010/11/12/the-designers-guide-to-the-osx-command-prompt/)，这篇文章将帮你跟上本文的节奏。

作为参考，我还在下面列出了两款专门针对 Sass / Compass 的基于图形界面的 App。但在这篇入门文章中，我们将假设你正在使用命令行方式进行操作。

* [Scout](http://mhs.github.com/scout-app/) (跨平台) 由 [Mutually Human](http://mutuallyhuman.com/) 开发
* [Compass.app](http://compass.handlino.com/) (Windows/Linux/Mac OS X) 由 Handlino 开发.


### CSS Parser (译者注：CSS 解析器)

我还愿意安装 [css_parser](http://rubygems.org/gems/css_parser) 以便充分利用其 `compass stats` 的所有功能：输出关于我的 Sass 样式表的各种统计数据。具体说来，它将会输出一个报告，其中包括 Sass 的规则、属性、mixin 定义以及 CSS 规则与属性的条数。

> It outputs a report that gives a count of the Sass rules, properties, mixins defined and mixins used as well as the CSS rules and properties that get output from your Sass-stylesheets. (这句话需要咨询 @ben7th 才能正常译出)

运行以下命令即可安装 `css_parser`

```
gem install css_parser
```

现在，准备工作已经就绪，你可以开始一些实质性的 Sass 和 Compass 行动了！

创建一个测试项目
---------------------

开始学习某种新事物的最佳方法，就是直接投入到具体操作中去。话说到此，现在就定位到你平时存放开发代码的位置吧（或者你打算存放这个测试项目的具体位置），然后运行下面这条命令：

```
compass create sass-test
```

另一种可选方案是，直接用下面的命令从 GitHub 上的 [the test project](https://github.com/thesassway/sass-test) 项目直接抓取源码目录到自己选定的存储位置：

```
git clone https://github.com/thesassway/sass-test.git
```

但我们不建议你这样做，不然就会完全破坏我们的学习目的——如何自行完成整个操作过程。

OK，让我们继续前进。利用 ([cd](http://en.wikipedia.org/wiki/Cd_(command))) 命令，把当前所在位置改变到最新创建的 `/sass-test` 目录下方，然后用你最喜欢的编辑器打开它。我使用 [TextMate](http://macromates.com/)，但我一直在考虑试一试 [Vim](http://www.vim.org/) 或 [Sublime Text 2](http://www.sublimetext.com/2)。我们在 Changelog 网站上对 Vim 编辑器做了大量介绍，所以如果你对 Vim 感兴趣，可以看一眼 [Changelog 站内关于 Vim 的网页搜索结果](http://search.aol.com/aol/search?s_it=topsearchbox.nrf&v_t=na&q=vim+site%3Athechangelog.com) 以便深入研究。

把 Sass 编译为 CSS
-------------------

这是最简单的部分。所有艰难的工作都由 Sass 和 Compass 来完成，你只要运行下面的命令，让 Compass 做它该做的事就可以了。

```
compass watch
```

如果前面的准备工作都没问题，你应当看到类似于下面这样的屏幕显示：

```
$ sass-test git:(master) compass watch
FSSM -> An optimized backend is available for this platform!
FSSM ->     gem install rb-fsevent
>>> Compass is polling for changes. Press Ctrl-C to Stop.
```

如果这就是你屏幕上实际显示的内容，那么你可以大喊一声“耶”来祝贺自己了。因为现在各项准备都以就绪，你可以开始用 Sass 的方式编写 CSS 啦！

`compass watch` 这条命令所做的事情，正是你预想的那样——它会监测你的 Sass 文件内容变化（只监测文件被保存之后的内容变化）并把你的 Sass 代码自动编译为 CSS。那么，它怎么知道你的 Sass 代码在什么位置？又怎么知道编译生成的 CSS 文件又该放在哪里呢？这问题问得很好，未来我们将在另一篇标题为《配置 Compass》文章中详细讨论。

与此同时，让我们看看位于 `sass-test` 项目根目录下的 `config.rb` 文件（译者注：可参考 [config.rb](https://github.com/thesassway/sass-test/blob/master/config.rb)）。这就是 [Compass 的配置文件](http://compass-style.org/help/tutorials/configuration-reference/)，基本上可以把它看做 Compass 的大脑，其中定义了一系列的变量名。有了这些变量，Compass 才能知道你的 Sass，CSS，图片文件以及 JavaScript 文件都放在什么位置，需要调用哪些扩展组件，你所偏好的语法格式和输出格式是什么样的等等，不一而足。

写一些 Sass 代码
---------------

在我们真正动手写 Sass 代码之前，了解一些关于它的历史是很重要的。事实上，关于 Sass 最难理解的就是它有两套 [语法](http://en.wikipedia.org/wiki/Syntax) ——初学 Sass 的朋友们通常会为此感到困惑或者畏惧，甚至碰上这种情况就打消了继续尝试的念头。为什么我了解这一点？因为我自己就曾忍痛啃过这块众所周知的硬骨头，我当时的感受与这些人如出一辙。但现在为了避免偏题，我们还是言归正传吧。

Sass 就像 CSS 一样。好吧，这么说有点误导。Sass **在某些方面可以像** CSS 一样。前文提到过，Sass 有一些历史，它曾有过不止一套语法。其中的一套语法甚至也叫做 “Sass”，这就更叫人困惑了。现在我澄清一下，主要的一套语法被称作 “SCSS”（这个缩写表示 “Sassy CSS”），它是在 Sass 3 推出后开始使用的新语法。而早一些的语法（我曾提到的那段历史的一部分）被称作 **缩进式语法**（或者简称 “Sass”）。 -- 此处需要 @ben7th 确认.

既然我们已经简要介绍了 Sass 的历史，也说明了它有两套语法的事实，那么接下来我相信你已经做好写 Sass 代码的准备了。其实，我应该说 SCSS ——因为 SCSS 与 CSS 很相似，它的语法是作为 CSS3 样式表的语法扩展而被设计出来的。这意味着每个合法的 CSS3 样式表同时也是一个合法的 SCSS 样式表。实际上，你可以把某个 CSS 文件的内容复制粘贴到一个 SCSS 文件中，经过编译之后，仍然能够得到干净的 CSS。

下面让我们测试一下上述“理论”，把我们的博客网站正在使用的 [css 文件](http://thesassway.com/css/master.css) 复制粘贴到我们的测试项目中的 `sass-test/sass/screen.scss` 文件内（译者注：可参考 [screen.scss](https://github.com/thesassway/sass-test/blob/scss-is-like-css/sass/screen.scss)），保存后运行 `compass compile` 命令。此后，再仔细看一看 `sass-test/stylesheets/screen.css` 这个文件（译者注：可参考 [screen.css](https://github.com/thesassway/sass-test/blob/scss-is-like-css/stylesheets/screen.css)），就会发现 Sass 与 Compass 已经把经过压缩的不可读的 CSS 内容编译过了，形成了一份可读的，完美地缩进过的 CSS 文件。而且，还伴随着原始代码文件中包含的用于排除故障而写的代码注释。

结论和接下来的步骤
-------------------------

很显然，这里给出的例子并不是最实用的，而且严格说来我们根本没写任何代码。我想通过这个例子证明的是：从编写 CSS 代码转换到编写 Sass 代码，在某些情况下可以说几乎是零成本的，因为你刚才就已经亲自实现了这种转换。

接下来的步骤就是充分了解  [Sass](http://sass-lang.com/tutorial.html#features) 和 [Compass](http://compass-style.org/) 的各种特性，在需要的时候选择其中的一部分为自己所用。这是转换到 Sass 的最有利的一点——你可以循序渐进地触及 Sass 和 Compass 为你提供的诸多好处，而不必抱有畏难情绪，担心你需要花上“个把星期”才能学会它……

开始行动吧，现在立刻开始。