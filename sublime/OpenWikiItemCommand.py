# coding: utf-8
import sublime, sublime_plugin, time
from os import path, makedirs

class OpenWikiItemCommand(sublime_plugin.WindowCommand):
  def run(self, **args):
    item_name = args.get("item_name", None)

    if not item_name: return

    self.wiki_dir = path.join(self.window.folders()[0], "_miniwiki")

    if not path.exists(self.wiki_dir): makedirs(self.wiki_dir)

    self.create_or_open(item_name)


  def create_or_open(self, item_name):
    file_name = path.join(self.wiki_dir, "%s.markdown" % item_name)

    if path.isfile(file_name):
      return self.window.open_file(file_name)

    file = open(file_name, "w")
    
    file.write(self.item_header(item_name).encode('utf-8'))
    file.close()
    
    self.window.open_file(file_name)


  def generate_permalink(self):
    return "%i.html" % (round(time.time()))

  
  def item_header(self, item_name):
    return ("---\n"
            "layout: post\n"
            "title: %s\n"
            "permalink: %s\n"
            "---\n"
           ) % (item_name, self.generate_permalink())