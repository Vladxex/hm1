point_1 = (0, 2)  # координаты первой точки
point_2 = (2, 5)  # координаты второй точки
point_3 = (5, 2)  # координаты третей точки
point_4 = (6, 6)  # координаты четвертой точки
point_5 = (8, 3)  # координаты пятой точки
list_1 = [point_1, point_2, point_3, point_4, point_5]


# сортировка на мин маршрут
def sort(sort_list, sed_list):
    if len(sort_list) > 2:
        a = ((sort_list[1][0] - sort_list[0][0]) ** 2 + (sort_list[1][1] - sort_list[0][1]) ** 2) ** 0.5
        b = ((sort_list[2][0] - sort_list[0][0]) ** 2 + (sort_list[2][1] - sort_list[0][1]) ** 2) ** 0.5
        if a < b:
            sed_list.append(sort_list[0])
            sort_list.pop(0)
            return sort(sort_list, sed_list)
        elif a > b:
            sed_list.append(sort_list[0])
            sort_list[1], sort_list[2] = sort_list[2], sort_list[1]
            sort_list.pop(0)
            return sort(sort_list, sed_list)

    else:
        sed_list.append(sort_list[0])
        sed_list.append(sort_list[1])
    return sed_list


sl = sort(list_1, [])  # сортируем
sl.append(point_1)  # добавляем возврат домой

# подстановка значений в формулу
print(f'{point_1}', end='')
c, g, gg = 0, 0, 0
for i in sl:
    if c != 0:
        g = ((i[0] - c[0]) ** 2 + (i[1] - c[1]) ** 2) ** 0.5
        gg += g
        print(f' -> {i}[{gg}]', end='')
    c = i
print(' =', gg)