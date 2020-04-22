#!/usr/bin/env python3
import os, sys, time, subprocess, shutil, random, filecreator

user_name = os.environ.get("USER")
theme_file_location = ""

# Helper functions
def exit_message():
    print("exiting to terminal")
    exit()


def list_to_string(s):
    strr = " "
    return strr.join(s)


# Function to call "convert" and generate color pallete
def get_colors(img):
    print("Generating colors... This might take awhile")
    flags = ["-resize", "25%", "-colors", str(16), "-unique-colors", "txt:-"]
    img += "[0]"
    return subprocess.check_output(["convert", img, *flags]).splitlines()


# Saves the new color scheme to a file in ~/.regowal/styles/regowaltheme for safe keeping
def save_color_cache(scheme):
    new = []  # new array to store hex colors
    scheme = scheme.split()  # split the "dirty list"
    for item in scheme:  # cycle through array items
        if len(item) == 7 and item[0] == "#":  # indexed item matches a hex color
            new.append(item)  # append to list
        # send list to be brighten/darkened
    new_scheme = sorted(new)
    filecreator.write_color_file(
        "/home/" + user_name + "/.regowal/styles/regowaltheme/",
        new_scheme[0],
        new_scheme[15],
        new_scheme[2],
        new_scheme[13],
        new_scheme[14],
        new_scheme[15],
        new_scheme[3],
        new_scheme[4],
        new_scheme[5],
        new_scheme[6],
        new_scheme[7],
        new_scheme[8],
        new_scheme[9],
        new_scheme[10],
        new_scheme[11],
        new_scheme[12],
    )
    filecreator.write_rofi_file(
        "/home/" + user_name + "/.regowal/styles/regowaltheme/",
        new_scheme[13],
        new_scheme[14],
        new_scheme[14],
        new_scheme[4],
        new_scheme[15],
        new_scheme[10],
        new_scheme[0],
        new_scheme[14],
        new_scheme[2],
        new_scheme[14],
        new_scheme[14],
    )


# Sets the wallpaper in theme specified and copies it to ~/.regowal/styles/regowaltheme/wallpaper for safe keeping
def set_wall_paper(pic_dir):
    command = subprocess.call(
        [
            "cp",
            str(pic_dir),
            str("/home/" + user_name + "/.regowal/styles/regowaltheme/wallpaper"),
        ]
    )
    with open(
        "/home/" + user_name + "/.regowal/styles/regowaltheme/theme", "r"
    ) as theme_settings:
        new_theme = ""
        for line in theme_settings:
            line = line.split()
            if len(line) > 0 and line[1] == "desktop_wallpaper":
                line[2] = (
                    "/home/" + user_name + "/.regowal/styles/regowaltheme/wallpaper"
                )
            if len(line) == 3:
                new_theme += (
                    str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n"
                )
    with open(
        "/home/" + user_name + "/.regowal/styles/regowaltheme/theme", "w"
    ) as write_file:
        write_file.writelines(new_theme)


# writes the color theme in the theme specified in the arguments
def write_new_color_file(new_colors, old_colors):
    new_colors = new_colors.split()
    new_color_file = ""
    for line in old_colors:
        if len(line) > 2:
            line = line.split()
            if line[1] == "color_base03":
                line[2] = new_colors[0]
            if line[1] == "color_base02":
                line[2] = new_colors[1].strip("\n")
            if line[1] == "color_base01":
                line[2] = new_colors[2].strip("\n")
            if line[1] == "color_base00":
                line[2] = new_colors[3].strip("\n")
            if line[1] == "color_base0":
                line[2] = new_colors[14].strip("\n")
            if line[1] == "color_base1":
                line[2] = new_colors[14].strip("\n")
            if line[1] == "color_base2":
                line[2] = new_colors[6].strip("\n")
            if line[1] == "color_base3":
                line[2] = new_colors[7].strip("\n")
            if line[1] == "color_yellow":
                line[2] = new_colors[8].strip("\n")
            if line[1] == "color_orange":
                line[2] = new_colors[9].strip("\n")
            if line[1] == "color_red":
                line[2] = new_colors[10].strip("\n")
            if line[1] == "color_magenta":
                line[2] = new_colors[11].strip("\n")
            if line[1] == "color_violet":
                line[2] = new_colors[12].strip("\n")
            if line[1] == "color_blue":
                line[2] = new_colors[13].strip("\n")
            if line[1] == "color_cyan":
                line[2] = new_colors[14].strip("\n")
            if line[1] == "color_green":
                line[2] = new_colors[15].strip("\n")
            new_color_file += str(line[0] + "  " + line[1] + "  " + line[2] + "\n")
    with open(theme_file_location, "w+") as file:
        file.writelines(new_color_file)


def main():

    # pull args to identify the image selected
    if len(sys.argv) > 1:
        image = sys.argv[1]
    else:
        print(
            "No image is selected - using cached scheme in /home/"
            + user_name
            + "/.regowal/styles/"
        )
        image = None

    # Confirm the user wants to proceed
    answer = input("Are you sure you want to continue?   (y,N) ")
    if answer != "y":
        exit_message()

    # Opening theme file to retrieve data
    theme_file_location = "/home/" + user_name + "/.regowal/styles/regowaltheme/color"
    try:
        with open(theme_file_location, "r") as theme_File:
            old_colors = theme_File.readlines()
    except:
        print(
            "No color file found with "
            + theme_file_location
            + ". Verify you spelled it correctly"
        )
        exit_message()

    # Call function to get color palette and save
    if image != None:
        colors = get_colors(image)
        save_color_cache(str(colors))
    else:
        colors = old_colors

    # Call function to set wallpaper from passed picture
    set_wall_paper(image)

    # Command to refresh regolith-look
    answer = input("Want to refresh regolith?   (y/N) ")
    if answer != "y":
        exit_message()
    else:
        print("Refreshing Regolith")
        subprocess.check_output(["regolith-look", "refresh"])

    exit_message()


if __name__ == "__main__":
    main()
