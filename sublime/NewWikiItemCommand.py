# coding: utf-8
import sublime, sublime_plugin, time, os
from sublime import active_window
from os import path

class NewWikiItemCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.wiki_dir = path.join(sublime.active_window().folders()[0], "_miniwiki")

    if not path.exists(self.wiki_dir):
      return sublime.error_message("wiki条目文件夹不存在！")

    active_window().show_input_panel("添加新的wiki条目", "", self.new_item, None, None)

  def generate_permalink(self):
    return "%i.html" % (round(time.time()))
  
  def item_header(self, item_name):
    return ("---\n"
            "layout: post\n"
            "title: %s\n"
            "permalink: %s\n"
            "---\n"
           ) % (item_name, self.generate_permalink())
  
  def new_item(self, item_name):
    file_name = path.join(self.wiki_dir, "%s.markdown" % item_name)
  
    if os.path.isfile(file_name):
      return sublime.error_message("文件已存在！")

    file = open(file_name, "w")
    
    file.write(self.item_header(item_name))
    file.close()
    
    active_window().open_file(file_name)
  
