<<<<<<< HEAD
*This will be a calculator desktop app for Linux(Ubuntu)* 
Recompile resource collection file after every resource change
- **pyrcc5 resources.qrc -o resources_rc.py**
=======
*This will be a calculator desktop app for Linux(Ubuntu)*
- Recompile resource collection file after every resource change
--pyrcc5 resources.qrc -o resources_rc.py 

Create the desktop application with the command: 
- **pyinstaller --noconfirm --onefile --windowed main.py**
>>>>>>> 91117b6 (Changed QRC file to properly load images, creating desktop app is functional)
