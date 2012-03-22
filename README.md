To install, just clone this repo into your sublime text 2/packages directory
```
git clone git://github.com/karthikram/Rtools
```
Once this becomes approved in package control, you should just be able to do it from the command palette (open command palette, type in Install Pacakges, and once list is populated look for Rtools)

# Customization

1. Since I am on OSX and use R64.app, I have set it up that way. If you prefer to use 32-bit R, replace `R64` with `R` in the `Rtools.py` file. In windows (untested), you should set it to the `.exe` file you wish to use.

2. I have included a basic roxygen template to populate the section above each file. If you prefer to have additional or fewer fields, I will make that as a setting in a future version. For you you can edit `Rtools.py` or post it as an issue and I will update it.

## Key bindings

To preserve or change these key bindings, copy them to your user file.


