# Regowal

Regowal is a theme generator for Regolith-linux
https://regolith-linux.org/ /// https://github.com/regolith-linux

Dependancies include <code>python 3.7</code> and <code>imagemagick</code> and of course Regolith-Linux v1.3 or higher (v1.4 support with gnome-terminal soon)

Regowal setup will create a hidden directory at ~/.regowal and point your ~/.Xresources-regolith to it.

Once setup.py is complete use regowal + image to set up a theme. Regowal will copy your image to the hidden theme folder for safe keeping.

Sometimes a manual <code>regolith-look refresh</code> is needed to fully update the wallpaper but Regowal tries at the end anyway.

<bold>HOW TO INSTALL</bold>

<code>sudo apt install git imagemagick</code>

<code>cd ~/Documents</code>

<code>git clone https://github.com/JollyRogerTrader/Regowal.git</code>

<code>cd Regowal</code>

<code>python3 setup.py</code>

<bold>HOW TO USE</bold>

<code>regowal (-light -alt) "full path to img"</code>
<weak>-light is for light mode </weak>>
<weak>-alt is to force alternate color generation (works better for black and white or lower color range images)
</weak>
note: you do not need to run setup.py more than once or run it if you deleted the .regowal theme from your home directory and would like to reinstall.

<bold>HOW TO SWAP TO DEFUALT THEME</bold>

<code>regolith-look set cahuella && regolith-look refresh</code> OR <code>rm ~/.Xresources-regolith</code> -Regolith with look back at your default themes folder thats in /etc/regolith/styles

currently Regowal is only updating i3 and Rofi colors. GTK color theming is a work in progress. If your ~/.Xresources-regolith has additional settings then ensure you have a backup prior to running <code>python3 setup.py</code> this script is still in development and something might break. you can backup your .Xresources-regolith file with <code>cp ~/.Xresources-regolith .Xresources-regolith.bk</code>

![Regowal example1](Desktop.png)
![Regowal example2](Desktop1.png)
![Regowal example3](Desktop2.png)
![Regowal example4](Desktop3.png)
