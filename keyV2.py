import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout Elang Keyboard v1.9 - 9 Kolom
CONFIG_CONTENT = 'extra-keys = [["bash","git clone ","&&","CTRL","node","HOME","END","DEL","go"],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","","pip install ",""],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER",""]]'

def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")

    print("[+] Keyboard Termux berhasil diupdate ke v1.9")
    print("[+] Layout: bash | git clone | && | CTRL | node | HOME | END | DEL | go")
    print("[+]         UP | LEFT | DOWN | RIGHT | PGUP | PGDN | pip install |")
    print("[+]         ls | cd | pkg | nano | python | clear | exit | ENTER |")
    print("[!] Jalankan 'termux-reload-settings' biar langsung kepake")

if __name__ == "__main__":
    install()
