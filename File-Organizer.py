import os
import shutil
import sched
import time


def move_file(src_path, dest_path):
    # Check if the file has finished downloading
    while not os.path.exists(src_path):
        pass

    # Move the file from the download folder to the desired location
    shutil.move(src_path, dest_path)

# Set the paths for the download folder and the destination folders
download_folder = "C:\\Users\\isuru\\Downloads"
audio_folder = "C:\\Users\\isuru\\Downloads\\audio"
image_folder = "C:\\Users\\isuru\\Downloads\\image"
pdf_folder = "C:\\Users\\isuru\\Downloads\\pdf"
program_folder = "C:\\Users\\isuru\\Downloads\\program"
video_folder = "C:\\Users\\isuru\\Downloads\\video"

# Get the list of files in the download folder
files = os.listdir(download_folder)

# Iterate over the list of files and move them to the appropriate destination folder
for file in files:
    src_path = os.path.join(download_folder, file)
    if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".wmv") or file.endswith(".mov") or file.endswith(".flv") or file.endswith(".3gp") or file.endswith(".m4v"):
        dest_path = video_folder
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        move_file(src_path, dest_path)
    elif file.endswith(".mp3") or file.endswith(".flac") or file.endswith(".m4a") or file.endswith(".wma") or file.endswith(".aac") or file.endswith(".wav"):
        dest_path = audio_folder
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        move_file(src_path, dest_path)
    elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".ico") or file.endswith(".webp"):
        dest_path = image_folder
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        move_file(src_path, dest_path)
    elif file.endswith(".pdf") or file.endswith(".epub") or file.endswith(".mobi") or file.endswith(".azw") or file.endswith(".azw3"):
        dest_path = pdf_folder
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        move_file(src_path, dest_path)
    elif file.endswith(".exe") or file.endswith(".dmg") or file.endswith(".deb") or file.endswith(".rpm") or file.endswith(".msi"):
        dest_path = program_folder
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        move_file(src_path, dest_path)


   
