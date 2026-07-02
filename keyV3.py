
import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout Keyboard v.3- Full 9x3
CONFIG_CONTENT = 'extra-keys = [["bash ","git clone ","&&","CTRL","node ","HOME","END","DEL","go "],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","vim ","pip install ","htop"],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER","rm -rf "]]'

def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")
    print("[!] v.3: Layout Full 27 tombol")
    print("[!] WARNING: Tombol paling kanan bawah = rm -rf")
    print("[!] Jalankan: termux-reload-settings")
   

if __name__ == "__main__":
    install()
