import sublime, sublime_plugin

class RDocsCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sel = self.view.sel()[0]

      params_reg = self.view.find('(?<=\().*(?=\))', sel.begin())
      params_txt = self.view.substr(params_reg)
      params = params_txt.split(',')

      snippet = "#`<brief desc>\n#`\n#`<full description>\n"

      for p in params:
         snippet += "#`@param %s <what param does>\n" % p

      snippet+= "#`@keywords\n#`@seealso\n#`@return\n#`@alias\n#`@export\n#`@examples \dontrun{\n#`\n#` }"

      self.view.insert(edit, sel.begin(), snippet)