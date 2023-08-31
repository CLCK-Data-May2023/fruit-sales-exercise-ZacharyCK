# import pandas
import pandas as pd

df_fruit_sales = pd.DataFrame({
    'Apples': ['35', '21'],
    'Bananas': ['41', '34']},
    index=['2017 Sales', '2018 Sales']
)

df_fruit_sales.to_csv('fruit.csv')


