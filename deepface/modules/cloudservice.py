from flask import Flask, jsonify
import cloudinary
import cloudinary.api
import cloudinary.uploader
import os
import glob
import requests
from dotenv import load_dotenv
from deepface.commons.logger import Logger

logger = Logger(module="modules/cloudservice.py")

load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)


def fetch_cloudinary_images(folder_name):

    resources = []

    res = cloudinary.api.resources(type='upload',  resource_type='image', prefix=f'mafqoud/images/{folder_name}')
    resources.extend(res.get('resources', []))
    return resources

def download_image(url, local_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            for chunk in response:
                file.write(chunk)

def sync_folder(folder_name, local_dir):
    cloudinary_images = fetch_cloudinary_images(folder_name)
    cloudinary_urls = {img['secure_url']: img['public_id'] for img in cloudinary_images}

    # Download new images and track downloaded image paths
    downloaded_paths = []
    for img in cloudinary_images:
        url = img['secure_url']
        public_id = img['public_id']
        file_name = url.split('/')[-1]  # Get the actual file name
        local_path = os.path.join(local_dir, file_name)
        
        
        if not os.path.exists(local_path):
            download_image(url, local_path)
        downloaded_paths.append(local_path)
    
    # Remove old images
    local_images = [os.path.join(local_dir, f) for f in os.listdir(local_dir) if os.path.isfile(os.path.join(local_dir, f))]
    for local_path in local_images:
        if local_path not in downloaded_paths:
            os.remove(local_path)

def delete_pkl_files(directory):
    """Delete all .pkl files in the specified directory."""
    pkl_files = glob.glob(os.path.join(directory, '*.pkl'))
    for pkl_file in pkl_files:
        os.remove(pkl_file)



