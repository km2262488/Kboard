import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout Keyboard Versi Clean
CONFIG_CONTENT = 'extra-keys = [["git clone ","&&","CTRL","ALT","HOME","END","DEL"],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","pip install "],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER"]]'

def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")

    print("[+] Keyboard Termux berhasil diupdate ke v1.8 Clean")
    print("[+] Layout: git clone | && | pip install | python | nano | ls")
    print("[!] Jalankan 'exit' lalu buka ulang Termux biar kepake")

if __name__ == "__main__":
    install()
