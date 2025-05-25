

import sys
import os
def init(PATH=os.getcwd()):
    current_dir = os.getcwd()
    dirs=(os.listdir(current_dir))
    if ".vcs" in dirs:
        print("[!] Version control system already initialized in this directory.")
        return
    print(f"[✓] Initialized version control system at {PATH}")
    main_folder = ".vcs"
    subfolders = ["objects", "commits"]
    files = ["index", "HEAD"]
    os.makedirs(main_folder, exist_ok=True)
    for folder in subfolders:
        os.makedirs(os.path.join(main_folder, folder), exist_ok=True)
    for file in files:
        with open(os.path.join(main_folder, file), 'w') as f:
            f.write("")


def add(file_path):
    print(f"[✓] Add command received for file: {file_path}")

def commit(message):
    print(f"[✓] Commit command received with message: '{message}'")

def log():
    print("[✓] Log command received")

def show(commit_id):
    print(f"[✓] Show command received for commit: {commit_id}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: 'add' requires a filename.")
        else:
            add(sys.argv[2])
    elif command == "commit":
        if len(sys.argv) < 3:
            print("Error: 'commit' requires a message.")
        else:
            commit(" ".join(sys.argv[2:]))
    elif command == "log":
        log()
    elif command == "show":
        if len(sys.argv) < 3:
            print("Error: 'show' requires a commit ID.")
        else:
            show(sys.argv[2])
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
