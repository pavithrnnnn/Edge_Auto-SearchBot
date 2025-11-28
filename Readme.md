# 🔍 Edge Search Automation Bot  
A simple but powerful Windows automation bot that performs random Bing/Edge searches using **PyAutoGUI** and **keyboard** libraries.  
The script generates natural random sentences and performs real human-like searches in Microsoft Edge.

---

## ⚙️ Features
- 🖱️ OS-level mouse + keyboard automation  
- 🔤 Random word-based sentence generator  
- ⏳ Human-like random delays between searches  
- 🧠 Failsafe: Move mouse to top-left corner to stop  
- ❌ Press `q` anytime to instantly quit the script  
- 🛑 No browser drivers required — works with your real Edge installation  

---

## 📦 Requirements
🐍 Python 3.8+
🌐 Microsoft Edge installed
🎯 OS-level mouse/keyboard control enabled
📡 Internet connection

Install dependencies:

```bash
pip install pyautogui 
pip install pillow pygetwindow pymsgbox mouseinfo
pip install keyboard

```
---
## 🚀 How It Works

- Opens Microsoft Edge
- Generates a random 3–7 word sentence
- Focuses the address bar
- Types the query slowly
- Presses Enter
- Waits a random delay
- Repeats for N searches

---
## PROCEDURE
- 1. Configure Mouse Coordinates
     Prior to executing the bot, determine the on-screen coordinates of the search bar in your browser.You can acheive this by running the "Test_cord.py" script first .The rules are simple
     Place your mouse cursor on the edge browser location where it usually opens and run the "Test_cord.py",You will get the x,y Coordinates which is usex by the main script
     Attached video 4 Reference 😁
     
- 2. Update on the main code
     On the main code 

---
## 🛑 Failsafe System

- Move your mouse to top-left corner → script stops instantly
- Press Q → quits safely
- You will never get stuck in automation loops.
---
## 🤝 Contributing

Feel free to fork and improve! PRs are welcome.
---
