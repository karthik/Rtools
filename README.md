# Using Sublime Text for coding in R
I use [Sublime Text 2](http://www.sublimetext.com/) as my primary code editor for `R`. It has now become my swiss knife for all scientific computing. Few key features that make it stand out are full-screen editing with a mini-map, distraction-free editing, and multi-select. In addition, ST2 has numerous packages such as integrated git (commit and push without leaving your editor), markdown preview, syntax highlighting, code formatting and it's easy to code up anything else you might need (like the ones below).

# Script 1:  Easily add roxygen2 documentation to any R script
This package will allow you to effortlessly document any `R` function using the `roxygen2` syntax. Simply select the first line of the function definition, press a keyboard shortcut, and voila!

### Installation

1. copy `Roxygen.py` to the your packages folder (typically found in `~/Library/Application Support/Sublime Text 2/Packages/User`)
2. Next, click `Preferences` > `Key Bindings - User` and paste the snippet below.

<pre>

 { "keys": ["super+shift+alt+r"], "command": "r_docs", "context":
      [
        { "key": "selection_empty", "operator": "equal", "operand": false, "match_all": true },
        {
        "operand": "source.r",
        "operator": "equal", 
        "match_all": true, 
        "key": "selector"
         }
      ]   
    }
</pre>
3. Change the keyboard shortcut to whatever you like. In this case `⌘ + alt + shift + R` (super in Sublime Text jargon means ⌘) 

### Usage

Select the first line of of a R function definition (e..g `test<- function(x)`), press shortcut and it will generate the following template. Both the template and shortcut can be easily customized to your needs (just see the script and edit accordingly). The script will automatically populate all of the function arguments into the documentation. You can customize `roxygen` tags by editing `Roxygen.py`

<hr>

<pre>
#'&lt;brief desc&gt;
#'
#'&lt;full description&gt;
#'@param x &lt;what param does&gt;
#'@keywords 
#'@seealso 
#'@return
#'@alias
#'@export 
#'@examples
#'test&lt;- function(x)
</pre>

# Script 2 - Send selection to R
A short script to send any selected r code to R.

### Installation
1. Copy `Send-Selection.py` to your user folder.
2. Add the following keybinding:

<pre>
{ "keys": ["super+enter"], "command": "send_selection" }
</pre> 
3. That's it. Note that I use R64.app for day-to-day use. If you use regular R.app, then change all instances of R64 to R in `Send-Selection.py`.

