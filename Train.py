
# from deepface import DeepFace
# import os
# models = [
#     "VGG-Face",
#     "Facenet",
#     "Facenet512",
#     "OpenFace",
#     "DeepFace",
#     "DeepID",
#     "ArcFace",
#     "Dlib",
#     "SFace",
# ]

# metrics = ["cosine", "euclidean", "euclidean_l2"]

# backends = [
#     'opencv',
#     'ssd',
#     'dlib',
#     'mtcnn',
#     'retinaface',
#     'mediapipe',
#     'yolov8',
#     'yunet',
#     'fastmtcnn',
# ]

# # df = DeepFace.find(img_path='F:/projects/python/mafqoud/dataset/missing_people/m0.jpg'
# #                     , db_path='F:/projects/python/mafqoud/dataset/founded_people'
# #                     , enforce_detection = True
# #                     , model_name = models[2]
# #                     , distance_metric = metrics[2]
# #                     , detector_backend = backends[3])

# DeepFace.stream(db_path = "F:/deepface")

# base_dir = os.path.abspath(os.path.dirname(__file__))
# # base_dir = "f:\\"
# founded_dir = os.path.join(base_dir, 'mafqoud', 'images', 'founded_people')
# def get_main_directory():
#     path = os.path.abspath(__file__)
#     drive, _ = os.path.splitdrive(path)
#     if not drive.endswith(os.path.sep):
#         drive += os.path.sep
#     return drive

# base_dir = get_main_directory()
# missing_dir = os.path.join(base_dir, 'mafqoud', 'images', 'missing_people')
# print(missing_dir)

# print(base_dir)
# print(missing_dir)
# print(founded_dir)