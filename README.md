# Regowal

Regowal is a theme generator for Regolith-linux

Regowal setup will create a directory in your home folder and point .Xresources-regolith to it.
To run setup, navigate to the directory where setup is in a terminal type
<code>python3 setup.py</code>

Once setup.py is complete use regowal + image to set up a theme
<code>./regowal <full path to img></code>

Sometimes a manual <code>regolith-look refresh</code> is needed to fully update the wallpaper

The theme can be reset to the default with
<code>regolith-look set cahuella && regolith-look refresh</code>

currently Regowal is only updating i3 colors. Rofi + GTK colors are in progress.
