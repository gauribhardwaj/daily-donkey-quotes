# check_quotes.py
import json

with open('quotes.json') as f:
    quotes = json.load(f)

dupes = set([x for x in quotes if quotes.count(x) > 1])

if dupes:
    print("❌ Duplicate quotes found:", dupes)
    exit(1)
else:
    print("✅ No duplicate quotes found.")
