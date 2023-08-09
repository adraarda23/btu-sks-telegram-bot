
import requests
from bs4 import BeautifulSoup
from tabula import read_pdf
from tabula import convert_into
from os import path


class ScrapeMenu:

  def __init__(self):
    pass

  def getPdf(self):
    requests.packages.urllib3.disable_warnings()
    if path.exists("pdf0.pdf"):
      print("dosya zaten var")
    else:
      url = "https://sks.btu.edu.tr/tr/sayfa/detay/4398/beslenme-ve-di̇yeteti̇k"
      response = requests.get(url, verify=False)
      page = BeautifulSoup(response.content, 'html.parser')
      ilan = page.find("table")
      trs = ilan.find_all("tr")
      link = trs[1].find("a").get("href")
      print("Dosya Indiriliyor")
      response = requests.get(link, verify=False)
      pdf = open("pdf0" + ".pdf", 'wb')
      pdf.write(response.content)
      pdf.close()
      print("PDF Dosyasi Indirildi")

  def convertPdfToCsv(self):
    df = read_pdf("pdf0.pdf", pages='all')[0]
    convert_into("pdf0.pdf", "yemekhane.csv", output_format="csv", pages='all')