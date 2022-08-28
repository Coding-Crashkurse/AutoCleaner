# AutoCleaner

<h2>Works on Windows only!</h2>

<h3>Autodelete files in repositories which are older than 7 days</h3>

This Repo contains a `main.py` file which sould be converted to a `.exe` file to work as intended.

How to make it work:

1. `pip install pyinstaller`
2. `pyinstaller main.py --onefile -w`

This will create a dist folder which an executeable. When you click on the .exe file it will create the following dir and file:

`C:\Users\<user>\Autoclean\delete_folders.txt`

In this file you can copy as many repositories as you want which you want to monitor. Default is to monitor the Downloads folder.
It will also write an `open.bat` into the following folder: `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

This will cause to run the python script every time you want to start your computer.
