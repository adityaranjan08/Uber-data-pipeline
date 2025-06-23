from fileinput import filename
import os
import shutil
from datetime import datetime

SHAREPOINT_FOLDER = "data/sharepoint"
STAGING_FOLDER = "data/staging"

def stage_files():
    os.makedirs(STAGING_FOLDER,exist_ok=True)
    files_staged = 0

    for file_name in os.listdir(SHAREPOINT_FOLDER):
        source_path = os.path.join(SHAREPOINT_FOLDER, file_name)

        if os.path.isfile(source_path):
            # generate timestamped name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
            staged_name = f"{timestamp}_{file_name}"
            dest_path = os.path.join(STAGING_FOLDER, staged_name)

            shutil.copy(source_path, dest_path)
            print(f"Staged: {file_name} as {staged_name}")
            files_staged += 1

            if files_staged == 0:
                print("No files found in sharepoint folder to stage.")


if __name__ == "__main__":
    stage_files()