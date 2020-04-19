import subprocess, os, re

username = os.getlogin()

colorfiledata = """
#define color_base03   #2E3440
#define color_base02   #3B4252
#define color_base01   #434C5E
#define color_base00   #7B8394
#define color_base0    #D8DEE9
#define color_base1    #E5E9F0
#define color_base2    #ECEFF4
#define color_base3    #ECEFF4
#define color_yellow   #EBCB8B
#define color_orange   #D08770
#define color_red      #BF616A
#define color_magenta  #5E81AC
#define color_violet   #B48EAD
#define color_blue     #81A1C1
#define color_cyan     #88C0D0
#define color_green    #A3BE8C
"""
typefacefiledata = """
! Typeface: Source Code Pro
#define typeface_bar_glyph  Source Code Pro Medium 13
#define typeface_wm         Source Code Pro Medium 13
#define typeface_bar        pango:Source Code Pro Medium 13, Material Design Icons 13
#define typeface_rofi       Source Code Pro Medium 18
#define typeface_terminal   Source Code Pro:pixelsize=24:antialias=true:autohint=true

#define typeface_bar_glyph_wifi 
#define typeface_bar_glyph_wired 
#define typeface_bar_glyph_up 
#define typeface_bar_glyph_dn 
#define typeface_bar_glyph_cpu 
#define typeface_bar_glyph_battery_100 
#define typeface_bar_glyph_battery_80 
#define typeface_bar_glyph_battery_50 
#define typeface_bar_glyph_battery_20 
#define typeface_bar_glyph_battery_0 
#define typeface_bar_glyph_battery_charging 
#define typeface_bar_glyph_battery_ac 
#define typeface_bar_glyph_battery_unknown 
#define typeface_bar_glyph_time 
#define typeface_bar_glyph_workspace 

#define typeface_bar_glyph_media_playing 
#define typeface_bar_glyph_media_paused 

#define typeface_bar_glyph_notify_none 
#define typeface_bar_glyph_notify_some 
#define typeface_bar_glyph_notify_error 
#define typeface_bar_glyph_help 

#define typeface_bar_glyph_thermometer 
#define typeface_bar_glyph_sound 
#define typeface_bar_glyph_mute 

#define typeface_bar_glyph_memory 

#define typeface_bar_glyph_on 
#define typeface_bar_glyph_off 

#define typeface_bar_glyph_numlock 
#define typeface_bar_glyph_capslock 
"""
themefiledata = (
    """
#define gtk_theme           Adwaita
#define icon_theme          Paper
#define desktop_wallpaper   /usr/share/backgrounds/regolith-structure-7.png
#define rofi_theme          /home/"""
    + username
    + """/Regowal/styles/regowaltheme/rofi.rasi

#define i3wm_window_border_size         1
#define i3wm_floatingwindow_border_size 1
#define i3wm_gaps_inner_size            5
#define i3wm_gaps_outer_size            0
#define i3wm_bar_position         bottom
"""
)
rootfiledata = (
    """
! -- Styles - Colors
#include "/home/"""
    + username
    + """/Regowal/styles/regowaltheme/color"

! -- Styles - Fonts
#include "/home/"""
    + username
    + """/Regowal/styles/regowaltheme/typeface"

! -- Styles - Theme
#include "/home/"""
    + username
    + """/Regowal/styles/regowaltheme/theme"

! -- Applications
! These files map values defined above into specific app settings.
#include "/etc/regolith/styles/st-term"
#include "/etc/regolith/styles/i3-wm"
#include "/etc/regolith/styles/i3xrocks"
#include "/etc/regolith/styles/rofi"
#include "/etc/regolith/styles/gnome"
"""
)
rofifiledata = """
/* global settings and color variables */
* {
   blue:             #81A1C1;
   darkblue:         #5E81AC;
   cyan:             #8FBCBB;
   lightcyan:        #88C0D0;
   green:            #A3BE8C;
   red:              #BF616A;

   dark1:            #2E3440;
   dark2:            #3B4252;
   dark3:            #434C5E;
   dark4:            #4C566A;

   light1:           #D8DEE9;

   background-color: @dark1;
   border-color:     @dark2;
   text-color:       @dark3;
   dark-text-color:  @darkblue;
   main-color:       @blue;
   highlight:        @cyan;
   urgent-color:     @red;
   selected-color:   @lightcyan;
}

window {
   background-color: @background-color;
   width: 640px;
   padding: 10px;
   fullscreen: false;
   border:  2px;
   border-radius: 0px;
   border-color: @border-color;
}

mainbox {
   background-color: @background-color;
   spacing:0px;
}

message {
   padding: 6px 10px;
   background-color: @background-color;
}

textbox {
   text-color: @text-color;
   background-color:@background-color;
}

listview {
   fixed-height: true;
   dynamic: true;
   scrollbar: false;
   spacing: 0px;
   padding: 1px 0px 0px 0px;
   margin: 0px 0px 1px 0px;
   background: @background-color;
}

element {
   padding: 4px 10px;
}

element normal.normal {
   padding: 0px 15px;
   background-color: @background-color;
   text-color: @dark-text-color;
}

element normal.urgent {
   background-color: @background-color;
   text-color: @urgent-color;
}

element normal.active {
   background-color: @background-color;
   text-color: @main-color;
}

element selected.normal {
    background-color: @border-color;
    text-color:       @selected-color;
}

element selected.urgent {
    background-color: @urgent-color;
    text-color:       @background-color;
}

element selected.active {
    background-color: @border-color;
    text-color:       @green;
}

element alternate.normal {
    background-color: @background-color;
    text-color:       @dark-text-color;
}

element alternate.urgent {
    background-color: @background-color;
    text-color:       @urgent-color;
}

element alternate.active {
    background-color: @background-color;
    text-color:       @main-color;
}

scrollbar {
   background-color: @background-color;
   handle-color: @background-color;
   handle-width: 0px;
}

mode-switcher {
   background-color: @background-color;
}

button {
   background-color: @background-color;
   text-color:       @text-color;
}

button selected {
    text-color:       @main-color;
}

inputbar {
   background-color: @background-color;
   spacing: 0px;
   children:   [ prompt,textbox-prompt-colon,entry,case-indicator ];
}

prompt {
   padding:0px 10px;
   background-color: @background-color;
   text-color: @highlight;
}

entry {
   padding:0px 6px;
   background-color:@background-color;
   text-color:@light1;
}

case-indicator {
   padding:6px 10px;
   text-color:@main-color;
   background-color:@background-color;
}

#textbox-prompt-colon {
	padding:0px 0px;
    expand:     false;
    str:        ":";
    margin:     0px 0.3em 0em 0em ;
    text-color: @highlight;
    background-color:@background-color;
}"""


def writefiles(dir):
    with open(dir + "color", "w") as colorfile:
        print("Creating color")
        colorfile.writelines(colorfiledata)
    with open(dir + "typeface", "w") as typefacefile:
        print("Creating typeface")
        typefacefile.writelines(typefacefiledata)
    with open(dir + "theme", "w") as themefile:
        print("Creating theme")
        themefile.writelines(themefiledata)
    with open(dir + "root", "w") as rootfile:
        print("Creating root")
        rootfile.writelines(rootfiledata)
    with open(dir + "rofi.rasi", "w") as rofifile:
        print("Creating rofi.rasi")
        rofifile.writelines(rofifiledata)


print(
    """
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`
"""
)
print(
    """
------------------------
Welcome to Regowal setup
------------------------
"""
)
ans = input("Do you want to create a standalone theme for regowal? (y,N)?   ")
if ans != "y":
    print("Dont forget to pass the theme you want to edit when calling ./regowal")
    print("*note editing theme colors is permanent (recommend having standalone theme)")
else:
    command = subprocess.call(["mkdir", str("/home/" + username + "/Regowal/")])
    if command == 0:
        print("Directory created at /home/" + username + "/etc/Regowal/")
        command = subprocess.call(
            ["mkdir", str("/home/" + username + "/Regowal/styles/")]
        )
        command = subprocess.call(
            ["mkdir", str("/home/" + username + "/Regowal/styles/regowaltheme/")]
        )
        if command == 0:
            print("Directory created at /home/" + username + "/etc/Regowal/styles/")

    else:
        print("***")
        print("Failed to make the Regowal directory - it might already be created")
        print("***")
newdirectory = "/home/" + username + "/Regowal/styles/regowaltheme/"
print(
    """
Converting regowal.py to regowal and making it executable
"""
)
subprocess.call(["cp", "regowal.py", "regowal"])
subprocess.call(["chmod", "+x", "regowal"])
writefiles(newdirectory)
with open("/home/" + username + "/.Xresources-regolith", "r") as xresfile:
    newxresfile = ""
    data = xresfile.readlines()
    print(data)
    for line in data:
        print(line)
        if line.find("root"):
            line = (
                '#include "/home/' + username + '/Regowal/styles/regowaltheme/root"\n'
            )
        newxresfile += line
with open("/home/" + username + "/.Xresources-regolith", "w") as xresfile:
    xresfile.writelines(newxresfile)
print(
    """
----------------------------------------------------------
Setup complete => './regowal <theme> <wallpaper>' is ready
----------------------------------------------------------
"""
)
