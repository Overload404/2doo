import json
import os


def create(main_dir, path="userlist.json", user="Default"):
    fullpath = f"{main_dir}{path}"
    with open(fullpath, "w") as file:
        default_userlist = {0: user}
        json.dump(default_userlist, file, indent=4)


def load(main_dir, path="userlist.json"):
    fullpath = f"{main_dir}{path}"
    with open(fullpath, "r") as file:
        data = json.load(file)
    return data


def init(main_dir, path="userlist.json", user="Default"):
    fullpath = f"{main_dir}{path}"
    exists = os.path.isfile(fullpath)
    if not exists:
        create(main_dir)
    data = load(main_dir)
    return data


def save(userlist, path="userlist.json", main_dir="./"):
    fullpath = f"{main_dir}{path}"
    with open(fullpath, "w") as file:
        json.dump(userlist, file, indent=4)