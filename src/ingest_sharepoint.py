import os
import shutil

RAW_FOLDER = "data/raw"
SHAREPOINT_FOLDER = "data/sharepoint"

def ingest_files():
    # create sharepoint folder if doesn't exist
    os.makedirs(SHAREPOINT_FOLDER, exist_ok=True)


    # copy each file from raw to simulated sharepoint folder
    for file_name in os.listdir(RAW_FOLDER):
        raw_path = os.path.join(RAW_FOLDER, file_name)
        sharepoint_path = os.path.join(SHAREPOINT_FOLDER, file_name)


        if os.path.isfile(raw_path):
            shutil.copy(raw_path, sharepoint_path)
            print(f"Ingested '{file_name}' to SharePoint folder.")


if __name__ == "__main__":
    ingest_files()