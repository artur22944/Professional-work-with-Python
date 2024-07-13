import requests


TOKEN = "token"


def create_folder_yandex(folder_name: str):

    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        headers={"Authorization": f"OAuth {TOKEN}"},
        params={"path": folder_name},
    )

    return response.status_code


def delete_folder_yandex(folder_name: str):

    response = requests.delete(
        "https://cloud-api.yandex.net/v1/disk/resources",
        headers={"Authorization": f"OAuth {TOKEN}"},
        params={"path": folder_name},
    )

    return response.status_code
