import statistics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
import pandas as pd
import csv


goldAndSilverStock = pd.read_csv('GoldSilver.csv', names=['Date', 'GoldPrice', 'SilverPrice'])
titanic = pd.read_csv('TitanicSurvival.csv')
gold_prices = goldAndSilverStock['GoldPrice']
silver_prices = goldAndSilverStock['SilverPrice']
print(titanic)

#####2. Знайти математичне сподівання, медіану, моду, дисперсію,
######  середньоквадратичне відхилення (поясніть їх зміст)

print(" ")
print("Gold price expected value")
print(statistics.median(goldAndSilverStock['GoldPrice']))
##Математичне сподівання ціни золота в даному випадку прогнозована середня ціна на золото

print(" ")
print("Gold price Median")
print(statistics.median(goldAndSilverStock['GoldPrice']))
##Медіана ціна на золото, це ціна яка перебуває в середині статистичного ряду цін на золото

print(" ")
print("Gold price Mode")
print(statistics.mode(goldAndSilverStock['GoldPrice']))
##Ціна на золото яка зустрічається в вибірці частіше за все

print(" ")
print("Silver price expected value")
print(statistics.median(goldAndSilverStock['SilverPrice']))
#Same for silver stock price
print(" ")
print("Silver price Median")
print(statistics.median(goldAndSilverStock['SilverPrice']))
#Same for silver stock price
print(" ")
print("Silver price Mode")
print(statistics.mode(goldAndSilverStock['SilverPrice']))
#Same for silver stock price


#####3. Візуалізувати завантажені дані за допомогою гістограми

plt.hist([gold_prices, silver_prices], bins=20, edgecolor='k', label=['Gold', 'Silver'])
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Histogram of Gold and Silver Prices')
plt.legend()
plt.show()
### Нажаль забракло часу розібратись як розгранулювати гістограму по датам
### дана гістограма демонструє як часто зустрічаються ті чі інші ціни на золото чи срібло


#####4. Для цих даних проробити всі дії з пункту колекції Series і
#####   DataFrame бібліотеки pandas

print('4. Для цих даних проробити всі дії з пункту колекції Series і')
print(' DataFrame бібліотеки pandas')
print(' ')
print('******************************************')
print('SERIES FUNCTIONS ')
print('******************************************')
print(' ')
print(goldAndSilverStock.count())
print(goldAndSilverStock['SilverPrice'].mean())
print(goldAndSilverStock['SilverPrice'].min())
print(goldAndSilverStock['SilverPrice'].max())
print(goldAndSilverStock['SilverPrice'].std())
print(goldAndSilverStock['SilverPrice'].describe())
print(goldAndSilverStock['SilverPrice'].values)
print(goldAndSilverStock['SilverPrice'].dtype)

print(' ')
print('******************************************')
print('DATAFRAME')
print('******************************************')
print(' ')
print(goldAndSilverStock.iloc[11])
print(goldAndSilverStock.iloc[22])
print(goldAndSilverStock.iloc[44])
print(silver_prices[(silver_prices > 300) & (silver_prices <400)].count())
print(goldAndSilverStock.T)
print(goldAndSilverStock.T.sort_index(axis=1, ascending=False)) #sort by index of columns in desc order
print(goldAndSilverStock.sort_values(by='GoldPrice',  ascending=False)) #sort by index of columns
print(' ')


#####5. Виконати первинну обробку даних
#####   TODO


#####8. Переглянути рядки набору даних катастрофи «Титаніка»
###### AND
#####9. Налаштувати назви стовпців
titanic.columns = ['name','survived','sex','age','Class']
print(' ')
#print(titanic.head())
print(' ')
#print(titanic.tail())

#####10. Провести простий аналіз даних
##MinAge
minAge = pd.Series([x for x in titanic['age'] if str(x) != 'nan']).min()
print(minAge)
##MaxAge
maxAge = pd.Series([x for x in titanic['age'] if str(x) != 'nan']).max()
print(maxAge)
##AverageAge
averageAge = pd.Series([x for x in titanic['age'] if str(x) != 'nan']).mean()
print(averageAge)
##SurvivedPassengers
survivedPassengers = titanic[titanic['survived'] == 'yes']
print(survivedPassengers)
##WomenFrom1stClass
womenFrom1stClass = titanic[(titanic['sex'] == 'female') & (titanic['Class'] == '1st')].sort_values(by='age',  ascending=True)
print(womenFrom1stClass)
##YoungestWomanFrom1stClass
youngestWomanFrom1stClass = titanic[(titanic['sex'] == 'female') & (titanic['Class'] == '1st')].min()
print(youngestWomanFrom1stClass)
##OldestWomanFrom1stClass
oldestWomanFrom1stClass = titanic[(titanic['sex'] == 'female') & (titanic['Class'] == '1st')].max()
print(oldestWomanFrom1stClass)
##SurvivedWomanFrom1stClass
survivedWomanFrom1stClass = titanic[(titanic['sex'] == 'female') & (titanic['Class'] == '1st') & (titanic['survived'] == 'yes')].count()
print(survivedWomanFrom1stClass)

#####11. Побудувати гістограму віку пасажирів
plt.hist(titanic['age'])
plt.xlabel('Age')
plt.ylabel('Qty')
plt.title('Histogram of Titanic passengers ranged by age')
plt.show()