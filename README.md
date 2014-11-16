jekyll-miniwiki
===============

基于 jekyll 扩展实现的一个小型 wiki 工具。同时包括了 sublime text 2 的专用插件。


功能特性
------------------

1. 以 markdown 文件的形式创建词条，以词条名称区分所有的词条，词条名称支持中文。
2. 支持在编辑过程中快速查找词条，并插入其他词条的链接。（需要 sublime text 2 环境）
3. 当词条名称修改时，自动修改所有针对该词条的链接。（需要 sublime text 2 环境）

另外还具有如下特性：

- 词条语法是 github 风格的 markdown 语法。会包含一些自定义的扩充。
- 本地预览时支持中文文件名


实现方式
------------------

所有的词条文件被放置在 _miniwiki 文件夹下。工程解析时会自动取得 _miniwiki 文件夹下的所有 .markdown 文件。简化起见，一开始不分子文件夹。


sublime 插件
-----------------

1. 输入一个标题，在当前工作 folder 的 `_miniwiki` 文件夹下创建带有指定头部模板内容的 .markdown 文件。指定的头部是：

  ```
  ---
  layout: post
  title: 输入的标题
  permalink: 自增 ID.html
  ---
  ```
  其中，自增ID根据工程下的 `_miniwiki/list` 计算得知
  
2. 获得 `_miniwiki` 下的 .markdown 文件清单，在一个列表中让用户选择，针对选定的条目，在当前编辑器内插入 `[标题](:permalink)` 这样的链接（已初步实现）

3. 在某个 .markdown 文件编辑时，按快捷键弹出一个UI，输入一个新标题来改名。改名后，当前 markdown 的文件名变为 新标题.markdown，头部信息中的 title 内容值变为 新标题。同时，搜索 _miniwiki 下所有条目，找到其中对应的链接，逐一修改文件内容。
