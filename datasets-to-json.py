import os
import json
import yaml

DATASET_DIR = "datasets"
OUTPUT_FILE = "public/data.json"

def read_all_yml_files(dataset_dir):
    all_data = []
    for fname in os.listdir(dataset_dir):
        if fname.endswith(".yml") or fname.endswith(".yaml"):
            file_path = os.path.join(dataset_dir, fname)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    content = yaml.safe_load(f)
                except Exception as e:
                    print(f"Error loading {fname}: {e}")
                    continue
            # Add filename as a new field
            if isinstance(content, dict):
                content['__filename__'] = fname
                all_data.append(content)
    return all_data

def main():
    data = read_all_yml_files(DATASET_DIR)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, indent=2, ensure_ascii=False)
    print(f"Data written to {OUTPUT_FILE} ({len(data)} datasets)")

if __name__ == "__main__":
    main()