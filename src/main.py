#!/bin/python3

# Built with Love.
# Author: ropydev
# Github: https://github.com/ropydev/Github-Profile-Cloner
# v0.1 - (13/08/2026)

import requests
import subprocess
import os
import argparse

# Colors
Red = "\033[1m\033[31m"
Green = "\033[1m\033[32m"
Blue = "\033[36m"
Reset = "\033[0m"

def printLogo():
    subprocess.run(["clear"], check=True)
    banner = f"""{Blue}   ____ _ _   _           _           ____             __ _ _             ____ _                       
  / ___(_) |_| |__  _   _| |__       |  _ \\ _ __ ___  / _(_) | ___       / ___| | ___  _ __   ___ _ __ 
 | |  _| | __| '_ \\| | | | '_ \\ _____| |_) | '__/ _ \\| |_| | |/ _ \\_____| |   | |/ _ \\| '_ \\ / _ \\ '__|
 | |_| | | |_| | | | |_| | |_) |_____|  __/| | | (_) |  _| | |  __/_____| |___| | (_) | | | |  __/ |   
  \\____|_|\\__|_| |_|\\__,_|_.__/      |_|   |_|  \\___/|_| |_|_|\\___|      \\____|_|\\___/|_| |_|\\___|_|

+-------------------------------------+
  Created by Ronald Bello (ropydev)
  https://github.com/ropydev
+-------------------------------------+
{Reset}"""
    print(banner)

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
            timeout=30
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
        subprocess.run(["git", "clone", "--mirror", url, os.path.join(destPath, repo.split("/")[1])], check=True)
        print(f"{Green}[+]{Reset} Se clono con exito el repositorio https://github.com/{repo}")
    except Exception as e:
        print(f"{Red}[!]{Reset} Ocurrio un error clonando el repositorio https://github.com/{repo}")

def genUserInfo(owner: str, folder: str):
    """
    Obtiene información de un usuario de GitHub y la guarda en un archivo Markdown.
    Incluye avatar, nombre, bio, ubicación, seguidores y repositorios públicos.
    """
    url = f"https://api.github.com/users/{owner}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error al obtener datos: {response.status_code}")

    data = response.json()

    md_content = f"""<h1>Perfil de {data.get('login')}</h1>

<img src="{data.get('avatar_url')}" alt="{data.get('login')} Avatar" width="250px" >

<p><b>Nombre:</b> {data.get('name') or 'No disponible'} </p>
<p><b>Bio:</b> {data.get('bio') or 'No disponible'} </p>
<p><b>Ubicación:</b> {data.get('location') or 'No disponible'} </p>
<p><b>Blog/Website:</b> {data.get('blog') or 'No disponible'} </p>
<p><b>Seguidores:</b> {data.get('followers')} </p>
<p><b>Siguiendo:</b> {data.get('following')} </p>
<p><b>Repositorios Públicos:</b> {data.get('public_repos')}</p>
"""

    filename = os.path.join(folder, f"{owner}.md")
    with open(filename, "w") as f:
        f.write(md_content)
    print(f"{Green}[+]{Reset} Perfil guardado en {filename}")


def cloneProfile(owner, folder):
    try:
        repos = getRepos(owner)
        genUserInfo(owner, os.path.expanduser("~"))
        for repo in repos:
            cloneMirror(repo, folder)
        print(f"{Green}[+]{Reset} Todos los repositorios fueron clonados a la carpeta {folder}")
    except Exception as e:
        print(f"{Red}[!]{Reset} Ocurrio un error: {e}")


def argsParser():
    parser = argparse.ArgumentParser("./GithubProfileCloner.py -o <Github-user-dev>")
    parser.add_argument("-v", "--version", help="Version del script usada.")
    parser.add_argument("-o", "--owner", help="Usuario al que clonarle los repos.")
    return parser.parse_args()


def main():
    try:
        args = argsParser()
        if args.version:
            print("v0.1")
        elif args.owner:
            printLogo()
            owner = args.owner
            cloneProfile(owner, os.path.join(f"{os.path.expanduser("~")}/GithubProfileCloner"))
        else:
            print(f"{Red}[!]{Reset} Argumentos invalidos.")
    except KeyboardInterrupt:
        print(f"{Red}[!]{Reset} Aborted")

main()
