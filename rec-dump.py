import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def recycle_dumper():
	users = os.listdir('C:\\Users')
	for user in users:
		recycle_bin_path = os.path.join(os.environ["SystemDrive"], "$Recycle.Bin")
		files = os.listdir(recycle_bin_path)
		print(f"[-] {Fore.GREEN}Listing files for user{Fore.RESET}: {user}")
		for file in files:
			print(f"[*] {Fore.YELLOW}{str(file)}{Fore.RESET}")

recycle_dumper()
