from bs4 import BeautifulSoup
import requests
import smtplib


headers = {
    "User-Agent": "",
    "Accept-Language": ""
}
#you can find the values for those 2 fields here: http://myhttpheader.com

my_email = ""
password = ""
target_price = #your target price
url = "" #any Amazon item URL

webpage = requests.get(url, headers=headers).text
soup = BeautifulSoup(webpage, "html.parser")

price = soup.find(name="span", class_="a-price-whole").text
price = float(price)

product_name = soup.find(name="span", id="productTitle").text.strip()

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            print("logging in")
            connection.login(my_email, password)
            print("logged in")
            connection.sendmail(from_addr=my_email, to_addrs="emailTheAlertShouldGoTo", msg=f"{product_name}\nis now {price}$\n{url}")
            print("email sent")


