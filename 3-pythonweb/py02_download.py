import requests

res = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

print(res)

fornecedores_file = open("mortes-covid-global.csv", "wb")

for pedaco in res.iter_content(100000):
  fornecedores_file.write(pedaco)

fornecedores_file.close()