import os
import shutil
import time

# ==============================
# SMART FILE ORGANIZER
# ==============================

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xlsx", ".csv"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar"],
}

LOG_FILE = "log.txt"


def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")


def organize_files(folder_path):

    start = time.time()

    moved = 0
    skipped = 0

    print("\n==============================")
    print(" SMART FILE ORGANIZER ")
    print("==============================\n")

    files = os.listdir(folder_path)

    for file in files:

        source = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(source):
            continue

        extension = os.path.splitext(file)[1].lower()

        folder_found = False

        for folder, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, folder)

                os.makedirs(destination_folder, exist_ok=True)

                destination = os.path.join(destination_folder, file)

                shutil.move(source, destination)

                print(f"✓ {file}  -->  {folder}")

                write_log(f"{file} moved to {folder}")

                moved += 1
                folder_found = True
                break

        if not folder_found:

            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(source, os.path.join(other_folder, file))

            print(f"✓ {file}  -->  Others")

            write_log(f"{file} moved to Others")

            skipped += 1

    end = time.time()

    print("\n==============================")
    print(" ORGANIZATION COMPLETED ")
    print("==============================")

    print(f"Files Moved      : {moved}")
    print(f"Others Folder    : {skipped}")
    print(f"Time Taken       : {end-start:.2f} seconds")

    print("\nProject Completed Successfully!\n")


if __name__ == "__main__":

    folder = input("Enter folder path: ")

    if os.path.exists(folder):
        organize_files(folder)
    else:
        print("Invalid Folder Path!")