
    print('Решение задачи №4  Полярная система координат')
    data = input('Введите декартовы координаты в виде x;y: ')
    if ';' in data:
        data_split = data.split(';')
        decart_coordinats.append(transform(data_split[0]))
        decart_coordinats.append(transform(data_split[1]))
        polar_coordinate = polar_coords(decart_coordinats)
        print(f'Полярный радиус: radius={polar_coordinate[0]:.3f}')
        print(f'Полярный угол: phi={polar_coordinate[1]:.3f}')
    else:
        print('Недостаточно данных. Выполнение программы невозможно')


if __name__ == '__main__':
    main()