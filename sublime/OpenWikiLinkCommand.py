# coding: utf-8
import sublime, sublime_plugin, re

class OpenWikiLinkCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    match = re.search("/_miniwiki/\w+.markdown", self.view.file_name())

    if not match: return

    word_region = self.view.word(self.view.sel()[0].a)
    word        = self.view.substr(word_region)

    delimeter_region = sublime.Region(word_region.b, word_region.b + 1)
    delimeter        = self.view.substr(delimeter_region)

    pattern = self.pattern_from(delimeter, word)

    if not pattern: return

    line_region = self.view.line(word_region)
    line        = self.view.substr(line_region)
    match       = re.search(pattern, line)

    if not match: return

    self.view.window().run_command("open_wiki_item", {"item_name": match.group(1)})

  def pattern_from(self, delimeter, word):
    return {
      "]": "\[(%s)\]\(\w+\.html\)" % word,
      ".": "\[(\w+)\]\(%s\.html\)" % word,
      ")": "\[(\w+)\]\(\w+\.html\)",
    }[delimeter]
