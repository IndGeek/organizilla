import os
import shutil
import tkinter as tk
from tkinter import messagebox

DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".avi", ".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".sh", ".bat"],
    "Others": [] # leave it empty
}

cwd = os.getcwd()

# Create directories
for directory, extensions in DIRECTORIES.items():
    # Check if any files have the relevant extension
    if any([os.path.isfile(file) for file in os.listdir(cwd) if os.path.splitext(file)[1].lower() in extensions]):
        path = os.path.join(cwd, directory)
        os.makedirs(path, exist_ok=True)

# Organize files
for file in os.listdir(cwd):
    if os.path.isfile(os.path.join(cwd, file)):
        file_path = os.path.join(cwd, file)
        file_ext = os.path.splitext(file_path)[1]
        for directory, extensions in DIRECTORIES.items():
            if file_ext.lower() in extensions:
                dest_dir = os.path.join(cwd, directory)
                shutil.move(file_path, dest_dir)
                break
        else:
            dest_dir = os.path.join(cwd, "Others")
            shutil.move(file_path, dest_dir)

# Prompt the user with a message box
root = tk.Tk()
root.withdraw()
result = messagebox.askquestion("OrganiZilla", "Done organizing your files! Would you like to donate?")

if result == 'Sure':
    # Open website for donation
    import webbrowser
    webbrowser.open('https://organizilla.nated.in/donate')
elif result == 'No Thanks':
    # do nothing
    pass
else:
    # do something else
    pass