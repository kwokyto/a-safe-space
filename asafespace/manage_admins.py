from utilities import get_admins, get_md5_hash
import json
import sys

def is_nusnetid(nusnetid):
    if len(nusnetid) != 8:
        return False
    if nusnetid[0] != "e":
        return False
    if not nusnetid[1:].isnumeric():
        return False
    return True

def write_admins(dictionary):
    with open('ADMINS.txt', 'w') as json_file:
        json.dump(dictionary, json_file)
    json_file.close()

def add_admin():
    name = input("What is the new admin's name?\nName: ")
    nusnetid = ""
    while not is_nusnetid(nusnetid):
        nusnetid = str(input("What is the new admin's NUSNET ID?\nNUSNET ID: ")).lower()
    hash = get_md5_hash(nusnetid)
    admins = {}
    try:
        admins = get_admins()
    except:
        pass
    admins[name] = hash
    write_admins(admins)
    print("Admin " + name + " has successfully been added.\n")

def remove_admin():
    try:
        admins = get_admins()
    except:
        print("There are no admins to remove.\n")
        return
    
    admin_list = list(admins.keys())
    if len(admin_list) == 0:
        print("There are no admins to remove.\n")
        return

    print("Select an admin to remove:")
    for i in range(len(admin_list)):
        print("[" + str(i+1) + "]" + admin_list[i])
    
    while True:
        index = input("Option: ")
        if not index.isnumeric():
            continue
        index = int(index)
        if index <= 0:
            continue
        if index > len(admin_list):
            continue
        admins.pop(admin_list[index-1])
        write_admins(admins)
        break
    print("Removal of admin is successfuln")    

while (True):
    answer = None
    while True:
        answer = input("Select an option:\n   [1] Add an admin\n   [2] Remove an admin\n   [3] Exit\nOption: ")
        if answer == "1":
            add_admin()
        if answer == "2":
            remove_admin()
        if answer == "3":
            break
    if answer == "3":
        break