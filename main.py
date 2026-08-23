import os
import tkinter as tk
from tkinter import filedialog

import yt_dlp


def format_size(size):
    if not size:
        return "Unknown"

    if size >= 1024 ** 3:
        return f"{size / (1024 ** 3):.2f} GB"

    return f"{size / (1024 ** 2):.2f} MB"


def choose_folder():
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(
        title="Select a folder to save the video"
    )

    root.destroy()

    return folder


url = input("Enter YouTube video URL: ").strip()

if not url:
    print("Error: No URL was provided.")
    exit()


print("\nFetching video information...")

try:
    info_options = {
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(info_options) as ydl:
        info = ydl.extract_info(url, download=False)

except Exception as error:
    print("\nFailed to fetch video information.")
    print(f"Error: {error}")
    exit()


title = info.get("title", "Unknown")
duration = info.get("duration", 0)
formats = info.get("formats", [])


best_format = None

for video_format in formats:
    if (
        video_format.get("vcodec") != "none"
        and video_format.get("acodec") != "none"
        and video_format.get("filesize")
    ):
        best_format = video_format


if best_format:
    file_size = best_format.get("filesize")
else:
    file_size = info.get("filesize") or info.get("filesize_approx")


if duration:
    minutes = int(duration // 60)
    seconds = int(duration % 60)
    duration_text = f"{minutes}:{seconds:02d}"
else:
    duration_text = "Unknown"


print("\n" + "=" * 50)
print("Video Information")
print("=" * 50)

print(f"Title: {title}")
print(f"Duration: {duration_text}")
print(f"Estimated size: {format_size(file_size)}")

print("=" * 50)


confirmation = input("\nDo you want to download this video? (y/n): ")

if confirmation.lower() not in ("y", "yes"):
    print("Download cancelled.")
    exit()


print("\nSelect a folder for the downloaded video.")

save_folder = choose_folder()

if not save_folder:
    print("No folder was selected.")
    exit()


download_options = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": os.path.join(
        save_folder,
        "%(title)s.%(ext)s"
    ),
    "merge_output_format": "mp4",
}


print("\nStarting download...")

try:
    with yt_dlp.YoutubeDL(download_options) as ydl:
        ydl.download([url])

    print("\nDownload completed successfully.")
    print(f"Saved to: {save_folder}")

except Exception as error:
    print("\nDownload failed.")
    print(f"Error: {error}")
