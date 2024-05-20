from flask import Blueprint, request , jsonify
from deepface.api.src.modules.core import service
from deepface.commons.logger import Logger
from deepface.commons.path import path
import json

logger = Logger(module="api/src/routes.py")

blueprint = Blueprint("routes", __name__)


@blueprint.route("/")
def home():
    return "<h1>Welcome to DeepFace API!</h1>"


@blueprint.route("/represent", methods=["POST"])
def represent():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img_path = input_args.get("img") or input_args.get("img_path")
    if img_path is None:
        return {"message": "you must pass img_path input"}

    model_name = input_args.get("model_name", "VGG-Face")
    detector_backend = input_args.get("detector_backend", "opencv")
    enforce_detection = input_args.get("enforce_detection", True)
    align = input_args.get("align", True)

    obj = service.represent(
        img_path=img_path,
        model_name=model_name,
        detector_backend=detector_backend,
        enforce_detection=enforce_detection,
        align=align,
    )

    logger.debug(obj)

    return obj


@blueprint.route("/verify", methods=["POST"])
def verify():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img1_path = input_args.get("img1") or input_args.get("img1_path")
    img2_path = input_args.get("img2") or input_args.get("img2_path")

    if img1_path is None:
        return {"message": "you must pass img1_path input"}

    if img2_path is None:
        return {"message": "you must pass img2_path input"}

    model_name = input_args.get("model_name", "VGG-Face")
    detector_backend = input_args.get("detector_backend", "opencv")
    enforce_detection = input_args.get("enforce_detection", True)
    distance_metric = input_args.get("distance_metric", "cosine")
    align = input_args.get("align", True)

    verification = service.verify(
        img1_path=img1_path,
        img2_path=img2_path,
        model_name=model_name,
        detector_backend=detector_backend,
        distance_metric=distance_metric,
        align=align,
        enforce_detection=enforce_detection,
    )

    logger.debug(verification)

    return verification


@blueprint.route("/analyze", methods=["POST"])
def analyze():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img_path = input_args.get("img") or input_args.get("img_path")
    if img_path is None:
        return {"message": "you must pass img_path input"}

    detector_backend = input_args.get("detector_backend", "opencv")
    enforce_detection = input_args.get("enforce_detection", True)
    align = input_args.get("align", True)
    actions = input_args.get("actions", ["age", "gender", "emotion", "race"])

    demographies = service.analyze(
        img_path=img_path,
        actions=actions,
        detector_backend=detector_backend,
        enforce_detection=enforce_detection,
        align=align,
    )

    logger.debug(demographies)

    return demographies

@blueprint.route("/find", methods=["POST"])
def find():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img_name = input_args.get("img") or input_args.get("img_name")
    db_path = input_args.get("db_path")
    img_type = input_args.get("img_type")
    model_name = input_args.get("model_name", "Facenet512")
    detector_backend = input_args.get("detector_backend", "yolov8")
    enforce_detection = input_args.get("enforce_detection", True)
    distance_metric = input_args.get("distance_metric", "euclidean_l2")
    align = input_args.get("align", True)

    if img_name is None:
        return {"message": "you must pass img1_path input"}

    if db_path is None:
        dataset_path = os.path.join(path.get_parent_path(), 'dataset')
        if img_type == "missing_person":
            img_path = os.path.join(dataset_path, 'missing_people', img_name)
            db_path = os.path.join(dataset_path, 'founded_people')
        elif img_type == "founded_people":
            img_path = os.path.join(dataset_path, 'founded_people', img_name)
            db_path = os.path.join(dataset_path, 'missing_people')

    results = service.find(
        img_path=img_path,
        db_path=db_path,
        model_name=model_name,
        detector_backend=detector_backend,
        distance_metric=distance_metric,
        align=align,
        enforce_detection=enforce_detection,
    )

    # Calculate similarity_percentage for each row
    results[0]['similarity_percentage'] =100 - ((results[0]['distance'] / results[0]['threshold']) * 100)

    data = []
    for _, row in results[0].iterrows():
        data.append({
            "identity": row['identity'],
            "similarity_percentage": row['similarity_percentage']
        })

    json_data = json.dumps(data, indent=4)

    logger.debug(json_data)
    return json_data
