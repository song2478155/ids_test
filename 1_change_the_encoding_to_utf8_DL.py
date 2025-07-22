import os
import codecs
import pandas as pd
import numpy as np

def _process(df):
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    return df

def _renaming_class_label(df: pd.DataFrame):
    labels = {
        "Web Attack \x96 Brute Force": "Web Attack-Brute Force",
        "Web Attack \x96 XSS": "Web Attack-XSS",
        "Web Attack \x96 Sql Injection": "Web Attack-Sql Injection"
    }
    for old_label, new_label in labels.items():
        df.Label.replace(old_label, new_label, inplace=True)

def _to_utf8(filename: str, encoding="latin1", blocksize=1048576):
    tmpfilename = filename + ".tmp"
    with codecs.open(filename, "r", encoding) as source:
        with codecs.open(tmpfilename, "w", "utf-8") as target:
            while True:
                contents = source.read(blocksize)
                if not contents:
                    break
                target.write(contents)
    os.rename(tmpfilename, filename)

DIR_PATH = "/data2/msbaek_dir/0_datasets/CIC-IDS-2017/CSVs/MachineLearningCVE"
OUT_DIR_PATH = "/home/msbaek/test/8_csv"

# Ensure output directory exists
os.makedirs(OUT_DIR_PATH, exist_ok=True)

csv_files = [
    "Monday-WorkingHours.pcap_ISCX.csv",
    "Tuesday-WorkingHours.pcap_ISCX.csv",
    "Wednesday-workingHours.pcap_ISCX.csv",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
]

print("=== Starting preprocessing for each file ===")
for csv_f in csv_files:
    file_name = os.path.join(DIR_PATH, csv_f)
    print(f"\nProcessing file: {file_name}")

    # Step 1: Convert to UTF-8
    print(" - Converting encoding to UTF-8...")
    _to_utf8(file_name)

    # Step 2: Load CSV and remove all-NaN rows
    print(" - Loading CSV and removing rows with only NaN values...")
    df = pd.read_csv(file_name, skipinitialspace=True, on_bad_lines='skip')
    nan_rows = df[df.isna().all(axis=1)].shape[0]
    print(f"   > {nan_rows} NaN-only rows removed.")
    df = df[~ df.isna().all(axis=1)]

    # Step 3: Rename corrupted class labels
    print(" - Renaming corrupted class labels...")
    _renaming_class_label(df)

    # Step 4: Replace inf/nan values and fill missing with 0
    print(" - Processing NaN/inf values...")
    df = _process(df)

    # Save cleaned file
    df.to_csv(file_name, index=False)
    print(" - File saved after cleaning.")

print("\n=== Merging all cleaned files into a single DataFrame ===")
df = [pd.read_csv(os.path.join(DIR_PATH, f), skipinitialspace=True) for f in csv_files]
df = pd.concat(df, ignore_index=True)

print("\n=== Label distribution before filtering ===")
print(df.Label.value_counts())

# Optional filtering
filtering = True
if filtering:
    print("\n=== Filtering labels with less than 1000 samples ===")
    label_counts = df.Label.value_counts()
    labels_to_keep = label_counts[label_counts > 1000].index
    df = df[df.Label.isin(labels_to_keep)].reset_index(drop=True)
    print("Filtered label distribution:")
    print(df.Label.value_counts())

    save_path = os.path.join(OUT_DIR_PATH, "MachineLearningCVE_f.csv")
    print(f"Saving filtered dataset to: {save_path}")
    df.to_csv(save_path, index=False)
else:
    save_path = os.path.join(OUT_DIR_PATH, "MachineLearningCVE.csv")
    print(f"Saving full dataset to: {save_path}")
    df.to_csv(save_path, index=False)

print("\n=== Preprocessing complete ===")

