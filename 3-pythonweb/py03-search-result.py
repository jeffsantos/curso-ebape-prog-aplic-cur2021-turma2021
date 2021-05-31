import requests
import sys
from requests import HTTPError
import bs4
import webbrowser


if len(sys.argv) == 1:
  print("É preciso informar uma consulta!! Passe como argumento.")
  sys.exit(1)

try:
  url_str = "https://pypi.org/search/?q=" + "+".join(sys.argv[1:])
  print(url_str)
  resp = requests.get(url_str)
  resp.raise_for_status()

except HTTPError:
  print("Erro ao tentar obter a página")
  sys.exit(1)

#print(resp.text)

html_file = open("pypi_search.html", "wb")

for pedaco in resp.iter_content(100000):
  html_file.write(pedaco)

html_file.close()

soup = bs4.BeautifulSoup(resp.text, "html.parser")

packages = soup.select(".package-snippet")

for i in range(5):
  url_to_open = "https://pypi.org" + packages[i].get("href")
  print(f"Abrindo página {url_to_open}")
  webbrowser.open(url_to_open)
