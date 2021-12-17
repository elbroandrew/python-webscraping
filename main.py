from bs4 import BeautifulSoup
import requests
import pandas as pd

website = 'https://www.cars.com/shopping/results/?stock_type=cpo&makes%5B%5D=mercedes_benz&models%5B%5D=&list_price_max=&maximum_distance=20&zip='
response = requests.get(website)


#check the status code:
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('div', {'class': 'vehicle-card'})


def main():
    print(len(results))


if __name__ == '__main__':
    main()
