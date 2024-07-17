'''
This code is for the first day of the challenge - Data Cleaning and Preparation

Clean the concatenated dataset
'''

# Imports
import pandas as pd
import numpy as np

# Open concatenated dataset
data = pd.read_csv('data\\raw\\despesa_ceaps_2008-2022.csv')

# Data Cleaning

# - Removing unecessary columns from dataset
data_with_removed_columns = data.copy().drop(columns=['DATA', 'DOCUMENTO', 'DETALHAMENTO', 'COD_DOCUMENTO'])

# - Separating CNPJ and CPF
cpfs = data_with_removed_columns['CNPJ_CPF'].str.extract(r'^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$')
cnpjs = data_with_removed_columns['CNPJ_CPF'].str.extract(r'^([0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[/]?[0-9]{4}?[-][0-9]{2})$')
data_with_removed_columns.loc[:, 'CPF'] = cpfs
data_with_removed_columns.loc[:, 'CNPJ'] = cnpjs
data_with_removed_columns = data_with_removed_columns.drop(columns=['CNPJ_CPF'])

# - Handling missing data
data_with_removed_columns = data_with_removed_columns.fillna('Não tem')

# - Changing VALOR_REEMBOLSADO decimal comma to point
data_with_removed_columns['VALOR_REEMBOLSADO'] = data_with_removed_columns['VALOR_REEMBOLSADO'].str.replace(',', '.')
data_with_removed_columns['VALOR_REEMBOLSADO'] = data_with_removed_columns['VALOR_REEMBOLSADO'].str.replace('\r', '')
data_with_removed_columns['VALOR_REEMBOLSADO'] = data_with_removed_columns['VALOR_REEMBOLSADO'].str.replace('\n', '')

# - Transforming data types to maximize perfomance
before = data_with_removed_columns.memory_usage(deep=True)

data_with_removed_columns['ANO'] = data_with_removed_columns['ANO'].astype('uint16')
data_with_removed_columns['MES'] = data_with_removed_columns['ANO'].astype('uint8')
object_columns = ['SENADOR', 'TIPO_DESPESA', 'FORNECEDOR', 'CPF', 'CNPJ']
data_with_removed_columns[object_columns] = data_with_removed_columns[object_columns].apply(lambda x: x.astype('category'))
data_with_removed_columns['VALOR_REEMBOLSADO'] = data_with_removed_columns['VALOR_REEMBOLSADO'].astype('float64')

after = data_with_removed_columns.memory_usage(deep=True)

print(data_with_removed_columns.info())
print(f"Memory usage before:\n{before}\n")
print(f"Memory usage after:\n{after}\n")

# Saving file to cleaned folder
data_with_removed_columns.to_csv('data\\cleaned\\despesa_ceaps_cleaned.csv', index=False)
