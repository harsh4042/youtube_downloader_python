# YouTube Video Downloader

A simple YouTube Video Downloader GUI application built using Python, `tkinter`, and `yt_dlp`. This application allows users to download YouTube videos with a smooth, animated progress bar and percentage display.

## Features

- Download videos from YouTube in the best available quality
- Animated progress bar with percentage completion display
- Easy-to-use graphical interface created with `customtkinter`
- Windows `.exe` support for standalone usage


![image](https://github.com/user-attachments/assets/d4860057-cec5-4f6a-a25b-09c27ce121f3)


## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Building the Executable](#building-the-executable)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

## Requirements

- Python 3.6 or later
- Windows OS (for .exe support)
- Required Python packages:
  - `customtkinter`
  - `yt_dlp` (handles various video formats and resolutions)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Contents of requirements.txt:
```plaintext
customtkinter
yt_dlp
```

## Usage

1. Run the application using the following command:
   ```bash
   python youtube_downloader.py
   ```

2. Enter the YouTube video link in the text box and click Download
3. The video will download to the specified folder path in the script (currently set to `C:\Users\bagul\Downloads\Telegram Desktop`)
4. A smooth progress bar and percentage will indicate download progress

## Building the Executable

To convert this Python script to a Windows .exe file:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the standalone executable:
   ```bash
   pyinstaller --onefile --noconsole youtube_downloader.py
   ```

The process will create a `dist` folder containing `youtube_downloader.exe`. Double-click the `.exe` file to run the application as a standalone Windows application.

## Troubleshooting

### Issue: Download Jumps from 0% to 100%

If the progress bar jumps straight from 0% to 100%, ensure that:
- `yt_dlp` is correctly installed
- You have a stable internet connection

### Issue: SSL Certificate Error

Some users may encounter SSL errors due to outdated certificates. To fix this, update Python's SSL certificates:
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

### Other Issues

If you encounter any other issues:
- Open an issue in this repository
- Consult the `yt_dlp` documentation for additional help

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.
