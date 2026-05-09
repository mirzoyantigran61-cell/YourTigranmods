import os
import sys
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table

console = Console()

MOD_NAME = "YourTigranmods Official Comeback"
DOWNLOAD_URL = "https://pixeldrain.com/api/file/FcrcgCQP"
SAVE_PATH = "/storage/emulated/0/Download/YourTigranmodsOfficialComeback.apks"


def clear():
    os.system("clear")


def loading():
    clear()
    ascii_logo = r'''╝

████████╗██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
╚══██╔══╝██║██╔════╝ ██╔══██╗██╔══██╗████╗  ██║
   ██║   ██║██║  ███╗██████╔╝███████║██╔██╗ ██║
   ██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║
   ██║   ██║╚██████╔╝██║  ██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

            ╔══════════════════════════════════╗
║      YourTigran Cheat Safe      ║
║       Universal Engine v1       ║
╚══════════════════════════════════╝	       

'''

    console.print(f"[bold red]{ascii_logo}[/bold red]")
    console.print(Panel.fit(
        "[bold white]YourTigranmods Cheat Safe[/bold white]\n"
        "[green]Universal APK Loader[/green]",
        border_style="red"
    ))

    with Progress() as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        for i in range(100):
            time.sleep(0.02)
            progress.update(task, advance=1)


def show_menu():
    clear()

    table = Table(title="YourTigranmods Cheat Safe")

    table.add_column("Option", style="red", justify="center")
    table.add_column("Action", style="white")

    table.add_row("1", "Download Mod")
    table.add_row("2", "Mod Information")
    table.add_row("3", "Open Download Folder")
    table.add_row("4", "Exit")

    console.print(table)


def download_file():
    clear()
    console.print(Panel.fit("[green]Downloading APK...[/green]"))

    try:
        response = requests.get(DOWNLOAD_URL, stream=True)
        total = int(response.headers.get('content-length', 0))

        with open(SAVE_PATH, 'wb') as file:
            with Progress() as progress:
                task = progress.add_task("[red]Downloading", total=total)

                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        progress.update(task, advance=len(chunk))

        console.print(f"\n[bold green]Saved to:[/bold green] {SAVE_PATH}")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

    input("\nPress ENTER to continue...")


def mod_info():
    clear()

    info = """
YourTigranmods Official Comeback

• Universal UI Engine
• Multi Interface Support
• Fast Loading
• Android 5+ Support
• Overlay Support
• Shizuku Compatible
    """

    console.print(Panel.fit(info, border_style="red"))

    input("\nPress ENTER to continue...")


def open_folder():
    os.system(f'am start -a android.intent.action.VIEW -d file://{SAVE_PATH}')


loading()

while True:
    show_menu()
    choice = input("\nSelect option: ")

    if choice == "1":
        download_file()

    elif choice == "2":
        mod_info()

    elif choice == "3":
        open_folder()

    elif choice == "4":
        clear()
        console.print("[bold red]Goodbye.[/bold red]")
        sys.exit()

    else:
        console.print("[red]Invalid option[/red]")
        time.sleep(1)
