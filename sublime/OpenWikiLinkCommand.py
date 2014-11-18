# coding: utf-8
import sublime, sublime_plugin, re

class Pattern:
  def __init__(self, view):
    self.view        = view
    self.word_region = self.view.word(self.view.sel()[0].a)
    delimeter        = self.delimeter()

    if delimeter == ")":
      self.word_region = self.view.word(self.delimeter_region.a - 5)
      delimeter        = self.delimeter()

    self.regex = {
      "]": "\[(%s)\]\(\w+\.html\)" % self.word,
      ".": "\[(\w+)\]\(%s\.html\)" % self.word,
    }.get(delimeter, None)

  def delimeter(self):
    self.delimeter_region = sublime.Region(self.word_region.b, self.word_region.b + 1)
    self.word             = self.view.substr(self.word_region)
    return self.view.substr(self.delimeter_region)

class OpenWikiLinkCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    match = re.search("/_miniwiki/\w+.markdown", self.view.file_name())

    if not match: return

    pattern = Pattern(self.view)

    if not pattern.regex: return

    line_region = self.view.line(pattern.word_region)
    line        = self.view.substr(line_region)
    line_match  = re.search(pattern.regex, line)

    if not line_match: return

    self.view.window().run_command("open_wiki_item", {"item_name": line_match.group(1)})

