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

        snippet += "#' @export\n#' @keywords\n#' @seealso\n#' @return\n#' @alias\n#' @examples \dontrun{\n#'\n#'}\n"

        self.view.insert(edit, sel.begin(), snippet)


class SendSelectionCommand(sublime_plugin.TextCommand):
    @staticmethod
    def cleanString(str):
        str = string.replace(str, '\\', '\\\\')
        str = string.replace(str, '"', '\\"')
        return str

    def run(self, edit):
        # Check if it's an R file
        filescope = self.view.syntax_name(self.view.sel()[0].b)
        if ("source.r " not in filescope) and ("source.r." not in filescope):
            return

        # get selection
        selection = ""
        for region in self.view.sel():
            if region.empty():
                selection += self.view.substr(self.view.line(region)) + "\n"
                self.advanceCursor(region)
            else:
                selection += self.view.substr(region) + "\n"

        selection = (selection[::-1].replace('\n'[::-1], '', 1))[::-1]

        # only proceed if selection is not empty
        if(selection == ""):
            return

        # split selection into lines
        selection = self.cleanString(selection).split("\n")
        # define osascript arguments
        args = ['osascript']
        # add code lines to list of arguments
        for part in selection:
            args.extend(['-e', 'tell app "R64" to cmd "' + part + '"\n'])
        # execute code
        subprocess.Popen(args)


    def advanceCursor(self, region):
        (row, col) = self.view.rowcol(region.begin())

        # Make sure not to go past end of next line
        nextline = self.view.line(self.view.text_point(row + 1, 0))
        if nextline.size() < col:
            loc = self.view.text_point(row + 1, nextline.size())
        else:
            loc = self.view.text_point(row + 1, col)

        # Remove the old region and add the new one
        self.view.sel().subtract(region)
        self.view.sel().add(sublime.Region(loc, loc))
