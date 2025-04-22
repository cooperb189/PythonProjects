from pathlib import Path
import os, send2trash, pyinputplus as pi, shutil, sys

## FUNCTIONS
def delFolder(folder):
    answer = pi.inputYesNo(f"Are you sure you want to delete {folder}?: ").lower().strip()
    try:
        if answer == 'yes':
            send2trash.send2trash(folder)
            print("File/folder deleted.")
        else:
            print("Returning to main menu...")
    except:
        print("Invalid path object, please try again.")

def viewFolder(folder):
    for folName, sfName, fName in os.walk(folder):
        sfCount = 0
        fCount = 0
        print (f'The current folder is: {folName}.')
        for subfolders in sfName:
            print (f'The current subfolder is: {subfolders}.')
            sfCount += 1
        for files in fName:
            print(f'The current file is: {files}.')
            fCount += 1
        print()

def copyFolder(folder):
    nf = Path(input("Enter the absolute path of the location you want the new folder in: "))
    name = Path(input("Enter the name you want for your new folder: "))
    home = folder.parent
    shutil.copytree(home / folder, nf / name)

def copyFile(file):
    f = Path(input("Enter the absolute path for the folder you want to move the file into: "))
    home = file.parent
    home2 = f.parent
    shutil.copy(home / file, home2 / f)

def ans():
    oneOr2 = pi.inputNum("Press 1 to continue or 2 to exit: ", min=1, max=2)
    if oneOr2 == 2:
        sys.exit('Exiting...')

## MAIN PROGRAM LOOP 
while True:
    try:
        cli = pi.inputMenu(
            ['View Folder Contents', 'Delete Folders/Files', 'Copy Folders/Files', 'Edit Folders/Files'],
            prompt= f"\nChoose an option from the File Organizer:\n",
            numbered=True)

        if cli == 'View Folder Contents':
            viewFolder(Path(input("Enter the absolute path for the folders/files you're looking to check: ")))
            print("Finished")
            ans()
            continue

        elif cli == 'Delete Folders/Files':
            delFolder(Path(input("Enter the absolute path for the folders/files you want to delete: ")))
            ans()
            continue

        elif cli == 'Copy Folders/Files':
            copyChoice = pi.inputMenu(
                ['Copy Folder', 'Copy File'],
                prompt=f"\nWould you like to copy a folder or a file?\n",
                numbered=True)        
            if copyChoice == 'Copy Folder':
                copyFolder(Path(input("Enter the absolute path for the folder you want to copy: ")))
            elif copyChoice == 'Copy File':
                copyFile(Path(input("Enter the absolute path for the name and extension of the file you want to copy: ")))
            print("Completed")
            ans()
            continue

        elif cli == 'Edit Folders/Files':
            editChoice = pi.inputMenu(
                ['Move File Location', 'Move Folder Location', 'Organize Python Files'],
                prompt=f"\nChoose one of the following options:\n",
                numbered=True)
            if editChoice == 'Move File Location':
                msgFile = input(Path("Enter the absolute path of the file you want to transfer: "))
                locateFile = input(Path("Enter the absolute path of the folder you want to move the file to: "))
                shutil.move(msgFile, locateFile)
                print("Transfer completed")
            elif editChoice == 'Move Folder Location':
                msgFolder = input(Path("Enter the absolute path of the folder you want to transfer: "))
                locateFolder = input(Path("Enter the absolute path of the folder you want to transfer this folder into: "))
                shutil.move(msgFolder, locateFolder)
                print("Transfer completed")

        else:
            ans()
            continue
    except:
        print("An error has occured.")
        ans()
        print("Returning to main menu...")
        continue
