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

# making regowal executable
subprocess.call(["cp", "regowal.py", "regowal"])
subprocess.call(["chmod", "+x", "regowal"])

# writing template files
writefiles(newdirectory)
# os.system("touch ~/.Xresources-regolith")

try:
    with open("/home/" + username + "/.Xresources-regolith", "w") as xresfile:
        xresfile.write(
            '#include "/home/' + username + '/Regowal/styles/regowaltheme/root"\n'
        )
except:
    print("Could not write Xresources-regolith file")

print(
    """
----------------------------------------------------------
Setup complete => './regowal <wallpaper>' is ready
----------------------------------------------------------
"""
)
