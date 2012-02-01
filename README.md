# Easily add roxygen2 documentation 

I currently use ``Sublime Text 2` as my primary code editor for R.
To create roxygen documentation for any function, just select the first line of the function definition, press a keyboard shortcut, and voila!

## Installation

copy Roxygen.py to the User folder (typically found at `~/Library/Application Support/Sublime Text 2/Packages`)
Next, click `Preferences` > `Key Bindings - User` and paste the snippet below.

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
Change the keyboard shortcut to whatever you like.
done!

## Usage

Select the first line of of a R function definition (e..g `test<- function(x)`), press shortcut and it will generate the following template. Both the template and shortcut can be easily customized to your needs (just see the script and edit accordingly).

<pre>
#' <brief desc>
#` 
#' <full description>
#' @param x <what param does>
#` @keywords 
#` @seealso 
#` @return
#` @alias
#` @export 
#` @examples
#`
</pre>

