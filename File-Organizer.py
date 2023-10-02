import os
import shutil


def move_file(src_path, dest_path, file):
    # Check if the file exists
    if os.path.exists(src_path):
        # Check if the destination path exists
        if not os.path.exists(dest_path):
            # Move the file from the source path to the destination path
            shutil.move(src_path, dest_path)
        else:
            # If the destination path exists, print the file name and the destination path
            print(f"\nFile: {file} , already exists in {dest_path}\n")
            os.remove(src_path)


def organize_files(download_folder):
    # Set the paths for the destination folders
    video_folder = os.path.join(download_folder, "video")
    audio_folder = os.path.join(download_folder, "Music")
    image_folder = os.path.join(download_folder, "image")
    pdf_folder = os.path.join(download_folder, "Compressed")
    document_folder = os.path.join(download_folder, "Documents")
    code_folder = os.path.join(download_folder, "code")
    zip_folder = os.path.join(download_folder, "zip")
    other_folder = os.path.join(download_folder, "other")

    # Create the destination folders if they don't exist
    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(audio_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(pdf_folder, exist_ok=True)
    os.makedirs(document_folder, exist_ok=True)
    os.makedirs(code_folder, exist_ok=True)
    os.makedirs(zip_folder, exist_ok=True)
    os.makedirs(other_folder, exist_ok=True)

    # Get the list of files in the download folder
    files = os.listdir(download_folder)

    for file in files:
        src_path = os.path.join(download_folder, file)
        if os.path.isfile(src_path):  # Check if the current item is a file
            if file.endswith((".mp4", ".mkv", ".wmv", ".mov", ".flv", ".3gp", ".m4v", ".webm", ".vob", ".mpg", ".mpeg", ".avi")):
                dest_path = video_folder
            elif file.endswith((".mp3", ".flac", ".m4a", ".wma", ".aac", ".wav", ".ogg", ".alac", ".aiff")):
                dest_path = audio_folder
            elif file.endswith((".jpg", ".png", ".gif", ".ico", ".webp", ".jpeg", ".svg", ".bmp", ".tif")):
                dest_path = image_folder
            elif file.endswith((".pdf", ".epub", ".mobi", ".azw", ".djvu", ".prc", ".ibooks", ".lit")):
                dest_path = pdf_folder
            elif file.endswith((".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".key", ".odp", ".xls", ".xlsx", ".csv", ".ods")):
                dest_path = document_folder
            elif file.endswith((".py", ".java", ".cpp", ".html", ".css", ".js", ".php", ".rb", ".go", ".swift", ".kt", ".rs", ".ts", ".cs", ".json", ".xml", ".sh", ".yml", ".sql")):
                dest_path = code_folder
            elif file.endswith((".zip", ".rar", ".7z", ".tar", ".gz", ".bz2")):
                dest_path = zip_folder
            else:
                dest_path = other_folder
            if os.path.exists(dest_path):
                # If the file already exists in the destination folder, rename it
                filename, extension = os.path.splitext(file)
                new_filename = f"{filename}{extension}"
                dest_path = os.path.join(dest_path, new_filename)
            move_file(src_path, dest_path, file)


# Set the path for the download folder
download_folder = "C:\\Users\\isuru\\Downloads"

# Call the function to organize the files in the download folder
organize_files(download_folder)
