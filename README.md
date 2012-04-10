# Rtools for Sublime Text 2
This package provides a couple of useful tools for people using [Sublime Text 2](http://www.sublimetext.com/) to code in `R`. It has the key bindings to send a selection of code to R, and can also generate [Roxygen documentation](http://cran.r-project.org/package=roxygen2
) templates for any function quickly (select first line of a function till the first `{`, press keybinding and it will generate a template with `@params` from the function definition).

We plan to add functionality of [formatR](http://cran.r-project.org/package=formatR
) so you can format/tidy code inline to the next version. Please suggest other feature requests as issues (preferably tagged as a feature request).

# Installation

Installing via Package Control: The fastest way to install is via the command palette (open command palette, type in Install Packages, and once list is populated look for `R tools`)

If you don't have package control installed, the just clone this repo into your `Sublime Text 2/packages` directory

```
git clone git@github.com:karthikram/Rtools.git
```



## Customization

1. Since I am on OSX and use R64.app, I have set it up that way. If you prefer to use 32-bit R, replace `R64` with `R` in the `Rtools.py` file. In windows (untested), you should set it to the `R.exe` file you wish to use.

2. I have included a basic roxygen template to populate the section above each file. If you prefer to have fewer or more fields, I will move it to a settings file in a future version. For you you can edit `Rtools.py` or post it as an issue and I will update it.

## Key bindings

To preserve or change these key bindings, copy them to your `Key Bindings - User` file.
