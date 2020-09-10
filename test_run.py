from OSTLAB_logic import *

print('===TASK 1====')
test_no_null(), 'link_id|не должно быть null'
test_unique_value(), 'link_id|не должно быть литералов'
test_no_literals(), 'link_id|каждое значение должно быть уникально для всей колонки'

print('===TASK 2====')
test_longitude_xy(), 'x_from,y_from|координаты должны лежать в зоне, ограниченной координатами'
test_latitude_xy(), 'x_to,y_to|координаты должны лежать в зоне, ограниченной координатами'

print('===TASK 3====')
test_avg_speed_inf_null(), 'avg_speed|без отрицательных значений, Infinity и null.'
test_avg_speed_range_and_interval(), 'avg_speed|время суток должно быть в промежутке от 0 до 86400, с интервалом 15 ' \
                                     'минут, начиная с 0 '

print('===TASK 4====')
test_intensity_inf_null(), 'intensity|без отрицательных значений, Infinity и null.'
test_intensity_range_and_interval(), 'intensity|время суток должно быть в промежутке от 0 до 86400, с интервалом 15 ' \
                                     'минут, начиная с 0 '

print('===TASK 5====')
test_calendar(), 'calendar|формат данных должен быть записан по шаблону "ГГГГ-ММ-ДД"'
