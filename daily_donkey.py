import json
import random
import textwrap
import urllib.request

URL = "https://raw.githubusercontent.com/gauribhardwaj/daily-donkey-quotes/dev/quotes.json"

DONKEYS = {
    "happy": r"""
                          /\          /\
                         ( ^^        ^^ )
                          \ \\      // /
                           \_\\||||//_/
                            \/ o  o \
                           \/|      |\
                          \/ |  ∪   |
      ___________________\/  \      /
    """,
    "sleepy": r"""
                          /\         zZ
                         (-_-)       zZ
                          \ \\      // /
                           \_\\||||//_/
                            \/ -  - \
                           \/|      |\
                          \/ |  ~   |
      ___________________\/  \      /
    """,
    "angry": r"""
                          /\          /\
                        ( >.< )      ( >.< )
                          \ \\      // /
                           \_\\||||//_/
                            \/ >  < \
                           \/| >__< |\
                          \/ |  !!! |
      ___________________\/  \      /
    """
}

def speech_bubble(quote, width=50, indent=30):
    wrapped = textwrap.wrap(quote, width)
    max_len = max(len(line) for line in wrapped)
    pad = " " * indent
    top = pad + "." + "-" * (max_len + 2) + "."
    middle = "\n".join([f"{pad}| {line.ljust(max_len)} |" for line in wrapped])
    bottom = pad + "'" + "-" * (max_len + 2) + "'"
    return f"{top}\n{middle}\n{bottom}"

try:
    with urllib.request.urlopen(URL) as response:
        quotes = json.loads(response.read().decode())
        selected = random.choice(quotes)
        quote = selected["text"]
        mood = selected.get("mood", "happy")
        ascii_donkey = DONKEYS.get(mood, DONKEYS["happy"])

        print(speech_bubble(quote))
        print(ascii_donkey)
except Exception as e:
    print("Failed to fetch donkey wisdom 🐴:", e)
