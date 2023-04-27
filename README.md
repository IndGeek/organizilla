Download from SourceForge:
<br/>
<a href="https://sourceforge.net/projects/organizilla/files/latest/download"><img alt="Download Organizilla" src="https://a.fsdn.com/con/app/sf-download-button" width=170 srcset="https://a.fsdn.com/con/app/sf-download-button?button_size=2x 2x"></a>

## Use organiZilla 
It creates Folders accordingly, based on file type like images, video, audio, documents, programs, scripts etc.

- Copy and paste te organizilla.exe to the folder where you have messed up files.
- Double click on the exe file, and done!

## Customize the source code ( for developers )

### Windows
```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole --name organizilla --icon=organizilla.ico organizilla.py
```


### Linux 
```bash
pip3 install pandas
pip3 install pyinstaller
pyinstaller --onefile organizilla.py
chmod +x organizilla
```

