import sublime
import sublime_plugin
import os
import subprocess
import string


class RDocsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]

        params_reg = self.view.find('(?<=\().*(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = params_txt.split(',')

        snippet = "#'<brief desc>\n#'\n#'<full description>\n"

        for p in params:
            snippet += "#' @param %s <what param does>\n" % p

        snippet += "#' @export\n #' @keywords\n#' @seealso\n#' @return\n#' @alias\n#' @examples \dontrun{\n#'\n#'}\n"

        self.view.insert(edit, sel.begin(), snippet)


class SendSelectionCommand(sublime_plugin.TextCommand):
    @staticmethod
    def cleanString(str):
        str = string.replace(str, '\\', '\\\\')
        str = string.replace(str, '"', '\\"')
        return str

    def run(self, edit):
        # get selection
        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region) + "\n"
        selection = (selection[::-1].replace('\n'[::-1], '', 1))[::-1]

        # only proceed if selection is not empty
        if(selection == ""):
            return

        # get name of syntax file
        lang = self.view.settings().get('syntax')

        # R file
        if "R.tmLanguage" in lang:
            # split selection into lines
            selection = self.cleanString(selection).split("\n")
            # define osascript arguments
            args = ['osascript']
            # add code lines to list of arguments
            for part in selection:
                args.extend(['-e', 'tell app "R64" to cmd "' + part + '"\n'])
            # execute code
            subprocess.Popen(args)
