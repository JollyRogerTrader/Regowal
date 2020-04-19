#!/usr/bin/env python3
import os, sys, time, subprocess, shutil

username = os.getlogin()

subprocess.call(["cp", "regowal.py", "regowal"])
subprocess.call(["chmod", "+x", "regowal"])

########################################################################
# Helper functions
########################################################################
def exitMessage():
    print("exiting to terminal")
    exit()


def listToString(s):
    str1 = " "
    return str1.join(s)


# Generate color pallete
def getColors(img):
    flags = ["-resize", "25%", "-colors", str(16), "-unique-colors", "txt:-"]
    img += "[0]"

    return subprocess.check_output(["convert", img, *flags]).splitlines()


# Saves the new color scheme to a file in /etc/regolith/styles for safe keeping
def saveColorCache(scheme):
    newScheme = ""
    scheme = scheme.split()
    for item in scheme:
        if len(item) == 7 and item[0] == "#":
            newScheme += item + "\n"
    with open("/home/" + username + "/Regowal/styles/walscheme", "w") as file:
        file.writelines(newScheme)
    writeNewColorFile(newScheme, oldColors)


# Sets the wallpaper in theme specified and copies to /usr/share/background for safe keeping
def setWallPaper(pic):
    print("setting wallpaper...")
    command = subprocess.call(
        [
            "cp",
            str(pic),
            str("/home/" + username + "/Regowal/styles/regowaltheme/wallpaper"),
        ]
    )

    with open(
        "/home/" + username + "/Regowal/styles/regowaltheme/theme", "r"
    ) as themesettings:
        newTheme = ""
        print("found theme")
        for line in themesettings:
            line = line.split()
            if len(line) > 0 and line[1] == "desktop_wallpaper":
                print("found wallpaper settings and changing")
                line[2] = pic
            if len(line) == 3:
                newTheme += (
                    str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n"
                )
    with open(
        "/home/" + username + "/Regowal/styles/regowaltheme/theme", "w"
    ) as writefile:
        writefile.writelines(newTheme)


# writes the color theme in the theme specified in the arguments
def writeNewColorFile(newColors, oldColors):
    print("setting colors...")
    newColors = newColors.split()
    newColorFile = ""
    for line in oldColors:
        if len(line) > 2:
            line = line.split()
            if line[1] == "color_base03":
                line[2] = newColors[0]
            if line[1] == "color_base02":
                line[2] = newColors[1].strip("\n")
            if line[1] == "color_base01":
                line[2] = newColors[2].strip("\n")
            if line[1] == "color_base00":
                line[2] = newColors[3].strip("\n")
            if line[1] == "color_base0":
                line[2] = newColors[4].strip("\n")
            if line[1] == "color_base1":
                line[2] = newColors[5].strip("\n")
            if line[1] == "color_base2":
                line[2] = newColors[6].strip("\n")
            if line[1] == "color_base3":
                line[2] = newColors[7].strip("\n")
            if line[1] == "color_yellow":
                line[2] = newColors[8].strip("\n")
            if line[1] == "color_orange":
                line[2] = newColors[9].strip("\n")
            if line[1] == "color_red":
                line[2] = newColors[10].strip("\n")
            if line[1] == "color_magenta":
                line[2] = newColors[11].strip("\n")
            if line[1] == "color_violet":
                line[2] = newColors[12].strip("\n")
            if line[1] == "color_blue":
                line[2] = newColors[13].strip("\n")
            if line[1] == "color_cyan":
                line[2] = newColors[14].strip("\n")
            if line[1] == "color_green":
                line[2] = newColors[15].strip("\n")
            newColorFile += str(line[0] + "  " + line[1] + "  " + line[2] + "\n")
    with open(themeFileLocation, "w+") as file:
        file.writelines(newColorFile)


if len(sys.argv) > 1:
    picture = sys.argv[1]
else:
    print(
        "No image is selected - using cached scheme in /home/"
        + username
        + "/Regowal/styles/"
    )
    picture = None

homedir = os.path.expanduser("~")

answer = input("Are you sure you want to continue?   (y,N) ")
if answer != "y":
    exitMessage()

########################################################################
# Opening theme file to retrieve data
########################################################################

themeFileLocation = "/home/" + username + "/Regowal/styles/regowaltheme/color"
try:
    with open(themeFileLocation, "r") as themeFile:
        oldColors = themeFile.readlines()
except:
    print(
        "No color file found with "
        + themeFileLocation
        + ". Verify you spelled it correctly"
    )
    exitMessage()

########################################################################
# Call function to get color palette and save
########################################################################
if picture != None:
    colors = getColors(picture)
    saveColorCache(str(colors))
else:
    colors = oldColors

########################################################################
# Call function to set wallpaper from passed picture
########################################################################
setWallPaper(picture)

######################################################################
# Command to refresh regolith-look
######################################################################
answer = input("Want to refresh regolith?   (y/N) ")
if answer != "y":
    exitMessage()
else:
    print("refreshing regolith")
    subprocess.check_output(["regolith-look", "refresh"])

exitMessage()
