import user_list


def create(userlist, username, main_dir="./"):
    new_user_id = int(list(userlist.keys())[-1]) + 1
    userlist[str(new_user_id)] = username
    user_list.save(userlist, main_dir=main_dir)

    return new_user_id, userlist


def delete(userlist: dict, user_id,main_dir="./"):
    user_deleted = False
    for i in userlist.keys():
        if user_id == i:
            userlist.pop(i)
            user_deleted = True
    user_list.save(userlist, main_dir=main_dir)

    return user_deleted


def select(userlist, user_id):
    user_selected = False
    username = "Default"
    for i in userlist.keys():
        if i == user_id:
            username = userlist[i]
            user_selected = True
    return username, user_selected
