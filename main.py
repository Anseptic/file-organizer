import os
import shutil
from loguru import logger
import time

# logger configuration
log_file = "file_organizer.log"
logger.add(log_file)

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
                            try:
                                shutil.move(entry.path, directories[current_category])
                                logger.info(f"Moved {entry.name} to {current_category}")
                            except Exception as e:
                                logger.error(f"Error moving {entry.name}: {e}")

    # logging even if nothing is moved
    logger.info("Scanned directory for files.")
    if not any(os.scandir(prm_dir)):
        logger.info("No files were moved.")

while True:
    # 10 minute (600 sec) timer
    time.sleep(600)