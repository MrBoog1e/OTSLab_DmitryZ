import pandas as pd
import numpy as np

data = pd.read_csv('table.csv')


def test_no_null():
    print('--Не должно быть null--')
    contains_null = pd.isnull(data['link_id'])
    save_1 = data[contains_null]
    save_1.to_csv('LINK_ID_null.csv', encoding='utf-8', index=True)
    print(contains_null, 'отчёт сохранён в файле LINK_ID_null.csv')


def test_unique_value():
    print('--Каждое значение должно быть уникально для всей колонки--')
    unique_numbers = data[data.duplicated('link_id')]
    unique_numbers.to_csv('LINK_ID_unique_numbers.csv', encoding='utf-8')
    print(unique_numbers, 'отчёт сохранён в файле LINK_ID_unique_numbers.csv')


def test_no_literals():
    print('--Не должно быть литералов--')
    literals = data[pd.to_numeric(data.link_id, errors='coerce').isnull()]  # переобразовать в число
    literals.to_csv('LINK_ID_literals.csv', encoding='utf-8', index=True)
    print(literals, 'отчёт сохранён в файле LINK_ID_literals.csv')


def test_longitude_xy():
    print('(from_x|from_y) координаты должны лежать в зоне, ограниченной координатами')
    long_min = 30.432128906250004
    long_max = 46.69189453125001
    longitude_x = (long_max > data['x_from']) & (data['x_from'] < long_min)
    longitude_y = (long_max > data['y_from']) & (data['y_from'] < long_min)
    save_long_x = data[longitude_x]
    save_long_y = data[longitude_y]
    save_long_x.to_csv('FROM_X_longitude.csv', encoding='utf-8', index=True)
    save_long_y.to_csv('FROM_Y_longitude.csv', encoding='utf-8', index=True)
    print(longitude_x, 'отчёт сохранён в файле FROM_X_longitude.csv')
    print(longitude_x, 'отчёт сохранён в файле FROM_Y_longitude.csv')


def test_latitude_xy():
    print('(x_to|y_to) координаты должны лежать в зоне, ограниченной координатами')
    latitude_min = 53.839563678833606
    latitude_max = 57.3146573557333
    latitude_x = (latitude_max > data['x_to']) & (data['x_to'] < latitude_min)
    latitude_y = (latitude_max > data['y_to']) & (data['y_to'] < latitude_min)
    save_latitude_x = data[latitude_x]
    save_latitude_y = data[latitude_y]
    save_latitude_x.to_csv('X_TO_latitude.csv', encoding='utf-8', index=True)
    save_latitude_y.to_csv('Y_TO_latitude.csv', encoding='utf-8', index=True)
    print(latitude_x, 'отчёт сохранён в файле X_TO_latitude.csv')
    print(latitude_y, 'отчёт сохранён в файле Y_TO_latitude.csv')


def test_calendar():
    print('calendar - Формат данных должен быть записан по шаблону "ГГГГ-ММ-ДД".')
    calendar = data[pd.to_datetime(data.calendar, format='%Y/%m/%d', errors='coerce').isnull()]
    calendar.to_csv('CALENDAR_format_data.csv', encoding='utf-8', index=True)
    print(calendar, 'отчёт сохранён в файле CALENDAR_format_data.csv')


def test_intensity_inf_null():
    print('intensity - Без отрицательных значений, Infinity и null.')
    data['intensity'].replace([np.inf, -np.inf], np.nan, inplace=True)
    data[data.intensity.isnull()].to_csv('INTENSITY_null_inf.csv', encoding='utf-8')
    print(data[data.intensity.isnull()], 'отчёт сохранён в файле INTENSITY_null_inf.csv')


def test_intensity_range_and_interval():
    print('intensity - Время суток должно быть в промежутке от 0 до 86400, с интервалом 15 минут, начиная с 0')
    time_int = 900
    avg_s = data['intensity']
    for avg in avg_s:
        time_quart = 0
        try:
            avg_list = avg.split(',')
        except:
            print('stroka is not correct')
            break
        for item in avg_list:
            avg_time, avg_speed = item.split('=>')
            if time_quart != int(avg_time):
                print(item, 'Time in this string is not true')
                # data[avg_s].to_csv('intensity15.csv', encoding='utf-8', index=True)
                with open('INTENSITY_range_and_interval.csv', 'w') as file:
                    file.write(avg)
            time_quart += time_int
        if time_quart - time_int > 86400:
            print(time_quart)


def test_avg_speed_inf_null():
    print('avg_speed - Без отрицательных значений, Infinity и null.')
    data['avg_speed'].replace([np.inf, -np.inf], np.nan, inplace=True)
    data[data.intensity.isnull()].to_csv('AVG_SPEED_null_inf.csv', encoding='utf-8')
    print(data[data.intensity.isnull()], 'отчёт сохранён в файле AVG_SPEED_null_inf.csv')


def test_avg_speed_range_and_interval():
    print('avg_speed - Время суток должно быть в промежутке от 0 до 86400, с интервалом 15 минут, начиная с 0')
    time_int = 900
    avg_s = data['avg_speed']
    for avg in avg_s:
        time_quart = 0
        try:
            avg_list = avg.split(',')
        except:
            print('stroka is not correct')
            break
        for item in avg_list:
            avg_time, avg_speed = item.split('=>')
            if time_quart != int(avg_time):
                print(item, 'Time in this string is not true')
                # data[avg_s].to_csv('intensity15.csv', encoding='utf-8', index=True)
                with open('AVG_SPEED_range_and_interval.csv', 'w') as file:
                    file.write(avg)
            time_quart += time_int
        if time_quart - time_int > 86400:
            print(time_quart)
