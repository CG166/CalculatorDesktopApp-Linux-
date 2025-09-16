
*This will be a calculator desktop app for Linux(Ubuntu)* 
Recompile resource collection file after every resource change
- **pyrcc5 resources.qrc -o resources_rc.py**
  
*This will be a calculator desktop app for Linux(Ubuntu)*
- Recompile resource collection file after every resource change
--pyrcc5 resources.qrc -o resources_rc.py 

Create the desktop application executable with the command: 
- **pyinstaller --noconfirm --onefile --windowed main.py**

 Run Debian Installer to install Calculator Desktop App:
 - Download Calculator_1.0.deb
 - Install by clicking on the file and running it or by using the command **sudo dpkg -i Calculator_1.0.deb**

Remove application by running the command **sudo dpkg -r calculator**
