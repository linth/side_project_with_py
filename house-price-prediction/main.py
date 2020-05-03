"""
Machine learning for house price prediction with decision tree.

References:
    - https://github.com/Shreyas3108/house-price-prediction/blob/master/housesales.ipynb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

def main():
    data = pd.read_csv("kc_house_data.csv")
    data.head()
    data.describe()

    data['bedrooms'].value_counts().plot(kind='bar')
    plt.figure(1)
    plt.title('number of Bedroom')
    plt.xlabel('Bedrooms')
    plt.ylabel('Count')
    sns.despine
    plt.show()

    # plt.figure(2)
    sns.jointplot(x=data.lat.values, y=data.long.values, size=10)
    plt.ylabel('Longitude', fontsize=12)
    plt.xlabel('Latitude', fontsize=12)
    plt.show()
    # plt1 = plt()
    sns.despine

    plt.scatter(data.price, data.sqft_living)
    plt.title("Price vs Square Feet")
    plt.show()

    plt.scatter(data.price, data.long)
    plt.title("Price vs Location of the area")
    plt.show()

    plt.scatter(data.price, data.lat)
    plt.xlabel("Price")
    plt.ylabel('Latitude')
    plt.title("Latitude vs Price")
    plt.show()

    plt.scatter(data.bedrooms, data.price)
    plt.title("Bedroom and Price ")
    plt.xlabel("Bedrooms")
    plt.ylabel("Price")
    plt.show()
    sns.despine
    plt.show()

    plt.scatter((data['sqft_living'] + data['sqft_basement']), data['price'])
    plt.show()

    plt.scatter(data.waterfront, data.price)
    plt.title("Waterfront vs Price ( 0= no waterfront)")
    plt.show()

    train1 = data.drop(['id', 'price'], axis=1)
    train1.head()
    data.floors.value_counts().plot(kind='bar')
    plt.scatter(data.floors, data.price)
    plt.show()

    plt.scatter(data.condition, data.price)
    plt.show()

    plt.scatter(data.zipcode, data.price)
    plt.title("Which is the pricey location by zipcode?")
    plt.show()


if __name__ == '__main__':
    main()