import pandas as pd

data = pd.read_csv('data_table/table2.csv')
print('===TASK 1====')  #######################################################################################
print('--Не должно быть null--')
contains_null = pd.isnull(data['link_id'])
print(contains_null)
save_1 = data[contains_null]
save_1.to_csv('contains_null.csv', encoding='utf-8', index=True)

print('--Каждое значение должно быть уникально для всей колонки--')
unique_numbers = data[data.duplicated('link_id')]
# unique_numbers = data.drop_duplicates() #удалить дубликаты
print(unique_numbers)
unique_numbers.to_csv('unique_numbers.csv', encoding='utf-8')

print('--Не должно быть литералов--')
literals = data[pd.to_numeric(data.link_id, errors='coerce').isnull()]  # переобразовать в число
print(literals)
literals.to_csv('literals.csv', encoding='utf-8', index=True)

print('===TASK 2====')  ######################################################################################

print('(from_x|from_y) координаты должны лежать в зоне, ограниченной координатами')
long_min = 30.432128906250004
long_max = 46.69189453125001
longitude_x = (long_max > data['x_from']) & (data['x_from'] < long_min)
longitude_y = (long_max > data['y_from']) & (data['y_from'] < long_min)
print(data[longitude_x])
print(data[longitude_y])
save_long_x = data[longitude_x]
save_long_y = data[longitude_y]
save_long_x.to_csv('long_from_x.csv', encoding='utf-8', index=True)
save_long_y.to_csv('long_from_y.csv', encoding='utf-8', index=True)

print('(x_to|y_to) координаты должны лежать в зоне, ограниченной координатами')
latitude_min = 53.839563678833606
latitude_max = 57.3146573557333
latitude_x = (latitude_max > data['x_to']) & (data['x_to'] < latitude_min)
latitude_y = (latitude_max > data['y_to']) & (data['y_to'] < latitude_min)
print(data[latitude_x])
print(data[latitude_y])
save_latitude_x = data[latitude_x]
save_latitude_y = data[latitude_y]
save_latitude_x.to_csv('latitude_from_x.csv', encoding='utf-8', index=True)
save_latitude_y.to_csv('latitude_from_y.csv', encoding='utf-8', index=True)
