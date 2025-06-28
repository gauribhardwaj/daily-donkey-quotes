import json
import random
import urllib.request

URL = "https://raw.githubusercontent.com/gauribhardwaj/daily-donkey-quotes/main/quotes.json"

try:
    with urllib.request.urlopen(URL) as response:
        quotes = json.loads(response.read().decode())
        print("\n🫏 DailyDonkey says:\n\"" + random.choice(quotes) + "\"\n")
except Exception as e:
    print("Failed to fetch donkey wisdom 🐴:", e)
