from datasets import load_dataset, DownloadMode
import json
import os
from huggingface_hub import HfApi, hf_hub_download

dataset_id = "SDSC/digiwild-dataset"
token = os.getenv("HUGGINGFACE_TOKEN")

# Initialize API client
api = HfApi(token=token)

# Load all metadata files
files = api.list_repo_files(dataset_id, repo_type="dataset")
json_files = [file for file in files if file.endswith(".json")]

# Load the metadata compilation
try:
    data_files = "data/train-00000-of-00001.parquet"
    metadata = load_dataset(dataset_id, data_files=data_files)
    # Add new json entries to dataset
    for file in json_files:
        file = hf_hub_download(repo_id=dataset_id, filename=file, repo_type="dataset")
        with open(file, "r") as f:
            new = json.load(f)
        if not (new["image_md5"] in metadata["train"]["image_md5"]):
            metadata["train"] = metadata["train"].add_item(new)
except:
    metadata = load_dataset(dataset_id, data_files=json_files)


metadata.push_to_hub(dataset_id, token=token)
