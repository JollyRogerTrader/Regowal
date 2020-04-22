#!/usr/bin/env python3
import os, sys, time, subprocess, shutil, random, filecreator

username = os.environ.get("USER")
themeFileLocation = ""

# Helper functions
def exitMessage():
    print("exiting to terminal")
    exit()


def listToString(s):
    str1 = " "
    return str1.join(s)


# Function to call "convert" and generate color pallete
def getColors(img):
    print("Generating colors... This might take awhile")
    flags = ["-resize", "25%", "-colors", str(16), "-unique-colors", "txt:-"]
    img += "[0]"
    return subprocess.check_output(["convert", img, *flags]).splitlines()


# Saves the new color scheme to a file in ~/.regowal/styles/regowaltheme for safe keeping
def saveColorCache(scheme):
    newS = []  # new array to store hex colors
    scheme = scheme.split()  # split the "dirty list"
    for item in scheme:  # cycle through array items
        if len(item) == 7 and item[0] == "#":  # indexed item matches a hex color
            newS.append(item)  # append to list
        # send list to be brighten/darkened
    newScheme = sorted(newS)
    filecreator.writeColorfile(
        "/home/" + username + "/.regowal/styles/regowaltheme/",
        newScheme[0],
        newScheme[15],
        newScheme[2],
        newScheme[13],
        newScheme[14],
        newScheme[15],
        newScheme[3],
        newScheme[4],
        newScheme[5],
        newScheme[6],
        newScheme[7],
        newScheme[8],
        newScheme[9],
        newScheme[10],
        newScheme[11],
        newScheme[12],
    )
    filecreator.writeRofifile(
        "/home/" + username + "/.regowal/styles/regowaltheme/",
        newScheme[13],
        newScheme[14],
        newScheme[14],
        newScheme[4],
        newScheme[15],
        newScheme[10],
        newScheme[0],
        newScheme[14],
        newScheme[2],
        newScheme[14],
        newScheme[14],
    )


# Sets the wallpaper in theme specified and copies it to ~/.regowal/styles/regowaltheme/wallpaper for safe keeping
def setWallPaper(picDir):
    command = subprocess.call(
        [
            "cp",
            str(picDir),
            str("/home/" + username + "/.regowal/styles/regowaltheme/wallpaper"),
        ]
    )
    with open(
        "/home/" + username + "/.regowal/styles/regowaltheme/theme", "r"
    ) as themesettings:
        newTheme = ""
        for line in themesettings:
            line = line.split()
            if len(line) > 0 and line[1] == "desktop_wallpaper":
                line[2] = (
                    "/home/" + username + "/.regowal/styles/regowaltheme/wallpaper"
                )
            if len(line) == 3:
                newTheme += (
                    str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n"
                )
    with open(
        "/home/" + username + "/.regowal/styles/regowaltheme/theme", "w"
    ) as writefile:
        writefile.writelines(newTheme)


# writes the color theme in the theme specified in the arguments
def writeNewColorFile(newColors, oldColors):
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
                line[2] = newColors[14].strip("\n")
            if line[1] == "color_base1":
                line[2] = newColors[14].strip("\n")
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


def main():

    # pull args to identify the image selected
    if len(sys.argv) > 1:
        image = sys.argv[1]
    else:
        print(
            "No image is selected - using cached scheme in /home/"
            + username
            + "/.regowal/styles/"
        )
        image = None

    # Confirm the user wants to proceed
    answer = input("Are you sure you want to continue?   (y,N) ")
    if answer != "y":
        exitMessage()

    # Opening theme file to retrieve data
    themeFileLocation = "/home/" + username + "/.regowal/styles/regowaltheme/color"
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

    # Call function to get color palette and save
    if image != None:
        colors = getColors(image)
        saveColorCache(str(colors))
    else:
        colors = oldColors

    # Call function to set wallpaper from passed picture
    setWallPaper(image)

    # Command to refresh regolith-look
    answer = input("Want to refresh regolith?   (y/N) ")
    if answer != "y":
        exitMessage()
    else:
        print("Refreshing Regolith")
        subprocess.check_output(["regolith-look", "refresh"])

    exitMessage()


if __name__ == "__main__":
    main()
