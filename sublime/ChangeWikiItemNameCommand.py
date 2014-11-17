# coding: utf-8

import sublime, sublime_plugin, os, re

class ChangeWikiItemNameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # 获取工作目录
    work_folder         = sublime.active_window().folders()[0]
    wiki_item_folder    = os.path.join(work_folder, "_miniwiki")
    current_file_folder = os.path.dirname(self.view.file_name())

    current_file_base_name = self.get_file_base_name(self.view.file_name())
    current_file_extname   = self.get_file_extname(self.view.file_name())

    if wiki_item_folder != current_file_folder:
      return
    if current_file_extname != ".markdown":
      return

    sublime.active_window().show_input_panel("change current wiki markdown file name", current_file_base_name, self.change_wiki_item_name, None, None)

  def change_wiki_item_name(self, text):
    current_file_base_name = self.get_file_base_name(self.view.file_name())
    if text == current_file_base_name:
      return
    if text in self.get_wiki_file_base_names():
      return

    current_file_folder = os.path.dirname(self.view.file_name())
    new_file_name = "%s.markdown" % text
    new_file_path = os.path.join(current_file_folder, new_file_name)

    old_file_base_name = self.get_file_base_name(self.view.file_name())
    new_file_base_name = self.get_file_base_name(new_file_path)

    # 修改 文件头的 title
    file_text = open(self.view.file_name(), 'r').read().decode("utf-8")
    search_re = r'(---(?:\s|.)*)(title:\s*.*)((?:\s|.)*---)'
    replace_re = r'\1title: %s\3' % new_file_base_name
    new_file_text = re.sub(search_re, replace_re, file_text, 1)
    file = open(self.view.file_name(),"w")
    file.write(new_file_text.encode('utf-8'))
    file.close()

    # 获取 链接名
    search_re = r'---(?:\s|.)*permalink:\s*(.*)(?:\s|.)*---'
    link_name = re.match(search_re, file_text).group(1)

    # 修改 [你好](3.html) 这样的引用
    for f in os.listdir(current_file_folder):
      wiki_file = os.path.join(current_file_folder, f)
      extname = os.path.splitext(wiki_file)[1]
      if extname != ".markdown":
          continue
      file_text = open(wiki_file, 'r').read().decode("utf-8")

      search_re = r'(\[[^\]]*\])(\(%s\))' % link_name
      replace_re = r'[%s]\2' % new_file_base_name
      new_file_text = re.sub(search_re, replace_re, file_text, 0)
      file = open(wiki_file,"w")
      file.write(new_file_text.encode('utf-8'))
      file.close()

    # 修改文件名
    os.rename(self.view.file_name(), new_file_path)
    sublime.active_window().run_command('close')
    sublime.active_window().open_file(new_file_path)

  # file_path => "/a/b/c/abcd.markdown"
  # return abcd
  def get_file_base_name(self, file_path):
    file_name = os.path.split(file_path)[1]
    return os.path.splitext(file_name)[0]

  def get_file_extname(self, file_path):
    file_name = os.path.split(file_path)[1]
    return os.path.splitext(file_name)[1]    

  def get_wiki_file_base_names(self):
    work_folder         = sublime.active_window().folders()[0]
    wiki_item_folder    = os.path.join(work_folder, "_miniwiki")

    base_names = []
    for f in os.listdir(wiki_item_folder):
      base_name = os.path.splitext(f)[0]
      base_names.append(base_name)
    return base_names
