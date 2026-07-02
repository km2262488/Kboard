import os

CONFIG_CONTENT = """extra-keys = [ \\
['ESC','/','-','HOME','UP','END','PGUP','TAB','|','FORWARD_DEL'], \\
['CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','|','_','=','DEL'], \\
['git add ','git commit -m ','git push ','git pull ','git status ','git log ','nano ','vim ','exit','ENTER'] \\
]
"""

path = os.path.expanduser("~/.termux/termux.properties")

# Bikin folder .termux kalau belum ada
os.makedirs(os.path.dirname(path), exist_ok=True)

with open(path, "w") as f:
    f.write(CONFIG_CONTENT)

print("✅ Sukses! File termux.properties udah dibuat")
print("➡️  Jalanin ini biar langsung aktif: termux-reload-settings")
