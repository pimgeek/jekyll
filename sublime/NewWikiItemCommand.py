# coding: utf-8
import sublime, sublime_plugin, time, os
from sublime import active_window
from os import path

class NewWikiItemCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.WIKI_DIR            = path.join(sublime.active_window().folders()[0], "_miniwiki")
    self.WIKI_DIR_NOT_EXISTS = u"wiki条目文件夹不存在！"
    self.seINPUT_PANEL_TITLE = u"添加新的wiki条目: "
    self.ITEM_EXISTS         = u"文件已存在！"

    if not path.exists(self.WIKI_DIR):
      return sublime.error_message(self.WIKI_DIR_NOT_EXISTS)

    active_window().show_input_panel(self.INPUT_PANEL_TITLE, "", self.new_item, None, None)

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
    file_name = path.join(self.WIKI_DIR, "%s.markdown" % item_name)
  
    if os.path.isfile(file_name):
      active_window().open_file(file_name)
      return sublime.error_message(self.ITEM_EXISTS)

    file = open(file_name, "w")
    
    file.write(self.item_header(item_name).encode('utf-8'))
    file.close()
    
    active_window().open_file(file_name)
  
