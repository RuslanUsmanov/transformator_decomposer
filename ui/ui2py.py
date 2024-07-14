import os
import re


def generate_all(path: str):
    file_names = os.listdir(f"{path}{os.sep}qt_ui")
    ui_list = []
    pattern = re.compile(r".*\.ui")

    for file_name in file_names:
        if pattern.match(file_name):
            ui_list.append(file_name)

    for file_name in ui_list:
        file_path = os.path.join(path, "qt_ui", file_name)
        file_no_extention = file_name.removesuffix(".ui")
        outpath = f"{path}{os.sep}src{os.sep}{file_no_extention}.py"
        cmd = f"pyside6-uic {file_path} > {outpath}"
        os.popen(cmd)


if __name__ == "__main__":
    generate_all(os.path.dirname(os.path.abspath(__file__)))
