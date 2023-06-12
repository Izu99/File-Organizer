import os
import shutil
import sched
import time


def move_file(src_path, dest_path):
    # Check if the file has finished downloading
    while not os.path.exists(src_path):
        pass

    # Move the file from the download folder to the desired location
    filename = os.path.basename(src_path)
    new_dest_path = os.path.join(dest_path, filename)

    # Rename the file if it already exists at the destination path
    i = 1
    while os.path.exists(new_dest_path):
        name, extension = os.path.splitext(filename)
        new_filename = f"{name} ({i}){extension}"
        new_dest_path = os.path.join(dest_path, new_filename)
        i += 1

    shutil.move(src_path, new_dest_path)


# Set the paths for the download folder and the destination folders
download_folder = "C:\\Users\\isuru\\Downloads"
audio_folder = "C:\\Users\\isuru\\Downloads\\audio"
image_folder = "C:\\Users\\isuru\\Downloads\\image"
pdf_folder = "C:\\Users\\isuru\\Downloads\\pdf"
program_folder = "C:\\Users\\isuru\\Downloads\\program"
video_folder = "C:\\Users\\isuru\\Downloads\\video"
zip_folder = "C:\\Users\\isuru\\Downloads\\zip"
other_folder = "C\\Users\\isuru\\Downloads\\other"

# Get the list of files in the download folder
files = os.listdir(download_folder)


# Iterate over the list of files and move them to the appropriate destination folder
for file in files:
    src_path = os.path.join(download_folder, file)
    if os.path.isfile(src_path):  # Check if the current item is a file
        if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".wmv") or file.endswith(".mov") or file.endswith(".flv") or file.endswith(".3gp") or file.endswith(".m4v") or file.endswith(".webm") or file.endswith(".vob") or file.endswith(".mpg") or file.endswith(".mpeg"):
            dest_path = video_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)
        elif file.endswith(".mp3") or file.endswith(".flac") or file.endswith(".m4a") or file.endswith(".wma") or file.endswith(".aac") or file.endswith(".wav") or file.endswith(".ogg") or file.endswith(".alac") or file.endswith(".aiff"):
            dest_path = audio_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)
        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".ico") or file.endswith(".webp") or file.endswith(".jpeg") or file.endswith(".svg") or file.endswith(".bmp") or file.endswith(".tif"):
            dest_path = image_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)
        elif file.endswith(".exe") or file.endswith(".dmg") or file.endswith(".deb") or file.endswith(".rpm") or file.endswith(".msi") or file.endswith(".apk") or file.endswith(".jar"):
            dest_path = program_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)
        elif file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".tar") or file.endswith(".gz") or file.endswith(".bz2"):
            dest_path = zip_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)
        else:
            dest_path = other_folder
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            move_file(src_path, dest_path)

