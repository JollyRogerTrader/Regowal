import subprocess, os, re

# This is just a collection of functions to write file using a template system.
# Do not edit this unless you are careful with how the file is formated when it is written

username = os.environ.get("USER")


def writeColorfile(
    dir,
    c03="#2E3440",
    c02="#3B4252",
    c01="#434C5E",
    c00="#7B8394",
    c0="#D8DEE9",
    c1="#E5E9F0",
    c2="#ECEFF4",
    c3="#ECEFF4",
    cy="#EBCB8B",
    co="#D08770",
    cr="#BF616A",
    cm="#5E81AC",
    cv="#B48EAD",
    cb="#81A1C1",
    cc="#88C0D0",
    cg="#A3BE8C",
):
    with open(dir + "color", "w") as colorfile:
        print("Creating color")
        colorfiledata = (
            """#define color_base03   """
            + c03
            + """
#define color_base02   """
            + c02
            + """
#define color_base01   """
            + c01
            + """
#define color_base00   """
            + c00
            + """
#define color_base0    """
            + c0
            + """
#define color_base1    """
            + c1
            + """
#define color_base2    """
            + c2
            + """
#define color_base3    """
            + c3
            + """
#define color_yellow   """
            + cy
            + """
#define color_orange   """
            + co
            + """
#define color_red      """
            + cr
            + """
#define color_magenta  """
            + cm
            + """
#define color_violet   """
            + cv
            + """
#define color_blue     """
            + cb
            + """
#define color_cyan     """
            + cc
            + """
#define color_green    """
            + cg
            + """
"""
        )
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
            + """/.regowal/styles/regowaltheme/rofi.rasi

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
            + """/.regowal/styles/regowaltheme/color"

! -- Styles - Fonts
#include "/home/"""
            + username
            + """/.regowal/styles/regowaltheme/typeface"

! -- Styles - Theme
#include "/home/"""
            + username
            + """/.regowal/styles/regowaltheme/theme"

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


def writeRofifile(
    dir,
    blue="#81A1C1",
    darkblue="#5E81AC",
    cyan="#8FBCBB",
    lightcyan="#88C0D0",
    green="#A3BE8C",
    red="#BF616A",
    dark1="#2E3440",
    dark2="#3B4252",
    dark3="#434C5E",
    dark4="#4C566A",
    light1="#D8DEE9",
):
    with open(dir + "rofi.rasi", "w") as rofifile:
        print("Creating rofi.rasi")
        rofifiledata = (
            """/* global settings and color variables */
* {
   blue:             """
            + blue
            + """;
   darkblue:         """
            + darkblue
            + """;
   cyan:             """
            + cyan
            + """;
   lightcyan:        """
            + lightcyan
            + """;
   green:            """
            + green
            + """;
   red:              """
            + red
            + """;

   dark1:            """
            + dark1
            + """;
   dark2:            """
            + dark2
            + """;
   dark3:            """
            + dark3
            + """;
   dark4:            """
            + dark4
            + """;

   light1:           """
            + light1
            + """;

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
        )
        rofifile.writelines(rofifiledata)
