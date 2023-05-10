import requests
from bs4 import BeautifulSoup
import pandas as pd 

Product_Name = []
Prices = []
Description = []
Reviews = []

for i in range(2,6):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    # print(soup.prettify())


    # nextPage = soup.find("a",class_="_1LKTO3").get("href")
    # completeNextPage = "https://www.flipkart.com" + nextPage
    # print(completeNextPage)

    # url = completeNextPage
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")

    box = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_ = "_4rR01T")


    for i in names:
        name = i.text
        Product_Name.append(name)

    # print(Product_Name)

    prices = box.find_all("div",class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        price = i.text
        Prices.append(price)

    # print(Prices)


    desc = box.find_all("ul",class_ = "_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)

    # print(Description)


    reviews = box.find_all("div", class_ = "_3LWZlK")

    for i in reviews:
        name = i.text
        Reviews.append(name)

    # print(Reviews)


df = pd.DataFrame({"Product Name":Product_Name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
df.to_csv("Flipkart_mobiles_under_50000.csv")
