import os
import pandas as pd
import sqlite3

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
            print(f"Reading: {file_path}")
            df = pd.read_csv(file_path)
            df = df.dropna()

            if "ride_id" not in df.columns:
                df["ride_id"] = ["RIDE" + str(i).zfill(4) for i in range(len(df))]

            all_dfs.append(df)

    if not all_dfs:
        print("NO CSV files found in staging folder.")
        return

    combined_df = pd.concat(all_dfs, ignore_index=True)
    print("Combined DataFrame created.")

    processed_path = os.path.join(PROCESSED_FOLDER, "processed.csv")
    final_path = os.path.join(FINAL_FOLDER, "final_output.csv")

    combined_df.to_csv(processed_path, index=False)
    combined_df.to_csv(final_path, index=False)

    print(f"Transformation complete. Final file saved to : {final_path}")

    # Save to SQLite database
    try:
        print("Attempting to save to SQLite...")
        conn = sqlite3.connect("data/uber_rides.db")
        combined_df.to_sql("uber_rides", conn, if_exists='replace', index=False)
        conn.close()
        print("Data also saved to SQLite: data/uber_rides.db")
    except Exception as e:
        print(f" Error saving to SQLite: {e}")

if __name__ == "__main__":
    clean_and_transform()
