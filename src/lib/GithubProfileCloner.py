#!/bin/python3

# Built with Love.
# Author: ropydev
# Github: https://github.com/ropydev/Github-Profile-Cloner
# v1.0 - (16/08/2026)

import requests
import subprocess
import os
import shutil

# Colors
Red = "\033[1m\033[31m"
Green = "\033[1m\033[32m"
Blue = "\033[36m"
Reset = "\033[0m"

clonePath = os.path.join(os.path.expanduser("~"), "GithubProfileCloner")


def getRepos(owner: str) -> list:
    api = "https://api.github.com"
    per_page = 100
    page = 1
    repos = []
    headers = {"Accept": "application/vnd.github.v3+json"}
    while True:
        resp = requests.get(
            f"{api}/users/{owner}/repos",
            headers=headers,
            params={"per_page": per_page, "page": page, "type": "public"},
            timeout=30,
        )

        if resp.status_code == 404:
            raise ValueError(f"Usuario '{owner}' no existe.")
        resp.raise_for_status()

        data = resp.json()
        if not isinstance(data, list):
            raise RuntimeError(f"Respuesta inesperada: {data}")

        for r in data:
            repos.append(r.get("full_name"))

        link = resp.headers.get("Link", "")
        if 'rel="next"' in link:
            page += 1
            continue
        break
    return repos


def cloneMirror(repo: str, destPath: str):
    try:
        url = f"https://github.com/{repo}"
        os.makedirs(destPath, exist_ok=True)
        subprocess.run(
            [
                "git",
                "clone",
                "--mirror",
                url,
                os.path.join(destPath, repo.split("/")[1]),
            ],
            check=True,
        )
        print(
            f"{Green}[+]{Reset} Se clono con exito el repositorio https://github.com/{repo}"
        )
    except Exception as e:
        print(
            f"{Red}[!]{Reset} Ocurrio un error clonando el repositorio https://github.com/{repo}"
        )


def pushMirror(token: str, owner: str, repo: str, path: str):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {"name": repo, "private": False, "description": ""}

    urlRepo = f"https://api.github.com/repos/{owner}/{repo}"
    resp = requests.get(urlRepo, headers=headers)
    if resp.status_code == 200:
        deleteResp = requests.delete(urlRepo, headers=headers)
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 201:
        print(f"{Green}[+]{Reset} Repositorio creado con éxito")
        clone_url = resp.json()["clone_url"]
    else:
        print("Error al crear repo:", resp.json())
        exit()
    os.chdir(path)
    subprocess.run(["git", "remote", "remove", "origin"], check=False)
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            f"https://{owner}:{token}@github.com/{owner}/{repo}.git",
        ],
        check=True,
    )
    subprocess.run(["git", "push", "--mirror", "origin"], check=True)


def updateInfo(token, owner):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(f"https://api.github.com/users/{owner}")
    userData = resp.json()
    bio = f"{userData.get("bio")}\n\nCloned by Github-Profile-Cloner\n(https://github.com/ropydev/Github-Profile-Cloner)"
    data = {
        "name": userData.get("name"),
        "bio": userData.get("bio"),
        "blog": userData.get("blog"),
        "company": userData.get("company"),
        "location": userData.get("location"),
        "email": userData.get("email"),
        "hireable": userData.get("hireable"),
        "twitter_username": userData.get("twitter_username"),
    }
    resp = requests.patch(url, headers=headers, json=data)
    if resp.status_code == 200:
        print(f"{Green}[+]{Reset} Se cambio correctamente la info del perfil.")
    else:
        print(
            f"{Red}[!]{Reset} Ocurrio un error inesperado y desconocido ({resp.status_code})"
        )


def cloneProfile(owner, folder, token, user):
    try:
        updateInfo(token, owner)
        if os.path.exists(clonePath):
            shutil.rmtree(clonePath)
        repos = getRepos(owner)
        for repo in repos:
            cloneMirror(repo, folder)
            repoName = repo.split("/")[1]
            pushMirror(
                token, user, repoName, os.path.join(clonePath, repo.split("/")[1])
            )
        print(
            f"{Green}[+]{Reset} Todos los repositorios fueron clonados a la carpeta {folder}"
        )
        return {"error": "false"}
    except Exception as e:
        print(f"{Red}[!]{Reset} Ocurrio un error: {e}")
        return {"error": "true", "msg": str(e)}
