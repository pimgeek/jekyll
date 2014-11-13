# coding: utf-8

import sublime, sublime_plugin, os, glob, re, fileinput

class GetWikiItemsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    global files, names, item_folder
    global e
    e = edit

    files = []
    names = []

    # 检查当前文档，如果是 markdown 才继续
    current_file_name = self.view.file_name()
    if current_file_name == None:
      return

    if not re.search(r'\.markdown', current_file_name):
      return

    # 获取工作目录
    work_folder = sublime.active_window().folders()[0]
    item_folder = work_folder + "/_miniwiki"

    # 遍历获取所有 markdown 文件
    self.find_markdown(item_folder)
    sublime.active_window().show_quick_panel(names, self.insert_link)

  def find_markdown(self, path):
    dirs = []
    for _file in glob.glob(path + "/*"):
      if os.path.isdir(_file):
        dirs.append(_file)
      else:
        files.append(_file)
        name = _file.replace(item_folder + "\\", "")
        names.append(name)

    for _dir in dirs:
      self.find_markdown(_dir)

  def insert_link(self, index):
    if index == -1:
      return

    name = names[index].split('.markdown')[0]
    
    # 获取当前输入位置
    point = self.view.sel()[0].end()
    _name = name.split("\\")[-1]
    
    permalink = self.get_item_of(files[index])
    if permalink:
      self.view.insert(e, point, "["+ _name +"](" + permalink + ")")


  def get_item_of(self, f):
    for line in open(f).readlines():
      m = re.match(r'^permalink:(\ )*(.+)', line)
      if m:
        return m.group(2)

    return None