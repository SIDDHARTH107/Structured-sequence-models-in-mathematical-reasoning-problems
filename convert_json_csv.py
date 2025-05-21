import os
import json
import pandas as pd

FOLDER_PATH = "data"  # Folder with my JSON files
OUTPUT_CSV = "merged_output.csv"

all_data = []

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith(".json"):
        file_path = os.path.join(FOLDER_PATH, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                clean_data = {}
                for k, v in data.items():
                    clean_key = k.strip().replace(";", "")
                    clean_data[clean_key] = v

                all_data.append(clean_data)

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

df = pd.DataFrame(all_data)
df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')

print(f"Successfully saved {len(df)} records to '{OUTPUT_CSV}'")
