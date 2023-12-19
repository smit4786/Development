import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

for arg in sys.argv[1:]:
   response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + arg)


print(response.json())