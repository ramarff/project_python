import json
from urllib import request
from tabulate import tabulate

print("Selamat Datang di Program Rama")
print("Program cari brand handphone berbasi command line")
print("Program ini dibuat menggunakan API: https://api-mobilespecs.azharimm.site/v2/brands")

class Menu:
    def __init__(self, url):
        self.url=url

    def call(self):
        url=self.url;
        response=request.urlopen(url)
        data=json.loads(response.read())

    def data_brand(self):
        brand_name=[]
        type_brand=[]
        headers=["brand","type"]
        table=[[brand_name, type_brand]]
        for i in range(len(data['data'])):
           brand_name.append(data['data'][i]['brand_name'])
           type_brand.append(data['data'][i]['brand_slug'])

    def tampil(self):
        print(tabulate(self.table, self.headers, tablefmt="grid"))


# url="https://api-mobilespecs.azharimm.site/v2/brands"
# response=request.urlopen(url)
# data=json.loads(response.read())
# headers = ["brand", 'type']
# # table=data['data']
# brand_name=[]
# type_brand=[]
# headers=["Brand", "Type"]
# table=[[brand_name, type_brand]]
# for i in range(len(data['data'])):
#    brand_name.append(data['data'][i]['brand_name'])
#    type_brand.append(data['data'][i]['brand_slug'])

# print(i)
# print(tabulate(table, headers, tablefmt="grid"))

menu=Menu("https://api-mobilespecs.azharimm.site/v2/brands")
menu.tampil()