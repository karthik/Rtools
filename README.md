# Easily add roxygen2 documentation to any R script

I primarily use [Sublime Text 2](http://www.sublimetext.com/) as my primary code editor for `R`.
This package will allow you to effortlessly document any `R` function using the `roxygen2` syntax. Simply select the first line of the function definition, press a keyboard shortcut, and voila!

## Installation

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
3. Change the keyboard shortcut to whatever you like. In this case `⌘ + alt + shift + R`

4. done!

## Usage

Select the first line of of a R function definition (e..g `test<- function(x)`), press shortcut and it will generate the following template. Both the template and shortcut can be easily customized to your needs (just see the script and edit accordingly).

<pre>
#` &lt;brief desc&gt;
#` 
#` &lt;full description&gt;
#` @param x &lt;what param does&gt;
#` @keywords 
#` @seealso 
#` @return
#` @alias
#` @export 
#` @examples
#`
test&lt;- function(x)
</pre>

