#  Edge Search Automation Bot  🤖🔍
A simple but powerful Windows automation bot that performs random Bing/Edge searches using PyAutoGUI and keyboard libraries.
The script generates natural random sentences and executes human-like searches in Microsoft Edge, making automation feel seamless and realistic.<br><br>
<br><br>
😎 Bonus: This tool completely automates your searches, so you don’t have to lift a finger while racking up those sweet daily points — let your PC do the work while you chill! 🍹<br><br>

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
>🐍 Python 3.8+<br><br>
>🎯 OS-level mouse/keyboard control enabled<br><br>


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
&nbsp;
---

## 📌PROCEDURE
- 1. Configure Mouse Coordinates:
     - Prior to executing the bot, determine the on-screen coordinates of the search bar in your browser.You can acheive this by running the "Test_cord.py" script first .The rules are simple
     - Place your mouse cursor on the edge browser location where it usually opens and run the "Test_cord.py",You will get the x,y Coordinates which is usex by the main script
      - Attached picture for Reference 😁
<img width="1273" height="457" alt="image" src="https://github.com/user-attachments/assets/5f13eab6-1056-405d-bfb5-6a95613433e0" />
<br><br>
- 2. Update on the main code:
     Once you obtain the mouse coordinates
     - Open the main script.
     - Locate the variables where the coordinates are required.
     - Replace the placeholder values with the X, Y coordinates from Test_cord.py.
     - Save the file after updating.
     This ensures that the bot clicks the correct search bar position every time.<br><br>
- 3. Run the main script<br><br>

```bash
     python Ghost_SearchBot.py

```  
---

## 🛑 Failsafe System

- Move your mouse to top-left corner → script stops instantly
- Press Q → quits safely
- You will never get stuck in automation loops.
---
## 🤝 Contributing

Feel free to fork and improve! PRs are welcome.
---
