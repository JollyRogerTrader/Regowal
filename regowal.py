#!/usr/bin/env python3
import os, sys, subprocess, filecreator, argparse
from PIL import Image
from collections import Counter

USER_NAME = os.environ.get("USER")

# Helper functions
def exit_message():
    print("exiting to terminal")
    exit()


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def list_to_string(s):
    strr = " "
    return strr.join(s)


def getnum(num):
    count = 0
    for i in num:
        if i != "#":
            if i == "f" or i == "F":
                count += 15
            elif i == "e" or i == "E":
                count += 14
            elif i == "d" or i == "D":
                count += 13
            elif i == "c" or i == "C":
                count += 12
            elif i == "b" or i == "B":
                count += 11
            elif i == "a" or i == "A":
                count += 10
            else:
                count += int(i)
    return count


def get_imcolors(image):
    picarray = []
    print("Generating colors... This might take awhile")
    flags = ["-resize", "25%", "-colors", str(16), "-unique-colors", "txt:-"]
    imcolors = subprocess.check_output(["convert", image, *flags]).splitlines()
    imcolors = str(imcolors).split()
    for item in imcolors:
        if item[0] == "#" and len(item) == 7:
            picarray.append(item)
    finaltups, out = [], []  # make a holding dict and final array
    for value in picarray:
        finaltups.append((getnum(value), value))  # make tuples and add to list
    sorted(finaltups, reverse=True)  # return tuple list sorted
    for i in finaltups:
        out.append(i[1])
    return out


# Get hex values for pixels in image
def get_pycolors(image):
    pic = Image.open(image)
    nwidth, nheight = 4, 4  # scale image to required 16 pixels
    pic1 = pic.resize((nwidth, nheight))
    picarray = []
    for x in range(nwidth):
        for y in range(nheight):
            value = pic1.getpixel((x, y))
            picarray.append(rgb2hex(value[0], value[1], value[2]))
    finaltups, out = [], []  # make a holding dict and final array
    for value in picarray:
        finaltups.append((getnum(value), value))  # make tuples and add to list
    sorted(finaltups, reverse=True)  # return tuple list sorted
    for i in finaltups:
        out.append(i[1])
    return out


def most_prominent(colorlist):
    dict = {}
    top_count = 0
    top_colors = []
    for item in colorlist:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] > top_count:
            top_count = dict[item]
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        top_colors.append(key)
    return top_colors


# Saves the new color scheme to a file in ~/.regowal/styles/regowaltheme for safe keeping
def save_color_theme(scheme):
    if len(scheme) >= 16:
        filecreator.write_color_file(
            "/home/" + USER_NAME + "/.regowal/styles/regowaltheme/",
            scheme[0],  # background
            scheme[15],  # i3bar main text
            scheme[0],
            scheme[15],  # number workspace text color
            scheme[15],  # i3bar
            scheme[15],  # i3bar
            scheme[2],
            scheme[3],
            scheme[13],  # files in ranger
            scheme[12],
            scheme[11],  # exec in ranger
            scheme[9],
            scheme[10],
            scheme[11],
            scheme[12],
            scheme[13],  # terminal text color
        )
        filecreator.write_rofi_file(
            "/home/" + USER_NAME + "/.regowal/styles/regowaltheme/",
            scheme[15],
            scheme[15],
            scheme[10],
            scheme[0],
            scheme[1],
            scheme[3],
            scheme[0],
            scheme[15],  # highlighter color
            scheme[2],
            scheme[15],
            scheme[15],
        )
    else:
        print(
            "Not enough colors detected, this happens when there isnt enough colors in the image selected"
        )


# Sets the wallpaper in theme specified and copies it to ~/.regowal/styles/regowaltheme/wallpaper for safe keeping
def set_wall_paper(pic_dir):
    command = subprocess.call(
        [
            "cp",
            str(pic_dir),
            str("/home/" + USER_NAME + "/.regowal/styles/regowaltheme/wallpaper"),
        ]
    )
    with open(
        "/home/" + USER_NAME + "/.regowal/styles/regowaltheme/theme", "r"
    ) as theme_settings:
        new_theme = ""
        for line in theme_settings:
            line = line.split()
            if len(line) > 0 and line[1] == "desktop_wallpaper":
                line[2] = (
                    "/home/" + USER_NAME + "/.regowal/styles/regowaltheme/wallpaper"
                )
            if len(line) == 3:
                new_theme += (
                    str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n"
                )
    with open(
        "/home/" + USER_NAME + "/.regowal/styles/regowaltheme/theme", "w"
    ) as write_file:
        write_file.writelines(new_theme)


def main():
    THEME_FILE_LOCATION = ""
    IMAGE = ""
    LIGHTMODE = False
    ONLYALT = False

    # parse arguments sent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-light", action="store_true", help="sets the color scheme to light mode",
    )
    parser.add_argument(
        "-alt",
        action="store_true",
        help="only use alternate means to generate colors (normally faster but can produce odd results",
    )
    parser.add_argument(
        "image",
        help="full path to image you want to use as your wallpaper and color scheme",
    )

    args = parser.parse_args()
    if args.light:
        LIGHTMODE = True
    if args.alt:
        ONLYALT = True
    if args.image:
        IMAGE = args.image

    if ONLYALT:
        colors = get_pycolors(IMAGE)
    else:
        colors = get_imcolors(IMAGE)
        if len(colors) < 16:
            print(
                "Not enough colors generated with ImageMagick - trying alternate means"
            )
            colors = get_pycolors(IMAGE)

    if LIGHTMODE:
        print("Generating light mode")
        save_color_theme(sorted(colors, reverse=True))
    else:
        save_color_theme(sorted(colors))

    # Call function to set wallpaper from passed picture
    set_wall_paper(IMAGE)

    # Command to refresh regolith-look
    print("Refreshing Regolith")
    subprocess.check_output(["regolith-look", "refresh"])

    exit_message()


if __name__ == "__main__":
    main()
