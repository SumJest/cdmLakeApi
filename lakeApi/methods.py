import enum


class ApiMethod(enum.Enum):
    get_files = "/files"
    get_files_by_user = "/files/user/{user_name}"
    find_files = "/files/name/{file_name}"
    get_file = "/file/id/{id}"
    upload_file = "/file/id/{id}/type/{file_name}/user/{user_name}"
    delete_file = "/file/id/{id}"
