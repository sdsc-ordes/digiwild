import json
from validation_submission.validation import validate_individual
import gradio as gr 
from huggingface_hub import HfApi
import os


def validate_save_individual(data, error_icon, error_box, mode):
    individual, error_icon, error_box = validate_individual(data, error_icon, error_box, mode)
    if individual:
        print("pushing to hugging face")
        push_to_dataset_hf(individual.model_dump())
    return individual, error_icon, error_box


def push_to_dataset_hf(individual):
    token = os.environ.get("HF_TOKEN", None)
    api = HfApi(token=token)
    import tempfile

    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump(individual, f)
    f.flush()
    f.close()
    path_in_repo = f"data/{individual['image_md5']}.json"
    # print(path_in_repo)
    # api.upload_file(
    #     path_or_fileobj=f.name,
    #     path_in_repo=path_in_repo,
    #     repo_id="SDSC/digiwild-dataset",
    #     repo_type="dataset",
    # )
