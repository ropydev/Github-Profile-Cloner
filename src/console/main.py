#!/bin/python3

# Built with Love.
# Console version
# python -m src.console.main -o owner -u user -t token

from ..lib import GithubProfileCloner
import argparse
import subprocess

Red = "\033[1m\033[31m"
Green = "\033[1m\033[32m"
Blue = "\033[36m"
Reset = "\033[0m"


def printLogo(color):
    subprocess.run(['clear'], check=True)
    banner = f"""{color}  ____ _ _   _           _           ____             __ _ _             ____ _                       
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


def argsParser():
    parser = argparse.ArgumentParser("./GithubProfileCloner.py -o <Github-user-dev>")
    parser.add_argument(
        "-v", "--version", help="Version del script usada.", action="store_true"
    )
    parser.add_argument("-o", "--owner", help="Usuario al que clonarle los repos.")
    parser.add_argument("-t", "--token", help="Token de La cuenta de github (PAT)")
    parser.add_argument(
        "-u",
        "--user",
        help="Usuario al que se le van a clonar los datos (el mismo del PAT)",
    )
    parser.add_argument("-e", "--email", help="Email del usuario al que se le va a enviar lo clonado.")
    parser.add_argument("--no-rewrite", action="store_true", help="No reescribe la historia de los commits")
    return parser.parse_args()


def main():
    try:
        args = argsParser()
        owner = args.owner
        token = args.token
        user = args.user
        email = args.email
        rewrite = args.no_rewrite
        if args.version:
            versionMsg = """Version v1.2 (18/08/2026) | Ronald Bello (ropydev)
https://github.com/ropydev/Github-Profile-Cloner"""
            print(versionMsg)
        elif owner and token and user and email:
            printLogo(Blue)
            decoration = f"+--{'-'*len(token)}--+\n"
            print(Blue+decoration+f"Token = {token[0:4] + '*'*(len(token)-4)}\nOwner = {owner}\nUser = {user}\nEmail = {email}\n"+decoration+Reset)
            confirmation = input(f"{Red}ADVERTENCIA: Este script borrara todos los repos del perfil {user} para hacer una clonacion correcta, porfavor confirme que esta acuerdo (y/N): ")
            print(Reset)
            if confirmation.lower() == "y":
                GithubProfileCloner.cloneProfile(
                    owner, GithubProfileCloner.clonePath, token, user, email, rewrite
                )
            elif confirmation.lower() == "n" or not confirmation:
                exit(0)
        else:
            print(f"{Red}[!]{Reset} Argumentos invalidos.")
    except KeyboardInterrupt:
        print(f"{Red}[!]{Reset} Aborted")


if __name__ == "__main__":
    main()
