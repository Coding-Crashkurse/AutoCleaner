import getpass
import os
from datetime import datetime, timedelta

class InitApp:
    def __init__(self):
        self.folder = f"C:/Users/{getpass.getuser()}/Autoclean"
        self.file = "delete_folders.txt"
        self.full_path = os.path.join(self.folder, self.file)
        self.observation_path = []
        self.init_file()
        self.bat_path = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
        self.bat_file = self.bat_path + '\\' + "open.bat"

    def init_file(self) -> None:
        if not os.path.isdir(self.folder):
            os.makedirs(self.folder)

        if not os.path.exists(self.full_path):
            with open(self.full_path, "w") as f:
                f.write("C:/Users/User/Downloads")

    def get_content(self) -> list[dict]:
        observation_path = []

        with open(self.full_path, "r") as file:
            content = file.readlines()
            lines = [line.rstrip() for line in content]

        for line in lines:
            observation_path.append({"path": line})
        return observation_path

    def get_all_files(self) -> list[str]:
        all_files = []
        content_dict = self.get_content()
        for file in content_dict:
            path = file.get("path")
            files = os.listdir(path)
            # files = [file for file in files if file.endswith(".txt")]
            full_paths = [os.path.join(path, file) for file in files]
            all_files.extend(full_paths)
        return all_files

    def get_time_stamps(self, files: list[str]):
        timestamps = []
        for file in files:
            timestamp = os.stat(file).st_mtime
            timestamps.append(datetime.fromtimestamp(timestamp))
        return timestamps

    def write_into_startup(self):
        newname = os.path.basename(__file__).replace(".py", ".exe")
        file_path = os.path.join(os.getcwd(), newname)
        with open(self.bat_file, "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)

app = InitApp()

if not os.path.exists(app.bat_file):
    app.write_into_startup()
else:
    files = app.get_all_files()
    timestamps = app.get_time_stamps(files)
    for file, timestamp in zip(files, timestamps):
        if datetime.now() - timedelta(days=os.environ.get("TIMEDELTA", 7)) > timestamp:
            if not os.path.isdir(file):
                os.remove(file)
