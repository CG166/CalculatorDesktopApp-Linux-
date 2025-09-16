# Calculator Desktop App for Linux (Ubuntu)
### This is a Calculator Desktop Application built for Linux (Ubuntu).  
## Resource Compilation  
After every change to the resource file, recompile it using the following command:  
`pyrcc5 resources.qrc -o rc_resources.py`  
## Building the Executable  
To create the desktop application executable, run:  
`pyinstaller --noconfirm --onefile --windowed main.py`  
This will bundle the app into a standalone executable.  
## Installing the App (Debian Installer)
1. Download the installer file: [Calculator_1.0.deb](https://github.com/CG166/CalculatorDesktopApp-Linux-/blob/main/CalculatorDesktopApp%20.deb%20Installer/Calculator_1.0.deb)

2. Install the application by:
   - **Option 1:** Double-click the .deb file and follow the installation instructions.
   - **Option 2:** Open the terminal and run the command:
     `sudo dpkg -i Calculator_1.0.deb`
## Uninstalling the App
To remove the calculator application, run the command:  
`sudo dpkg -r calculator`
