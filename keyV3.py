import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout Keyboard V3
CONFIG_CONTENT = 'extra-keys = [["bash ","git clone ","&&","CTRL","node ","HOME","END","DEL","go "],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","vim ","pip install ","htop"],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER",""]]'

def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")
    print("[+] Keyboard Updated to V.3")
    print("[!] Jalankan: termux-reload-settings")

if __name__ == "__main__":
    install()
