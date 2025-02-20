import uuid
from pydantic import ValidationError
import gradio as gr

from circumstances.class_circumstance import Circumstances
from behavior.class_behavior import Behaviors
from behavior.class_behavior_simple import BehaviorsSimple
from physical.class_physical import PhysicalAnomalies
from physical.class_physical_simple import PhysicalAnomaliesSimple
from follow_up.class_follow_up import FollowUpEvents
from classes import Report, Wounded, Dead, ImageBase64
from validation_submission.processing import (
    process_circumstance,
    process_behaviors,
    process_physical,
    process_followup,
)
from validation_submission.utils_individual import generate_random_md5
from validation_submission.resets import reset_error_box

from dotenv import load_dotenv
import os

load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv("PATH_ASSETS")
PATH_ICONS = PATH + PATH_ASSETS + "icons/"


def get_fields(data_dict, keyword):
    extract = {}
    for key, val in data_dict.items():
        if keyword in key:
            extract[key] = val
    return extract


def field_checker(data):
    img = ImageBase64.to_base64(data["image"]) if "image" in data.keys() else None
    geolocalisation = (
        data["geolocalisation"] if "geolocalisation" in data.keys() else None
    )
    specie = data["specie"] if "specie" in data.keys() else "NA"
    number = data["number"] if "specie" in data.keys() else 1
    comments = data["comments"] if "specie" in data.keys() else "NA"
    return img, geolocalisation, specie, number, comments


def validate_individual(data, error_icon, error_box, mode: str):
    error_icon, error_box = reset_error_box(error_icon, error_box)
    # data = get_json_one_individual() # TODO: This should change
    data["identifier"] = str(uuid.uuid4())
    data["image_md5"] = generate_random_md5()
    img, geolocalisation, specie, number, comments = field_checker(data)

    error_behavior = None
    error_circumstance = None
    error_followup = None
    error_physical = None
    error_individual = None
    if "wounded_state" not in data or "dead_state" not in data:
        data["wounded_state"] = "No"
        data["dead_state"] = "No"
    if (data["wounded_state"] == "Yes") or (data["dead_state"] == "Yes"):
        data_wounded_dead = data
        circumstance, error_circumstance = validate_circumstance(data_wounded_dead)
        physical, error_physical = validate_physical(data_wounded_dead, mode)
        followup, error_followup = validate_follow_up(data_wounded_dead)

        if data["wounded_state"] == "Yes":
            behavior, error_behavior = validate_behavior(data_wounded_dead, mode)
            try:
                individual = Report(
                    identifier=data["identifier"],
                    image=img,
                    image_md5=data["image_md5"],
                    geolocalisation=geolocalisation,
                    specie=specie,
                    number=number,
                    comments=comments,
                    wounded_state=data["wounded_state"],
                    wounded=Wounded(
                        circumstances=circumstance,
                        behaviors=behavior,
                        physical_anomalies=physical,
                        follow_up_events=followup,
                    ),
                    dead_state=data["dead_state"],
                )
            except ValidationError as e:
                error_individual = e

        elif data["dead_state"] == "Yes":
            try:
                individual = Report(
                    identifier=data["identifier"],
                    image=img,
                    image_md5=data["image_md5"],
                    geolocalisation=geolocalisation,
                    specie=specie,
                    number=number,
                    comments=comments,
                    wounded_state=data["wounded_state"],
                    dead_state=data["dead_state"],
                    dead=Dead(
                        circumstances=circumstance,
                        physical_anomalies=physical,
                        follow_up_events=followup,
                    ),
                )
            except ValidationError as e:
                error_individual = e
    else:
        try:
            individual = Report(
                identifier=data["identifier"],
                image=img,
                image_md5=data["image_md5"],
                geolocalisation=geolocalisation,
                specie=specie,
                number=number,
                comments=comments,
                wounded_state=data["wounded_state"],
                dead_state=data["dead_state"],
            )
        except ValidationError as e:
            error_individual = e
    if (
        error_behavior
        or error_circumstance
        or error_followup
        or error_physical
        or error_individual
    ):
        error_icon = gr.Image(
            PATH_ICONS + "supprimer.png",
            height=80,
            width=80,
            interactive=False,
            show_fullscreen_button=False,
            show_share_button=False,
            show_download_button=False,
            show_label=False,
            visible=True,
        )
        error_box = show_error(
            error_box,
            error_behavior,
            error_circumstance,
            error_followup,
            error_physical,
            error_individual,
        )
        individual = None
    else:
        error_icon = gr.Image(
            PATH_ICONS + "correct.png",
            height=80,
            width=80,
            interactive=False,
            show_fullscreen_button=False,
            show_share_button=False,
            show_download_button=False,
            show_label=False,
            visible=True,
        )
        error_box = gr.Text(
            label="ALL VALID.",
            value="Record Registered. Remember to press the CLEAR button before submitting a new record.",
            visible=True,
            elem_id="valid",
        )
    return individual, error_icon, error_box


def show_error(
    error_box,
    error_behavior,
    error_circumstance,
    error_followup,
    error_physical,
    error_individual,
):
    error_text = ""
    if error_circumstance:
        error_text += f"Error in circumstance: {error_circumstance}\n"
    if error_behavior:
        error_text += f"Error in behavior: {error_behavior}\n"
    if error_physical:
        error_text += f"Error in physical: {error_physical}\n"
    if error_followup:
        error_text += f"Error in follow-up: {error_followup}\n"
    if error_individual:
        error_text += f"Error in individual: {error_individual}\n"
    error_text += "PLEASE CORRECT THESE ERRORS BEFORE SUBMITTING."
    error_box = gr.Text(
        label="ERROR DETECTED !", value=error_text, visible=True, elem_id="error"
    )
    return error_box


#### VALIDATION FUNCTIONS
def validate_circumstance(data):
    circumstance_raw = get_fields(data, "circumstance")
    circumstance_formatted = process_circumstance(circumstance_raw)
    try:
        Circumstances.model_validate(circumstance_formatted)
        circumstances = Circumstances(**circumstance_formatted)
        error = None
    except ValidationError as e:
        error = e
        circumstances = None
    return circumstances, error


def validate_behavior(data, mode):
    behaviors_raw = get_fields(data, "behaviors")
    behaviors_formatted = process_behaviors(behaviors_raw)
    try:
        if mode == "simple":
            BehaviorsSimple.model_validate(behaviors_formatted)
            behavior = BehaviorsSimple(**behaviors_formatted)
        elif mode == "advanced":
            Behaviors.model_validate(behaviors_formatted)
            behavior = Behaviors(**behaviors_formatted)
        error = None
    except ValidationError as e:
        behavior = None
        error = e
    return behavior, error


def validate_physical(data, mode):
    physical_raw = get_fields(data, "physical")
    physical_formatted = process_physical(physical_raw)
    try:
        if mode == "simple":
            PhysicalAnomaliesSimple.model_validate(physical_formatted)
            physical = PhysicalAnomaliesSimple(**physical_formatted)
        elif mode == "advanced":
            PhysicalAnomalies.model_validate(physical_formatted)
            physical = PhysicalAnomalies(**physical_formatted)
        error = None
    except ValidationError as e:
        physical = None
        error = e
    return physical, error


def validate_follow_up(data):
    followup_raw = get_fields(data, "followup")
    followup_formatted = process_followup(followup_raw)
    try:
        FollowUpEvents.model_validate(followup_formatted)
        followup = FollowUpEvents(**followup_formatted)
        error = None
    except ValidationError as e:
        followup = None
    return followup, error
