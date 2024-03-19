import requests
from bs4 import BeautifulSoup

url_and_name = [
    {
        "prod_url":"https://www.amazon.in/Redmi-12-5G-Moonstone-Silver/dp/B0C9J97Z2D/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.FCizserMZFnPZMKT1d2QNRg2TH3BG4IuSHwbkmWrSKJFoGu5SRnxe59HdPqZdKF4hW1eq6zy39gCZDtvQ_XhgQUOYs0MEe5NvME2qWNpNbmkWDU0BI5tqIef9_yl0Sm7B_OWl0Ni5nqyLla7MEU9AFC9c86FX7wVoHFQMLaDEknu8zE-8gEJDSPfRLPyK5TOMOlEB6xwxyqo5qPn4dUoLyTAm9E8wX1Tgm1fXYUECH8.UPeyodg5lrAJ39P6RIgK38-6CFAwjQGMDPnbFcZEeBc&dib_tag=se&keywords=samsung%2Bgalaxy%2Bm21&qid=1710776412&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "Name":"Redmi 12",
        "target_price":12000
    },
{
        "prod_url":"https://www.amazon.in/Samsung-Segments-Smartphone-Octa-Core-Processor/dp/B0BZCR6TNK/ref=sr_1_3?dib=eyJ2IjoiMSJ9.FCizserMZFnPZMKT1d2QNRg2TH3BG4IuSHwbkmWrSKJFoGu5SRnxe59HdPqZdKF4hW1eq6zy39gCZDtvQ_XhgQUOYs0MEe5NvME2qWNpNbmkWDU0BI5tqIef9_yl0Sm7B_OWl0Ni5nqyLla7MEU9AFC9c86FX7wVoHFQMLaDEknu8zE-8gEJDSPfRLPyK5TOMOlEB6xwxyqo5qPn4dUoLyTAm9E8wX1Tgm1fXYUECH8.UPeyodg5lrAJ39P6RIgK38-6CFAwjQGMDPnbFcZEeBc&dib_tag=se&keywords=samsung%2Bgalaxy%2Bm21&qid=1710776412&sr=8-3&th=1",
        "Name":"Samsung",
        "target_price":14000
    },
{
        "prod_url":"https://www.amazon.in/gp/product/B0CC2DCH75/ref=ewc_pr_img_2?smid=A3CULM8YVQWVYP&th=1",
        "Name":"Wireless Mic",
        "target_price":1000
    }
]

def give_prod_price(URL):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='corePriceDisplay_desktop_feature_div')
    if (price == None):
        price = soup.find(id='corePriceDisplay_desktop_feature_div')
    return price.getText()

output_file=open('output.txt','w')
try:
    for every_prod in url_and_name:
        prod_price_returned = give_prod_price(every_prod.get("prod_url"))
        print(prod_price_returned[7:13] + " - " + every_prod.get("Name"))

        my_prod_price = prod_price_returned[7:13]
        my_prod_price = my_prod_price.replace(',', '')
        my_prod_price = int(float(my_prod_price))
        print(my_prod_price)

        if my_prod_price < every_prod.get("target_price"):
            print("Price is less now")
            output_file.write(every_prod.get("Name") + "\t" + "available at price \t"
                              + str(my_prod_price) + "\n")
        else:
            print("price is more than expected")

finally:
    output_file.close()





