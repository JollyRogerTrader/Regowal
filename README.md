# Regowal

Regowal is a theme generator for Regolith-linux
https://regolith-linux.org/ /// https://github.com/regolith-linux

Dependancies include <code>python 3.7</code> and <code>imagemagick</code>

<code>
sudo apt install git imagemagick
cd ~/Documents
git clone https://github.com/JollyRogerTrader/Regowal.git
cd Regowal
python3 setup.py
./regowal <full path to img>
</code>

Regowal setup will create a directory ~/Regowal and point your ~/.Xresources-regolith to it.

Once setup.py is complete use regowal + image to set up a theme. Regowal will copy your image to the them folder for safe keeping.

<code>./regowal <full path to img></code>

Sometimes a manual <code>regolith-look refresh</code> is needed to fully update the wallpaper

The theme can be reset to the default Regolith-linux theme with
<code>regolith-look set cahuella && regolith-look refresh</code>

currently Regowal is only updating i3 colors. Rofi + GTK colors are in progress. If your ~/.Xresources-regolith has additional settings then ensure you have a backup prior to running <code>python3 setup.py</code> this script is still in development and something might break. you can backup your .Xresources-regolith file with <code>cp ~/.Xresources-regolith .Xresources-regolith.bk</code>

![Regowal example1](Desktop.png)
![Regowal example2](Desktop1.png)
![Regowal example3](Desktop2.png)
![Regowal example4](Desktop3.png)
