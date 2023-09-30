import json
import os


# Create users to do list.
def todo_create(fullpath):
    with open(fullpath, "w") as file:
        default_list = []
        json.dump(default_list, file, indent=4)


# Load to do list at the filepath.
def todo_load(fullpath):
    with open(fullpath, "r") as file:
        data = json.load(file)
    return data


# Saves users to do list.
def todo_save(todo, fullpath):
    with open(fullpath, "w") as file:
        json.dump(todo, file, indent=4)
        changes_saved = True
    return changes_saved


# Initialize users to do list (load/create).
def todo_init(username, main_dir="./"):
    fullpath = f"{main_dir}{username}.json"
    exists = os.path.isfile(fullpath)
    if not exists:
        todo_create(fullpath)
    data = todo_load(fullpath)
    return data


def to_do_add(item, todo, fullpath):
    if len(todo) == 0:
        item_id = 0
    else:
        item_id = int(todo[-1]["item_id"]) + 1  # generates an ID that is greater than last item on the to-do list
    status = "todo"
    entry = {"item_id": item_id, "status": status, "item": item}
    todo.append(entry)
    todo_save(todo, fullpath)
    return todo


# Remove items from list
def to_do_remove(item_id, todo, fullpath):
    item_removed = False
    for i in todo:
        if i["item_id"] == int(item_id):
            todo.remove(i)
            todo_save(todo, fullpath)
            item_removed = True
    return todo, item_removed


# Mark item as done
def to_do_mark_done(item_id, todo, fullpath):
    item_marked_done = False
    for i in todo:
        if i["item_id"] == int(item_id):
            i["status"] = "done"
            todo_save(todo, fullpath)
            item_marked_done = True
    return todo, item_marked_done


# Edit item in the list
def to_do_edit(item_id, item, todo, fullpath):
    item_edited = False
    for i in todo:
        if i["item_id"] == item_id:
            i["item"] = item
            todo_save(todo, fullpath)
            item_edited = True
    return todo, item_edited
