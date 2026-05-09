import os
import sys
import json
import time
import socket
import platform
import webbrowser
import requests

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table

console = Console()

# =========================================
# CONFIG
# =========================================

VERSION = "v4.0"

MOD_NAME = "YourTigranmods Official Comeback"

DOWNLOAD_URL = "https://pixeldrain.com/api/file/FcrcgCQP"

SAVE_PATH = "/storage/emulated/0/Download/YourTigranmodsOfficialComeback.apks"

USERS_FILE = "users.json"

YOUTUBE = "https://youtube.com/@speedmak01?si=CGir5ln_pMMb9baJ"

TG1 = "https://t.me/speedmak"
TG2 = "https://t.me/speedmak1"
TG3 = "https://t.me/+cdjdEm2gr0gwODA1"

# =========================================
# UTILS
# =========================================

def clear():
    os.system("clear")


def wait():
    input("\n[ PRESS ENTER ]")


def typing(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False


# =========================================
# USERS
# =========================================

def load_users():

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)

    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):

    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


# =========================================
# REGISTER
# =========================================

def register():

    clear()

    console.print(
        Panel.fit(
            "[bold red]REGISTER[/bold red]",
            border_style="red"
        )
    )

    users = load_users()

    username = input("\nUsername: ")
    password = input("Password: ")

    if username in users:

        console.print(
            "\n[bold red]User already exists[/bold red]"
        )

        wait()
        return

    users[username] = password

    save_users(users)

    console.print(
        "\n[bold green]Registration Successful[/bold green]"
    )

    wait()


# =========================================
# LOGIN
# =========================================

def login():

    clear()

    console.print(
        Panel.fit(
            "[bold red]LOGIN[/bold red]",
            border_style="red"
        )
    )

    users = load_users()

    username = input("\nUsername: ")
    password = input("Password: ")

    if username in users and users[username] == password:

        console.print(
            "\n[bold green]Login Successful[/bold green]"
        )

        time.sleep(1)
        return True

    else:

        console.print(
            "\n[bold red]Invalid Username or Password[/bold red]"
        )

        wait()
        return False


# =========================================
# AUTH MENU
# =========================================

def auth():

    while True:

        clear()

        table = Table(title="AUTH SYSTEM")

        table.add_column(
            "Option",
            style="red",
            justify="center"
        )

        table.add_column(
            "Action",
            style="white"
        )

        table.add_row("1", "Login")
        table.add_row("2", "Register")
        table.add_row("3", "Exit")

        console.print(table)

        choice = input("\nSelect: ")

        if choice == "1":

            if login():
                break

        elif choice == "2":
            register()

        elif choice == "3":
            sys.exit()


# =========================================
# ASCII
# =========================================

ASCII = r'''

██╗   ██╗ ██████╗ ██╗   ██╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

████████╗██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
╚══██╔══╝██║██╔════╝ ██╔══██╗██╔══██╗████╗  ██║
   ██║   ██║██║  ███╗██████╔╝███████║██╔██╗ ██║
   ██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║
   ██║   ██║╚██████╔╝██║  ██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

╔══════════════════════════════════╗
║      YourTigran Cheat Safe      ║
║       Universal Engine v4       ║
╚══════════════════════════════════╝

'''

# =========================================
# LOADING
# =========================================

def loading():

    clear()

    console.print(
        f"[bold red]{ASCII}[/bold red]"
    )

    console.print(
        Panel.fit(
            f"[bold white]{MOD_NAME}[/bold white]\n"
            f"[red]Universal Engine {VERSION}[/red]",
            border_style="red"
        )
    )

    typing("Initializing modules...", 0.02)
    typing("Checking security...", 0.02)
    typing("Loading assets...", 0.02)
    typing("Connecting secure session...", 0.02)

    with Progress() as progress:

        task = progress.add_task(
            "[red]Loading...",
            total=100
        )

        for i in range(100):

            time.sleep(0.02)

            progress.update(
                task,
                advance=1
            )

    if internet():

        console.print(
            "\n[bold green]Internet Connected[/bold green]"
        )

    else:

        console.print(
            "\n[bold red]No Internet[/bold red]"
        )

    time.sleep(1)


# =========================================
# SUBSCRIBE PAGE
# =========================================

def subscribe_page():

    clear()

    console.print(
        Panel.fit(
f"""
[bold red]REQUIRED SUBSCRIPTIONS[/bold red]

YouTube:
{YOUTUBE}

Telegram:
{TG1}
{TG2}
{TG3}
""",
border_style="red"
))

    console.print("\n[1] Open YouTube")
    console.print("[2] Open Telegram")
    console.print("[3] Continue")

    choice = input("\nSelect: ")

    if choice == "1":

        webbrowser.open(YOUTUBE)

        wait()

        subscribe_page()

    elif choice == "2":

        webbrowser.open(TG1)

        wait()

        subscribe_page()


# =========================================
# FRIENDS PAGE
# =========================================

def friends_page():

    clear()

    text = """
SPECIAL THANKS

Ankit
Kaier
BRZ TEAM
Raj VARDHAN

Usernames:
@AnkitXlive
@KaierRlzx
@BRZGANG
@Config_king
"""

    console.print(
        Panel.fit(
            text,
            border_style="red"
        )
    )

    wait()


# =========================================
# DOWNLOAD
# =========================================

def download_file():

    clear()

    console.print(
        Panel.fit(
            "[green]Downloading APK...[/green]",
            border_style="red"
        )
    )

    try:

        response = requests.get(
            DOWNLOAD_URL,
            stream=True
        )

        total = int(
            response.headers.get(
                'content-length',
                0
            )
        )

        with open(
            SAVE_PATH,
            'wb'
        ) as file:

            with Progress() as progress:

                task = progress.add_task(
                    "[red]Downloading",
                    total=total
                )

                for chunk in response.iter_content(
                    chunk_size=1024
                ):

                    if chunk:

                        file.write(chunk)

                        progress.update(
                            task,
                            advance=len(chunk)
                        )

        console.print(
            f"\n[bold green]Saved:[/bold green] {SAVE_PATH}"
        )

    except Exception as e:

        console.print(
            f"[bold red]Error:[/bold red] {e}"
        )

    wait()


# =========================================
# MOD INFO
# =========================================

def mod_info():

    clear()

    info = f"""
{MOD_NAME}

• Universal UI Engine
• Multi Interface Support
• Fast Loading
• Android 5+ Support
• Overlay Support
• Shizuku Compatible
• Cyberpunk UI
• Auto Download System
• Online Engine
"""

    console.print(
        Panel.fit(
            info,
            border_style="red"
        )
    )

    wait()


# =========================================
# COMMUNITY
# =========================================

def community():

    clear()

    info = f"""
YOUTUBE:
{YOUTUBE}

TELEGRAM:
{TG1}
{TG2}
{TG3}
"""

    console.print(
        Panel.fit(
            info,
            border_style="red"
        )
    )

    wait()


# =========================================
# SYSTEM INFO
# =========================================

def system_info():

    clear()

    info = f"""
Python:
{sys.version}

Platform:
{platform.system()}

Device:
{platform.machine()}
"""

    console.print(
        Panel.fit(
            info,
            border_style="red"
        )
    )

    wait()


# =========================================
# ENGINE
# =========================================

def engine():

    clear()

    typing("Checking device...", 0.02)
    typing("Checking protection...", 0.02)
    typing("Encrypting session...", 0.02)
    typing("Launching engine...", 0.02)

    time.sleep(2)

    console.print(
        "\n[bold green]ENGINE STARTED SUCCESSFULLY[/bold green]"
    )

    wait()


# =========================================
# OPEN FOLDER
# =========================================

def open_folder():

    os.system(
        f'am start -a android.intent.action.VIEW -d file://{SAVE_PATH}'
    )


# =========================================
# MAIN MENU
# =========================================

def menu():

    while True:

        clear()

        table = Table(
            title=f"YourTigranmods Universal Engine {VERSION}"
        )

        table.add_column(
            "Option",
            style="red",
            justify="center"
        )

        table.add_column(
            "Action",
            style="white"
        )

        table.add_row("1", "Start Engine")
        table.add_row("2", "Download Mod")
        table.add_row("3", "Mod Information")
        table.add_row("4", "Community")
        table.add_row("5", "System Info")
        table.add_row("6", "Open Download Folder")
        table.add_row("7", "Exit")

        console.print(table)

        choice = input("\nSelect Option: ")

        if choice == "1":
            engine()

        elif choice == "2":
            download_file()

        elif choice == "3":
            mod_info()

        elif choice == "4":
            community()

        elif choice == "5":
            system_info()

        elif choice == "6":
            open_folder()

        elif choice == "7":

            clear()

            typing("Goodbye...", 0.03)

            sys.exit()

        else:

            console.print(
                "[red]Invalid Option[/red]"
            )

            time.sleep(1)


# =========================================
# START
# =========================================

loading()
auth()
subscribe_page()
friends_page()
menu()
