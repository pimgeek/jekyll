# coding: utf-8
import sublime, sublime_plugin, time, os
from os import path

class NewWikiItemCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.INPUT_PANEL_TITLE = u"添加新的wiki条目: "
    self.window.show_input_panel(self.INPUT_PANEL_TITLE, "", self.new_item, None, None)


  def new_item(self, item_name):
    self.window.run_command("open_wiki_item", {"item_name": item_name})
