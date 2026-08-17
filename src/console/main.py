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
    return parser.parse_args()


def main():
    try:
        args = argsParser()
        owner = args.owner
        token = args.token
        user = args.user
        if args.version:
            versionMsg = """Version v1.0 (16/08/2026) | Ronald Bello (ropydev)
https://github.com/ropydev/Github-Profile-Cloner"""
            print(versionMsg)
        elif owner and token and user:
            printLogo(Blue)
            decoration = f"+--{'-'*len(token)}--+\n"
            print(Blue+decoration+f"Token = {token[0:4] + '*'*(len(token)-4)}\nOwner = {owner}\nUser = {user}\n"+decoration+Reset)
            GithubProfileCloner.cloneProfile(
                owner, GithubProfileCloner.clonePath, token, user
            )
        else:
            print(f"{Red}[!]{Reset} Argumentos invalidos.")
    except KeyboardInterrupt:
        print(f"{Red}[!]{Reset} Aborted")


if __name__ == "__main__":
    main()
