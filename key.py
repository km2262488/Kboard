import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout Elang Keyboard v1.8 Clean
CONFIG_CONTENT = 'extra-keys = [["git clone ","&&","CTRL","ALT","HOME","END","DEL"],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","pip install "],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER"]]'

def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")

    print("[+] Keyboard Termux Updated")
    print("[+] Layout: git clone | && | pip install | python | nano | ls")
    print("[!] Jalankan 'exit' lalu buka ulang Termux")

if __name__ == "__main__":
    install()
