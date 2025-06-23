import os
import pandas as pd

STAGING_FOLDER = "data/staging"
PROCESSED_FOLDER = "data/processed"
FINAL_FOLDER = "data/final"

def clean_and_transform():
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    os.makedirs(FINAL_FOLDER, exist_ok=True)

    all_dfs = []

    for file in os.listdir(STAGING_FOLDER):
        if file.endswith(".csv"):
            file_path = os.path.join(STAGING_FOLDER, file)
            df = pd.read_csv(file_path)


            # drop rows with any missing values
            df = df.dropna()

            # optionally, add a unique ID if needed
            if "ride_id" not in  df.columns:
                df["ride_id"] = ["RIDE" + str(i).zfill(4) for i in range(len(df))]

            all_dfs.append(df)

    if not all_dfs:
        print("NO CSV files found in staging folder.")
        return
    

    combined_df = pd.concat(all_dfs, ignore_index=True)

    # save to processed
    processed_path = os.path.join(PROCESSED_FOLDER, "processed.csv")
    combined_df.to_csv(processed_path, index=False)


    # save to final output
    final_path = os.path.join(FINAL_FOLDER, "final_output.csv")
    combined_df.to_csv(final_path, index=False)

    print(f"Transformation complete. Final file saved to : {final_path}")

if __name__ == "__main__":
    clean_and_transform()