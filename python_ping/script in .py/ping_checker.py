import platform
import subprocess
import re
import sys
from colorama import Fore, Style, init

# UTF-8 sur Windows pour emojis
if sys.platform == "win32":
    import os
    os.system("chcp 65001 >nul")
    sys.stdout.reconfigure(encoding="utf-8")

init(autoreset=True)

def run_ping():
    url = input(Fore.CYAN + "Enter URL or IP: " + Style.RESET_ALL)
    system = platform.system().lower()
    print(Fore.YELLOW + f"Detected system: {system}" + Style.RESET_ALL)

    if system == "windows":
        command = ["ping", "-n", "4", url]
    else:
        command = ["ping", "-c", "4", url]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + f"Host {url} is reachable." + Style.RESET_ALL)
            output = result.stdout

            # Average latency
            if system == "windows":
                match = re.search(r"Average = (\d+)ms", output) or re.search(r"Moyenne = (\d+)ms", output)
            else:
                match = re.search(r"= [\d\.]+/([\d\.]+)/", output)
            latency = match.group(1) if match else "N/A"

            # Packet loss
            if system == "windows":
                loss_match = re.search(r"\((\d+)%\s*(?:de )?(?:pertes|loss)\)", output, re.IGNORECASE)
            else:
                loss_match = re.search(r"(\d+)% packet loss", output)
            loss = loss_match.group(1) if loss_match else "N/A"

            # Display table
            print("\n" + Fore.MAGENTA + "Ping summary:" + Style.RESET_ALL)
            print(Fore.CYAN + "-"*35 + Style.RESET_ALL)
            print(Fore.YELLOW + f"{'Result':<15}" + Fore.GREEN + "Success" + Style.RESET_ALL)
            print(Fore.YELLOW + f"{'Avg Latency':<15}" + Fore.CYAN + f"{latency} ms" + Style.RESET_ALL)
            loss_color = Fore.RED if loss != "0" and loss != "N/A" else Fore.GREEN
            print(Fore.YELLOW + f"{'Loss':<15}" + loss_color + f"{loss} %" + Style.RESET_ALL)
            print(Fore.CYAN + "-"*35 + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Host {url} is unreachable." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Ping error: {e}" + Style.RESET_ALL)

def main_menu():
    while True:
        print(Fore.CYAN + "\n===== MENU =====" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Enter URL and run ping test" + Style.RESET_ALL)
        print(Fore.RED + "2. Quit" + Style.RESET_ALL)
        choice = input(Fore.YELLOW + "Choice: " + Style.RESET_ALL)

        if choice == "1":
            run_ping()
        elif choice == "2":
            break
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
