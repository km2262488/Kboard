# Keyboard - Termux Versi Mager

Keyboard custom Termux versi mager buat daily use. Semua tombol kepake, nggak ada yang mubazir.

### **Cara Install**
```bash
pkg update && pkg install python -y
git clone https://github.com/km2262488/Kboard.git
cd Kboard
python key.py
or
python keyV2.py
termux-reload-setting
exit


kembali ke keyboard default

rm ~/.termux/termux.properties && termux-reload-settings
