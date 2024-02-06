import tkinter as tk
import run_command

def block_internet():
    command = ['powershell','-Command',"Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall reset & netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound'"]
    print(command)
    run_command.command(command)


def allow_internet():
    command = ['powershell','-Command',"Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall reset & netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound'"]
    run_command.command(command)

def block_internet_allow_chrome():
    command = ['powershell', '-Command', "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall reset & netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound & netsh advfirewall firewall add rule name=\"chrome1\" program=\"C:\Program Files\Google\Chrome\Application\chrome.exe\" dir=out action=allow & netsh advfirewall firewall add rule name=\"chrome2\" program=\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" dir=out action=allow'"]
    run_command.command(command)

def restrict_chrome():
    reg_file_path="URLBlocklist.reg"
    run_command.apply_reg_file(reg_file_path)

def unrestrict_chrome():
    reg_file_path="Cancel_URLBlocklist.reg"
    run_command.apply_reg_file(reg_file_path)

def white_list():
    reg_file_path="URLWhitelist.reg"
    run_command.apply_reg_file(reg_file_path)

def operation7():
    print("Operation 7")

def operation8():
    print("Operation 8")

def operation9():
    print("Operation 9")

root = tk.Tk()
root.title("3x3 Grid of Buttons")


# Define operations for each button
operations = [block_internet, allow_internet, block_internet_allow_chrome, 
              restrict_chrome, unrestrict_chrome, white_list, 
              white_list, operation8, operation9]

# Create buttons in a 3x3 grid
button_name = f"חסום אינטרנט"
button = tk.Button(root, text=button_name, command=operations[0])
button.grid(row=0, column=0, padx=5, pady=5)
button_name = f"אפשר אינטרנט"
button = tk.Button(root, text=button_name, command=operations[1])
button.grid(row=0, column=1, padx=5, pady=5)
button_name = f"חסום אינטרנט, אבל אפשר כרום"
button = tk.Button(root, text=button_name, command=operations[2])
button.grid(row=0, column=2, padx=5, pady=5)

button_name = f"הגבל כרום"
button = tk.Button(root, text=button_name, command=operations[3])
button.grid(row=1, column=0, padx=5, pady=5)
button_name = f"בטל הגבלת כרום"
button = tk.Button(root, text=button_name, command=operations[4])
button.grid(row=1, column=1, padx=5, pady=5)
button_name = f"הפעל רשימה לבנה"
button = tk.Button(root, text=button_name, command=operations[5])
button.grid(row=1, column=2, padx=5, pady=5)

button_name = f"אפשרות 7"
button = tk.Button(root, text=button_name, command=operations[6])
button.grid(row=2, column=0, padx=5, pady=5)
button_name = f"אפשרות 8"
button = tk.Button(root, text=button_name, command=operations[7])
button.grid(row=2, column=1, padx=5, pady=5)
button_name = f"אפשרות 9"
button = tk.Button(root, text=button_name, command=operations[8])
button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
