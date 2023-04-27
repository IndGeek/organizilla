## Use organiZilla 

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

