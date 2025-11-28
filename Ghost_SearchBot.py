import pyautogui
import time
import random
import webbrowser
import keyboard
# --------------------------------------------------------
# Configuration
# --------------------------------------------------------

pyautogui.FAILSAFE = True

NUM_SEARCHES = 20  #NO OF SEARCHES
SEARCH_ENGINE_URL = "https://www.bing.com"  #Obviously for rewards;)
SEARCH_BOX_COORDS = (X, Y)       #change as per the coordinates acquired from the previous test code 

# --------------------------------------------------------
# Random sentence generator  CHANGE AS REQUIRED
# --------------------------------------------------------
def random_sentence():

  words = [
  "weather", "today", "python", "tutorial", "news", "headlines", "best",
  "smartphones", "funny", "videos", "sports", "updates", "car", "reviews",
  "machine", "learning", "how", "to", "cook", "pasta", "gaming", "laptops",
  "music", "playlists", "travel", "places", "coding", "interview",
  "artificial", "intelligence", "top", "movies", "2024", "free", "courses",
  "internet", "speed", "test", "crypto", "price", "cloud", "computing",
  "random", "facts", "fitness", "tips", "healthy", "food", "online", "tools",
  "history", "science", "experiments", "motivation", "quotes", "space",
  "world", "map", "calculator", "dictionary", "meaning", "keyboard",
  "shortcuts", "anime", "productivity", "apps", "weather", "tomorrow",
  "stock", "market", "fun", "riddles", "brain", "teasers", "math", "tricks",
  "optical", "illusions", "technology", "ai", "chatbots", "computer",
  "vision", "robotics", "basics", "wallpapers", "challenges", "data",
  "science", "virat", "kohli", "stats", "programming", "books", "youtube",
        "trending", "gaming", "news", "machine", "parts", "fashion", "trends",
        "facts", "diy", "project", "ideas", "music", "theory", "electric", "cars",
        "mobile", "photography", "android", "iphone", "tips", "life", "hacks",
        "home", "workouts", "space", "telescope", "nanotechnology", "quantum",
        "computing", "linux", "commands", "windows", "tricks", "pc", "performance",
        "visual", "studio", "code", "cyber", "security", "ethical", "hacking",
        "wifi", "booster", "superhero", "movies", "fitness", "motivation",
        "healthy", "breakfast", "jokes", "memes", "google", "earth", "view",
        "beautiful", "places", "famous", "landmarks", "train", "timings", "flight",
        "tracker", "latest", "gadgets", "smart", "home", "devices", "weather",
        "radar", "music", "festivals", "gaming", "wallpapers", "deep", "learning",
        "neural", "networks", "crypto", "mining", "robot", "vacuum", "headphone",
        "reviews", "cloud", "storage", "keyboard", "reviews", "cheap", "hotels",
        "random", "sentences", "text", "generator", "math", "solver", "online",
        "notepad"
        ]

        return " ".join(random.choice(words) for _ in range(random.randint(3, 7)))
# --------------------------------------------------------
# Main Bot Execution  
# --------------------------------------------------------

        print(" Bot started! Press 'q' anytime to stop or move mouse to the top-left corner.")

        webbrowser.open(SEARCH_ENGINE_URL)
        time.sleep(5)

for pos in range(NUM_SEARCHES):

if keyboard.is_pressed("q"):
print("\size Bot stopped by user (key 'q').")
break

delay_minutes = 1         #Delay To Make your search Legit
print(f"\size Waiting {delay_minutes}/2 minutes before next search...")

for _ in range(delay_minutes * 60):
time.sleep(1)
if keyboard.is_pressed("q"):
print("\size Bot stopped by user (key 'q').")
exit()

        query = random_sentence()
        print(f" Search {pos+1}/{NUM_SEARCHES}: \"{query}\"")

    pyautogui.click(*SEARCH_BOX_COORDS)
    time.sleep(1)

        pyautogui.typewrite(query, interval=0.1)

            print(" Pausing 10 seconds before Enter...")
for _ in range(10):
    time.sleep(1)
    if keyboard.is_pressed("q"):
    print("\size Bot stopped by user (key 'q').")
exit()

    pyautogui.press("enter")
print(" Search executed!")

time.sleep(5)

    print("\size All searches completed or bot stopped. Exiting safely.")
