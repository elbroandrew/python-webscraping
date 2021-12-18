from bs4 import BeautifulSoup
import requests
import pandas as pd

name = []
mileage = []
rating = []
rating_count = []
price = []
dealer_name = []

# Pagination
for i in range(1, 11):
    website = 'https://www.cars.com/shopping/results/?page=' + str(i) + '&page_size=20&list_price_max=&makes[]=mercedes_benz&maximum_distance=20&models[]=&stock_type=cpo&zip='
    response = requests.get(website)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'vehicle-card'})

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
car_dealer.to_excel('multiple_pages_cars.xlsx', index=False)
