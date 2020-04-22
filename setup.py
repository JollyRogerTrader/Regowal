import subprocess, os, re
import filecreator

username = os.environ.get("USER")


def writefiles(dir):
    filecreator.writeColorfile(dir)
    filecreator.writeRofifile(dir)
    filecreator.writeRootfile(dir)
    filecreator.writeThemefile(dir)
    filecreator.writeTypefacefile(dir)


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
print(
    """
This script will modify your system to use Regowal. Please visit https://github.com/JollyRogerTrader/Regowal to find support and feel free to report bugs.
"""
)
ans = input("Are you sure you want to continue?   [y/n]?")
if ans != "y":
    exit()
try:
    print("Creating needed directories.")
    command = subprocess.call(["mkdir", str("/home/" + username + "/.regowal/")])
    if command == 0:
        print("Directory created at /home/" + username + "/.regowal/")
        command = subprocess.call(
            ["mkdir", str("/home/" + username + "/.regowal/styles/")]
        )
        command = subprocess.call(
            ["mkdir", str("/home/" + username + "/.regowal/styles/regowaltheme/")]
        )
        if command == 0:
            print("Directory created at /home/" + username + "/.regowal/styles/")

    else:
        print()

except:
    print(
        "Error creating directories - this is probably a bug and should be reported to https://github.com/JollyRogerTrader/Regowal"
    )


newdirectory = "/home/" + username + "/.regowal/styles/regowaltheme/"

# writing template files
writefiles(newdirectory)
xrescommand = None

try:
    xrescommand = subprocess.check_output(
        ["cat", "/home/" + username + "/.Xresources-regolith"]
    )
except:
    print("Did not find a Xresources-regolith file")

if len(str(xrescommand).split("\n")) > 1:
    print(
        ".Xresources-regolith has been customized with additional settings - editing will have to be done manually"
    )
    print(
        "modify .Xresources-regolith to read: "
        + '#include "/home/'
        + username
        + '/.regowal/styles/regowaltheme/root"\n'
    )
else:
    try:
        with open("/home/" + username + "/.Xresources-regolith", "w") as xresfile:
            xresfile.write(
                '#include "/home/' + username + '/.regowal/styles/regowaltheme/root"\n'
            )
    except:
        print("Could not write Xresources-regolith file")

print(
    """
Converting regowal.py to regowal and making it executable
"""
)

# making regowal executable
subprocess.call(["cp", "regowal.py", "regowal"])
subprocess.call(["chmod", "+x", "regowal"])

print(
    """
----------------------------------------------------------
Setup complete => './regowal <wallpaper>' is ready
----------------------------------------------------------
"""
)
