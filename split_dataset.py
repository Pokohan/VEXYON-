import glob
import os
import pandas as pd

EXCLUDED_FILES = {"dataset_merged.csv", "train.csv", "test.csv"}

def split_dataset(csv_dir=".", train_path="train.csv", test_path="test.csv"):
    os.chdir(csv_dir)

    csv_files = sorted(
        f for f in glob.glob("*.csv")
        if os.path.basename(f) not in EXCLUDED_FILES
    )

    if not csv_files:
        print("Erreur : Aucun fichier CSV source trouvé dans le dossier.")
        return

    train_dfs, test_dfs = [], []

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if df.empty or len(df) < 2:
                continue

            split_idx = int(len(df) * 0.8)
            if split_idx == 0:
                split_idx = 1

            train_dfs.append(df.iloc[:split_idx])
            test_dfs.append(df.iloc[split_idx:])
        except Exception as e:
            print(f"Impossible de lire {file} : {e}")

    if not train_dfs or not test_dfs:
        print("Erreur : Impossible de générer les jeux de données (données insuffisantes).")
        return

    train_df = pd.concat(train_dfs, ignore_index=True)
    test_df = pd.concat(test_dfs, ignore_index=True)

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"✓ train.csv ({len(train_df)} lignes) et test.csv ({len(test_df)} lignes) générés avec succès.")

if __name__ == "__main__":
    split_dataset()
