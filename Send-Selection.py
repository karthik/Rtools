import sublime, sublime_plugin
import os, subprocess, string

class SendSelectionCommand(sublime_plugin.TextCommand):
   @staticmethod
   def cleanString(str):
      str=string.replace(str,'\\','\\\\')
      str=string.replace(str,'"','\\"')
      return str

   def run(self, edit):
      # get selection
      selection = ""
      for region in self.view.sel():
         selection+=self.view.substr(region) + "\n"
      selection = (selection[::-1].replace('\n'[::-1], '', 1))[::-1]

      # only proceed if selection is not empty
      if(selection!=""):
         extension = os.path.splitext(self.view.file_name())[1]

         # R file
         if(extension.lower()==".r"):
            # define list of arguments
            args=['osascript','-e','tell app "R64" to activate']
            # split selection into lines
            selection=self.cleanString(selection).split("\n")
            # add code lines to list of arguments
            for part in selection:
               args.extend(['-e', 'tell app "R64" to cmd "' + part + '"\n'])
            # execute code and activate ST2
            p = subprocess.Popen(args)
            subprocess.Popen("""osascript -e 'tell app "Sublime Text 2" to activate' """, shell=True)