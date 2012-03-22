# Rtools for Sublime Text 2
This package provides a couple of useful tools for people using [Sublime Text 2](http://www.sublimetext.com/) to code in `R`. It has the key bindings to send a selection of code to R, and can also generate [Roxygen documentation](http://cran.r-project.org/package=roxygen2
) templates for any function quickly (select first line of a function till the first `{`, press keybinding and it will generate a template with `@params` from the function definition).

I plan to add functionality of [formatR](http://cran.r-project.org/package=formatR
) so you format/tidy code inline to the next version. Please suggest other feature requests here.

To install, just clone this repo into your `Sublime Text 2/packages` directory

```
git clone git@github.com:karthikram/Rtools.git
```

Once this becomes approved in package control, you should just be able to do it from the command palette (open command palette, type in Install Pacakges, and once list is populated look for Rtools)

## Customization

1. Since I am on OSX and use R64.app, I have set it up that way. If you prefer to use 32-bit R, replace `R64` with `R` in the `Rtools.py` file. In windows (untested), you should set it to the `.exe` file you wish to use.

2. I have included a basic roxygen template to populate the section above each file. If you prefer to have additional or fewer fields, I will make that as a setting in a future version. For you you can edit `Rtools.py` or post it as an issue and I will update it.

## Key bindings

To preserve or change these key bindings, copy them to your user file.


