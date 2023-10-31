import os
import shutil
import time

while True:
    prm_dir = input("Specify the directory: ")

    if not os.path.exists(prm_dir):
        print("The specified directory does not exist, try again.")
    else:
        break

# define the subdirectories
directories = {}
current_category = ""

with open("extensions.txt", "r") as extension_file:
    for line in extension_file:
        line = line.strip()
        if line.startswith("#"):
            # create a directory for category
            current_category = line[1:].strip()  # Remove the '#' and trim spaces
            directories[current_category] = os.path.join(prm_dir, current_category)
            if not os.path.exists(directories[current_category]):
                os.mkdir(directories[current_category])
        elif line:
            # move files to the corresponding category directory
            if current_category:
                if not os.path.exists(directories[current_category]):
                    os.mkdir(directories[current_category])
                for entry in os.scandir(prm_dir):
                    if entry.is_file():
                        file_extension = os.path.splitext(entry.name)[1].lower()
                        if file_extension == line:
                            shutil.move(entry.path, directories[current_category])

while True:
    time.sleep(120)