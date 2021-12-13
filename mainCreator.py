# MULTIMEDIA FILESYSTEM CREATOR

import os

# _PROJECTNAME_
# MAIN MIX FILES    MEDIA         EXPORTS         LOG.txt 
#                    |
#          AUDIO   FOOTAGE   IMAGES

parentDir = input("PARENT DIRECTORY:        ")
mode = 0o666

logFile = open(os.path.join(parentDir,"LOG.txt"),'w+')

#Top Dirs
tDir1 = os.path.join(parentDir,"MAIN_MIX")
tDir2 = os.path.join(parentDir,"MEDIA")
tDir3 = os.path.join(parentDir,"EXPORTS")

#Sub Dirs
sDir1 = os.path.join(tDir2,"AUDIO")
sDir2 = os.path.join(tDir2,"FOOTAGE")
sDir3 = os.path.join(tDir2,"IMAGES")

os.mkdir(tDir1, mode)
os.mkdir(tDir2, mode)
os.mkdir(tDir3, mode)
os.mkdir(sDir1, mode)
os.mkdir(sDir2, mode)
os.mkdir(sDir3, mode)

logFile.write("Yay! The files were all created and no-one had to cry!")
