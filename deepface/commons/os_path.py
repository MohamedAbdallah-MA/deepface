import os

class os_path :
    
    def get_main_directory():
        path = os.path.abspath(__file__)
        drive, _ = os.path.splitdrive(path)
        if not drive.endswith(os.path.sep):
            drive += os.path.sep
        return drive

    def get_main_drive_directory():
        return '/content/drive/MyDrive'