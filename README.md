# ha-volumio-pandora-plugin

## Scripts for Home Assistant to control the Volumio Pandora Plugin

These are basic YAML configuration files for Home Assistant to attempt to control the Volumio Pandora plugin with Google Assistant and an Input Select entity.

<b>It's not bug free</b> -- it's still alpha at this point.  An earlier version was working, but not smoothly, a few months ago.  These new files are a partial rewrite of that configuration.

Give it a shot and file an issue if you see something wrong or you have a suggestion.  I can't promise the world but I'll try to implement reasonable changes.

### NOTES:

* At this time, you will need to install the `pyscript` addon.  You can find instructions at https://github.com/custom-components/pyscript  This is just for one script to populate the `input_select` and I may find a solutions without needed dependencies.

* You need to change the path of the Python script in the `bin` directory to match your configuration.  Unfortunately, that has to be hard coded and won't take a relative path, like `/config/script.py`.  Oh well.  I'll try to come up with a solution.

* I named the thing `hornet` but you will probably want to call it something else. It goes back to Pandora and the translations (she kicked a hornet's nest).  So call it Fred if you want, who cares. :D

