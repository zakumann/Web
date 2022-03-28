import pandas
house = pandas.read_csv('boston_house_prices_dataset.csv')
print(house)
print(house.head(1))
print(house.describe())