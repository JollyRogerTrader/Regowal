import subprocess, os, re

username = os.environ.get('USER')


def writeColorFile(dir):
    with open(dir + "color", "w") as colorfile:
        print("Creating color")
        colorfiledata = """#define color_base03   #2E3440
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
        colorfile.writelines(colorfiledata)


def writeTypefacefile(dir):
    with open(dir + "typeface", "w") as typefacefile:
        print("Creating typeface")
        typefacefiledata = """
! Typeface: Source Code Pro
#define typeface_bar_glyph  Source Code Pro Medium 13
#define typeface_wm         Source Code Pro Medium 13
#define typeface_bar        pango:Source Code Pro Medium 13, Material Design Icons 13
#define typeface_rofi       Source Code Pro Medium 13
#define typeface_terminal   Source Code Pro:pixelsize=18:antialias=true:autohint=true

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
        typefacefile.writelines(typefacefiledata)


def writeThemefile(dir):
    with open(dir + "theme", "w") as themefile:
        print("Creating theme")
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
        themefile.writelines(themefiledata)


def writeRootfile(dir):
    with open(dir + "root", "w") as rootfile:
        print("Creating root")
        rootfiledata = (
            """! -- Styles - Colors
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
        rootfile.writelines(rootfiledata)


def writeRofifile(dir):
    with open(dir + "rofi.rasi", "w") as rofifile:
        print("Creating rofi.rasi")
        rofifiledata = """/* global settings and color variables */
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
        rofifile.writelines(rofifiledata)
