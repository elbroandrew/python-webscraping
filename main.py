from bs4 import BeautifulSoup
import requests
import pandas as pd

website = 'https://www.cars.com/shopping/results/?stock_type=cpo&makes%5B%5D=mercedes_benz&models%5B%5D=&list_price_max=&maximum_distance=20&zip='
response = requests.get(website)

soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('div', {'class': 'vehicle-card'})

# name = results[0].find('h2').get_text()
# mileage = results[0].find('div', {'class': 'mileage'}).get_text()
# rating = results[0].find('span', {'class': 'sds-rating__count'}).get_text()
# rating_count = results[0].find('span', {'class': 'sds-rating__link'}).get_text()
# price = results[0].find('span', {'class': 'primary-price'}).get_text()
# dealer_name: str = results[0].find('div', {'class': 'dealer-name'}).get_text().strip()

name = []
mileage = []
rating = []
rating_count = []
price = []
dealer_name = []

for result in results:
    # name
    try:
        name.append(result.find('h2').get_text())
    except:
        name.append('N/A')

    # mileage
    try:
        mileage.append(result.find('div', {'class': 'mileage'}).get_text())
    except:
        mileage.append('N/A')

    # rating
    try:
        rating.append(result.find('span', {'class': 'sds-rating__count'}).get_text())
    except:
        rating.append('N/A')

    # rating_count
    try:
        rating_count.append(result.find('span', {'class': 'sds-rating__link'}).get_text())
    except:
        rating_count.append('N/A')

    # price
    try:
        price.append(result.find('span', {'class': 'primary-price'}).get_text())
    except:
        price.append('N/A')

    # dealer name
    try:
        dealer_name.append(result.find('div', {'class': 'dealer-name'}).get_text().strip())
    except:
        dealer_name.append('N/A')


car_dealer = pd.DataFrame(
    {
        'Name': name,
        'Mileage': mileage,
        'Dealer Name': dealer_name,
        'Rating': rating,
        'Rating Count': rating_count,
        'Price': price
    }
)

# Data Cleaning
car_dealer['Rating Count'] = car_dealer['Rating Count'].apply(lambda x: x.strip('reviews)').strip('('))
car_dealer['Mileage'] = car_dealer['Mileage'].apply(lambda x: x.strip('mi.').strip())

# Output to Excel file
car_dealer.to_excel('single_page_car.xlsx', index=False)


def main():
    print(car_dealer['Rating Count'])


if __name__ == '__main__':
    main()
