#!/bin/python3

# Built with Love.
# Author: ropydev
# Github: https://github.com/ropydev/Github-Profile-Cloner
# v1.1 - (17/08/2026)

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


def cloneMirror(repo: str, destPath: str, name: str, email: str, norewrite: bool):
    try:
        url = f"https://github.com/{repo}"
        os.makedirs(destPath, exist_ok=True)
        repo_name = repo.split("/")[1]
        repo_path = os.path.join(destPath, repo_name)

        subprocess.run(
            ["git", "clone", "--mirror", url, repo_path],
            check=True,
        )
        print(f"{Green}[+]{Reset} Se clonó con éxito el repositorio https://github.com/{repo}")
        if not norewrite:
            os.chdir(repo_path)
            env_filter = (
                f'export GIT_AUTHOR_NAME="{name}"; '
                f'export GIT_AUTHOR_EMAIL="{email}"; '
                f'export GIT_COMMITTER_NAME="{name}"; '
                f'export GIT_COMMITTER_EMAIL="{email}";'
            )
            subprocess.run(["git", "filter-branch", "--env-filter", env_filter, "--", "--all"], check=True)
            print(f"{Green}[+]{Reset} Commits reescritos con autor {name} <{email}>")

    except Exception as e:
        print(f"{Red}[!]{Reset} Ocurrió un error clonando o reescribiendo el repositorio https://github.com/{repo}")


def pushMirror(token: str, owner: str, repo: str, path: str, user: str):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    repo = owner if repo == user else repo

    description = requests.get(f"https://api.github.com/repos/{user}/{repo}").json()["description"]
    data = {"name": repo, "private": False, "description": description}

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
    subprocess.run(["git", "push", "--mirror", "--force", "origin"], check=True)



def updateInfo(token, owner):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(f"https://api.github.com/users/{owner}")
    userData = resp.json()
    bio = f"{userData.get("bio")}"
    data = {
        "name": userData.get("name"),
        "bio": bio,
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


def removeRepos(token):
    headers = {"Authorization": f"token {token}"}

    url = "https://api.github.com/user/repos"
    params = {"per_page": 100, "affiliation": "owner"}
    repos = requests.get(url, headers=headers, params=params).json()

    for repo in repos:
        name = repo["name"]
        owner = repo["owner"]["login"]
        delete_url = f"https://api.github.com/repos/{owner}/{name}"
        
        resp = requests.delete(delete_url, headers=headers)
        if resp.status_code == 204:
            pass
        else:
            print(f"{Red}[-]{Reset} Error al borrar {name}: {resp.status_code} - {resp.text}")
    print(f"{Green}[+]{Reset} Se borraron todos los repositorios correctamente")


def getStars(user):
    url = f"https://api.github.com/users/{user}/starred"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Error al obtener stars: {resp.status_code}")
    repos = resp.json()
    repos = [ repo["full_name"] for repo in repos ]
    return repos

def addStars(token, owner):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    repos = getStars(owner)
    for repo in repos:
        star_url = f"https://api.github.com/user/starred/{repo}"
        
        r = requests.put(star_url, headers=headers)
        if r.status_code == 204:
            pass
        else:
            print(f"{Red}[!]{Reset} Error al dar star a {repo}: {r.status_code}")

def removeStars(token, owner):
    repos = getStars(owner)
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    for repo in repos:
        star_url = f"https://api.github.com/user/starred/{repo}"
        r = requests.delete(star_url, headers=headers)
        if r.status_code == 204:
            pass
        else:
            print(f"{Red}[!]{Reset} Error al eliminar star de {repo}: {r.status_code}")


def getFollowing(user):
    url = f"https://api.github.com/users/{user}/following"
    resp = requests.get(url).json()
    users = [ user['login'] for user in resp ]
    return users

def unfollowUsers(token, user):
    users = getFollowing(user)
    headers = { "Authorization": f"token {token}" }
    for user in users:
        url = f"https://api.github.com/user/following/{user}"
        resp = requests.delete(url, headers=headers)
        if resp.status_code != 204:
            print(f"{Red}[!]{Reset} Ocurrio un error desconocido en la peticion")
    print(f"{Green}[+]{Reset} Se dejo de seguir a todos los usuarios")

def followUsers(token, owner):
    users = getFollowing(owner)
    headers = { "Authorization": f"token {token}" }
    for user in users:
        url = f"https://api.github.com/user/following/{user}"
        resp = requests.put(url, headers=headers)
        if resp.status_code != 204:
            print(f"{Red}[!]{Reset} Ocurrio un error desconocido en la peticion")
    print(f"{Green}[+]{Reset} El seguimiento de usuarios fue correcto.")

def downloadProfileimg(user):
    try:
        url = f"https://api.github.com/users/{user}"
        resp = requests.get(url)
        data = resp.json()
        avatar = data["avatar_url"]
        img = requests.get(avatar)
        with open(os.path.join(os.path.expanduser("~"), f"GithubProfileCloner/{user}.jpg"), "wb") as f:
            f.write(img.content)
        print(f"{Green}[+]{Reset} Imagen del avatar copiada correctamente a la carpeta ~/GithubProfileCloner")
    except Exception:
        return

def cloneProfile(owner, folder, token, user, email, norewrite: bool):
    try:
        removeRepos(token)
        removeStars(token, user)
        unfollowUsers(token, user)
        addStars(token, owner)
        followUsers(token, owner)
        updateInfo(token, owner)
        if os.path.exists(clonePath):
            shutil.rmtree(clonePath)

        downloadProfileimg(owner)
        resp = requests.get(f"https://api.github.com/users/{owner}")
        userData = resp.json()
        name = userData["name"]

        repos = getRepos(owner)
        for repo in repos:
            try:
                cloneMirror(repo, folder, name, email, norewrite)
                repoName = repo.split("/")[1]
                pushMirror(
                    token,
                    user,
                    repoName,
                    os.path.join(clonePath, repo.split("/")[1]),
                    owner
                )
                print(f"{Green}[+]{Reset} Repo procesado: {repoName}")
            except Exception as e:
                print(f"{Red}[!]{Reset} Error con {repo}: {e}")
                continue

        print(f"{Green}[+]{Reset} Todos los repositorios fueron clonados a la carpeta {folder}")
        return {"error": "false"}

    except Exception as e:
        print(f"{Red}[!]{Reset} Ocurrió un error general: {e}")
        return {"error": "true", "msg": str(e)}

