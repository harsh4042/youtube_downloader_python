# YouTube Video Downloader

A simple YouTube Video Downloader GUI application built using Python, `tkinter`, and `yt_dlp`. This application allows users to download YouTube videos with a smooth, animated progress bar and percentage display.

## Features

- Download videos from YouTube in the best available quality.
- Animated progress bar with percentage completion display.
- Easy-to-use graphical interface created with `customtkinter`.
- Windows `.exe` support for standalone usage.

---

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Building the Executable](#building-the-executable)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

---

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Contents of requirements.txt:

plaintext
Copy code
customtkinter
yt_dlp
Requirements
Python 3.6 or later
Windows OS (for .exe support)
The following Python packages:
customtkinter
yt_dlp
Note: yt_dlp is used for YouTube video downloads and handles various formats and resolutions.

Usage
Run the application using the following command:

bash
Copy code
python youtube_downloader.py
Enter the YouTube video link in the text box and click Download.

The video will download to the specified folder path in the script (currently set to C:\Users\bagul\Downloads\Telegram Desktop).
A smooth progress bar and percentage will indicate download progress.
Building the Executable
To convert this Python script to a Windows .exe file, you can use PyInstaller.

Install PyInstaller:

bash
Copy code
pip install pyinstaller
Run PyInstaller to build a standalone executable:

bash
Copy code
pyinstaller --onefile --noconsole youtube_downloader.py
This will create a dist folder containing youtube_downloader.exe.
Double-click youtube_downloader.exe to run the application as a standalone Windows application.
Troubleshooting
Issue: Download Jumps from 0% to 100%
If the progress bar jumps straight from 0% to 100%, please ensure that:

yt_dlp is correctly installed.
You have a stable internet connection.
Issue: SSL Certificate Error
Some users may encounter SSL errors due to outdated certificates. To fix this, update Python’s SSL certificates by running:

bash
Copy code
/Applications/Python\ 3.x/Install\ Certificates.command
Other Issues
If you encounter any other issues, please open an issue in this repository or consult the yt_dlp documentation for additional help.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
