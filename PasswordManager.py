

# ICTPRG302 - Ash's Password Manager

import os  # checks if the file exists

# global variable for the file name to store credentials
TXT_FILE = "credentials.txt"

# make the file with a header if it doesn't exist yet
def ensure_file_exists():
    if not os.path.exists(TXT_FILE):  # check if file is missing
        with open(TXT_FILE, "w", encoding="utf-8") as f:  # create it, write mode
            f.write("site|username|password|url\n")  # header row

# ask the user for details and add one line to the file
def add_credential():
    print("\nAdd a new credential")
    site = input("Site / Service name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    url = input("URL (optional): ").strip()

    # build one pipe-separated row: site|username|password|url
    line = site + "|" + username + "|" + password + "|" + url

    # open the file in append mode so we only add new lines
    with open(TXT_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print("Saved.\n")

# read the file and print the stored rows (aligned to headers)
def view_credentials():
    # if file somehow missing, just say no data
    if not os.path.exists(TXT_FILE):
        print("\n(No credentials stored yet.)\n")
        return

    # read all lines from the file
    with open(TXT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # if file is empty or only has a header, say no data
    if len(lines) <= 1:
        print("\n(No credentials stored yet.)\n")
        return

    # skip the first line if it is the header
    header_text = "site|username|password|url"
    start_index = 1 if lines[0].strip() == header_text else 0

    # parse lines into rows (exactly 4 columns)
    rows = []
    for line in lines[start_index:]:
        line = line.strip()
        if line == "":
            continue
        parts = line.split("|")
        while len(parts) < 4:   # pad short lines
            parts.append("")
        rows.append(parts[:4])  # keep only 4 columns

    # compute column widths based on headers and data
    headers = ["Site", "Username", "Password", "URL"]
    widths = [len(h) for h in headers]  # start with header lengths

    for row in rows:
        for index in range(4):  # 0..3 (Site, Username, Password, URL)
            if len(row[index]) > widths[index]:
                widths[index] = len(row[index])

    # print header and a matching separator (single-line join, no splitting)
    header_line = " | ".join(headers[index].ljust(widths[index]) for index in range(4))
    sep_line    = "-+-".join("-" * widths[index]                 for index in range(4))
    print("\n" + header_line)
    print(sep_line)

    # print each row aligned to the computed widths (single-line join, no splitting)
    for row in rows:
        print(" | ".join(row[index].ljust(widths[index]) for index in range(4)))
    print()  # blank line after table

# main menu loop
def main():
    print("Ash's Password Manager")
    ensure_file_exists()  # make sure file with header exists

    while True:  # keep showing the menu until user quits
        print("[1] Add credentials")
        print("[2] View credentials")
        print("[Q] Quit")
        choice = input("Make your choice: ").strip().lower()  # normalize input

        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "q":
            print("Goodbye. Thanks for using Ash's Password Manager.")
            break
        else:
            print("Invalid option, try again.\n")

# only run main() if this file is executed directly
if __name__ == "__main__":
    main()

     
