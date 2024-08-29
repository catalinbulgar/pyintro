import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs
import urllib3

urllib3.disable_warnings()
url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/"
req = requests.get(url, verify=False)
link = Bs(req.text, 'html.parser')
print(link)
