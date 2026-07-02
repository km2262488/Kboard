import os

FILE_PATH = os.path.expanduser("~/.termux/termux.properties")

# Layout 
CONFIG_CONTENT = 'extra-keys = [["bash ","git clone ","&&","CTRL","node ","HOME","END","DEL","go "],["UP","LEFT","DOWN","RIGHT","PGUP","PGDN","vim ","pip install ","htop"],["ls","cd ","pkg ","nano ","python ","clear","exit","ENTER","rm -rf "],["npm install ","npm run dev ","python manage.py runserver ","docker ","psql ","mysql ","curl ","wget ","exit"]]'


def install():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write(CONFIG_CONTENT + "\n")
    print("[!] Layout Full ")
    print("[!] V.4")
    print("[!] Jalankan: termux-reload-settings")

if __name__ == "__main__":
    install()
