import tkinter as tk
import os

BLOCK_INTERNET='''powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall reset & netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound'"'''
ALLOW_INTERNET='''powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound'"'''
BLOCK_INTERNET_ALLOW_CHROME='''powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall reset & netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound & netsh advfirewall firewall add rule name=\"chrome1\" program=\"C:\Program Files\Google\Chrome\Application\chrome.exe\" dir=out action=allow & netsh advfirewall firewall add rule name=\"chrome2\" program=\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" dir=out action=allow'"'''
RESTRICT_CHROME='''regedit URLBlocklist.reg'''
UNRESTRICT_CHROME='''regedit Cancel_URLBlocklist.reg & powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound & netsh advfirewall firewall add rule name=\"chrome1\" program=\"C:\Program Files\Google\Chrome\Application\chrome.exe\" dir=out action=allow & netsh advfirewall firewall add rule name=\"chrome2\" program=\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" dir=out action=allow'"'''
APPLY_WHITE_LIST='''regedit URLWhitelist.reg'''
def execute(command):
    os.system(command)

def operation7():
    print("Operation 7")

def operation8():
    print("Operation 8")

def operation9():
    print("Operation 9")

root = tk.Tk()
root.title("koshernet.github.io תוכנת על ידי הראל ינון")

operations = {
f"חסום אינטרנט":lambda: execute(BLOCK_INTERNET),
f"אפשר אינטרנט":lambda: execute(ALLOW_INTERNET),
f"חסום אינטרנט, אבל אפשר כרום":lambda: execute(BLOCK_INTERNET_ALLOW_CHROME),
f"הגבל כרום":lambda: execute(RESTRICT_CHROME),
f"בטל הגבלת כרום":lambda: execute(UNRESTRICT_CHROME),
f"הפעל רשימה לבנה":lambda: execute(APPLY_WHITE_LIST),
f"אפשרות 7":lambda: operation7(),
f"אפשרות 8":lambda: operation8(),
f"אפשרות 9":lambda: operation9()
}

operations_iterator = iter(operations.items())

# Create buttons in a 3x3 grid
for i in range(3):
    for j in range(3):
        button_name, command = next(operations_iterator)
        #command==operations[3*i+j][1]
        button = tk.Button(root, text=button_name, command=command)
        button.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
