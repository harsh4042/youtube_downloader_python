import tkinter
import customtkinter
from yt_dlp import YoutubeDL
import time

# Initialize checkpoint index and total percentage completion for smoother progress updates
current_checkpoint_index = 0
update_intervals = [10, 25, 50, 80, 100]  # Define the points of gradual updates

# Download progress hook to update progress bar
def progress_hook(d):
    global current_checkpoint_index
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', 1)
        percent_complete = int((downloaded_bytes / total_bytes) * 100)

        # Move the progress bar gradually at set checkpoints
        if percent_complete >= update_intervals[current_checkpoint_index]:
            progressBar.set(update_intervals[current_checkpoint_index] / 100)
            pPercentage.configure(text=f"{update_intervals[current_checkpoint_index]}%")
            current_checkpoint_index += 1
            
            # Add a slight delay to simulate gradual updating
            time.sleep(0.2)

    elif d['status'] == 'finished':
        finishLable.configure(text="Downloaded!", text_color="green")
        progressBar.set(1)
        pPercentage.configure(text="100%")

# Reset the checkpoint before each download
def start_download():
    global current_checkpoint_index
    current_checkpoint_index = 0  # Reset checkpoint index at the start of each download
    ytLink = link.get()
    try:
        # Options for yt_dlp
        ydl_opts = {
            'format': 'best',  # Choose the best available quality
            # 'outtmpl': r"C:\Users\bagul\Downloads\Telegram Desktop\%(title)s.%(ext)s",  # Specify the download location
            'progress_hooks': [progress_hook]  # Attach the progress hook
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
    except Exception as e:
        finishLable.configure(text="Download Error", text_color="red")

# System settings theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube Video Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishLable = customtkinter.CTkLabel(app, text="")
finishLable.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# run app
app.mainloop()
