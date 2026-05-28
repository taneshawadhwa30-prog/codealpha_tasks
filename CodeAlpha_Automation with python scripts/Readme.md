# 📁 Task 3: Automated File Organizer

A Python automation script that scans a specific source directory and automatically transfers all images with a `.jpg` extension into a designated destination folder.

## 🚀 Features
* Automatically creates the destination folder if it doesn't already exist.
* Uses the `os` module to scan directory contents.
* Efficiently moves files using `shutil`.
* Helps keep clutter-free directories.

## 🛠️ Technologies Used
* Python 3.x
* `os` module
* `shutil` module

## 💻 How to Run
1. Create a folder named `source` in the same directory and add some `.jpg` images to it.
2. Run the script:
```bash
   python organizer.py