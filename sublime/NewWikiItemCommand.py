# coding: utf-8

import sublime, sublime_plugin, time, os
from os import path

class NewWikiItemCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.LABEL = u'添加新的 wiki 条目: '
    self.window.show_input_panel(self.LABEL, '', self.new_item, None, None)


  def new_item(self, item_name):
    self.window.run_command('open_wiki_item', {'item_name': item_name})