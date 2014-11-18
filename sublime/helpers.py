import os, sublime
from os import path

def is_wiki_item():
  window      = sublime.active_window()
  view        = window.active_view()
  working_dir = window.folders()[0]
  wiki_dir    = path.join(working_dir, "_miniwiki")
  file_dir    = path.dirname(view.file_name())
  _, extname  = path.splitext(view.file_name())

  return (file_dir == wiki_dir) and (extname == ".markdown")
