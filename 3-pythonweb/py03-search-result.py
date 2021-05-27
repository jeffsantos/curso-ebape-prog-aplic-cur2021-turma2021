import requests
import sys
from requests import HTTPError


try:
  resp = requests.get("https://pypi.org/search/?q=" + "+".join(sys.argv[1:]))
  resp.raise_for_status()

except HTTPError:
  print("Erro ao tentar obter a página")
  sys.exit(1)

print(resp.text)

