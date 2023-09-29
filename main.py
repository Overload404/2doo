# Import any necessary modules or libraries
import json
import os

# variables
main_dir = "./"
user_selected = False
msg = ""


# check if user file exists
def load_create_user_json(path="userlist.json", user="Default"):
    fullpath = f"{main_dir}{path}"
    exists = os.path.isfile(fullpath)
    if not exists:
        with open(fullpath, "w") as file:
            default_userlist = {0: user}
            json.dump(default_userlist, file, indent=4)
    with open(fullpath, "r") as file:
        data = json.load(file)
    return data


# Create a user
def create_user(userlist, path="userlist.json", username="Default"):
    fullpath = f"{main_dir}{path}"
    with open(fullpath, "w") as file:
        new_user_id = int(list(userlist.keys())[-1]) + 1
        userlist[new_user_id] = username
        json.dump(userlist, file, indent=4)


# Select a user
def select_user(userlist):
    global user_selected
    print("Username options: ")
    print("N - Create new user")
    for i in userlist.keys():
        print(f"{i} - {userlist[i]}")
    user_select = input("Select from above: ")
    if user_select == "N":
        username = ask_username()
        create_user(username=username, userlist=userlist)
    elif user_select not in userlist.keys() and user_select != "N":
        print("Not an option. Please select from above: ")
        user_select = input("Select from above: ")
    else:
        user_selected = True
    return user_select


def load_create_todo_json(username):
    fullpath = f"{main_dir}{username}.json"
    exists = os.path.isfile(fullpath)
    if not exists:
        with open(fullpath, "w") as file:
            default_userlist = []
            json.dump(default_userlist, file, indent=4)
    with open(fullpath, "r") as file:
        data = json.load(file)
    return data


# Write changes to To-Do list
def save_to_do_changes(username, to_do_list):
    fullpath = f"{main_dir}{username}.json"
    with open(fullpath, "w") as file:
        json.dump(to_do_list, file, indent=4)


# Asks for the username
def ask_username():
    username = input("Enter your username: ")
    return username


# Print out to do list into console
def to_do_print(username):
    to_do_list = load_create_todo_json(username)
    print(f"User: {username}")
    if len(to_do_list) > 0:
        print('Your to-do list: ')
        for i in to_do_list:
            item_id = i["item_id"]
            status = i["status"]
            item = i["item"]
            print(f"{item_id} - {item} - {status}")
    else:
        print("Nothing to do. Add some items.")
    print("##########################################")


# Add items
def to_do_add(username):
    global msg
    to_do_list = load_create_todo_json(username)
    if len(to_do_list) == 0:
        item_id = 0
    else:
        item_id = int(to_do_list[-1]["item_id"]) + 1  # generates an ID that is greater than last item on the to-do list
    item = input("Enter an item: ")
    status = "todo"
    entry = {"item_id": item_id, "status": status, "item": item}
    to_do_list.append(entry)
    save_to_do_changes(username, to_do_list)
    msg = "Item created."


# Remove items
def to_do_remove(username):
    global msg
    to_do_list = load_create_todo_json(username)
    
    if len(to_do_list) == 0:
        msg = "Nothing to remove. The list is empty. "
    else:
        item_id = input("Enter an ID to remove: ")
        existing_ids = []
        for i in to_do_list:
            existing_ids.append(i["item_id"])
        if not item_id.isnumeric():
            msg = "Item ID must be a number."
        elif item_id.isnumeric() and int(item_id) not in existing_ids:
            msg = "There's no item with this ID."
        elif item_id.isnumeric() and int(item_id) in existing_ids:
            for i in to_do_list:
                if i["item_id"] == int(item_id):
                    msg = "Item removed."
                    to_do_list.remove(i)
                    save_to_do_changes(username, to_do_list)
        else:
            msg = "There's no item with this ID."


# Mark items as done
def to_do_mark_done(username):
    global msg
    to_do_list = load_create_todo_json(username)
    if len(to_do_list) == 0:
        msg = "Nothing to mark. The list is empty."
    else:
        item_id = input("Enter an ID to mark as done: ")
        existing_ids = []
        for i in to_do_list:
            existing_ids.append(i["item_id"])
        if not item_id.isnumeric():
            msg = "Item ID must be a number."
        elif item_id.isnumeric() and int(item_id) not in existing_ids:
            msg = "There's no item with this ID."
        elif item_id.isnumeric() and int(item_id) in existing_ids:
            for i in to_do_list:
                if i["item_id"] == int(item_id):
                    msg = "Item marked as done."
                    i["status"] = "done"
                    save_to_do_changes(username, to_do_list)
        else:
            msg = "There's no item with this ID."

    save_to_do_changes(username, to_do_list)


def to_do_replace():
    pass


# Main loop for working with To Do list
def to_do_loop(username):
    os.system('cls')
    to_do_print(username)
    print(msg+" What would you like to do: ")
    print("1 - Add new item \n2 - Mark item as done \n3 - Remove item \n4 - Exit")
    to_do_action = input()
    if to_do_action == "1":
        to_do_add(username)
    elif to_do_action == "2":
        to_do_mark_done(username)
    elif to_do_action == "3":
        to_do_remove(username)
    elif to_do_action == "4":
        global user_selected
        user_selected = False
    else:
        print("Select an action.")


def main():
    os.system('cls')
    print("Welcome to 2doo")
    print()
    while not user_selected:
        userlist = load_create_user_json()
        user_select = select_user(userlist)
        username = userlist[user_select]
    while user_selected:
        to_do_loop(username)


# Check if this script is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
