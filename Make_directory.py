#This script will make the directorys for the photos
import os, shutil, sys

source = os.path.abspath('../SCRIPTS/Multi_watermark.py')
print source

def userInput():
    product_name = raw_input("name of the server or item: ")
    drives = raw_input("how many drive bays are there? ")
    cards = raw_input("What RAID cards will be used? seperate with commas, no spaces between entries: ")
    cpus = raw_input("How many procs can this server hold? ")
    cards = cards.split(',')
    return (product_name, int(drives),cards, int(cpus))

dir_setup = userInput()

print dir_setup
os.mkdir(dir_setup[0])
os.chdir(dir_setup[0])
destination = os.path.abspath('')
os.mkdir("Other")
os.chdir('Other')
for i in range(len(dir_setup[2])):
    os.mkdir(dir_setup[2][i])
    os.chdir(dir_setup[2][i])
    for i in range(dir_setup[3]):
        os.mkdir(str(i + 1) + "-CPU")
    os.chdir('..')
os.chdir('..')
os.mkdir('Drives')
os.chdir('Drives')
destination = os.path.abspath('')
for i in range(dir_setup[1] + 1):
    folder_name = str(i) + " Drives"
    os.mkdir(folder_name)
    shutil.copy(source, destination + "\\" + folder_name + "\\")
