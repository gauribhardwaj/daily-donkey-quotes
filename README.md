
Your workspace's emotional support donkey

# Daily Donkey Quotes 🫏

A bray a day keeps burnout away -Your workspace's emotional support donkey.
Fetches a daily donkey-worthy quote to kick off your workday with humour or wisdom.

## Usage

Add this to your `.bashrc` or `.zshrc`:

```bash
function dailydonkey() {
  quotes=$(curl -s https://raw.githubusercontent.com/gauribhardwaj/daily-donkey-quotes/main/quotes.json)
  quote=$(echo "$quotes" | jq -r '.[]' | shuf -n 1)
  echo -e "\n🫏  DailyDonkey says:\n\"$quote\"\n"
}
dailydonkey
