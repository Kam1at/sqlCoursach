import json
import loader
import updater
import getters


if __name__ == '__main__':
    file = open('config.json')
    config = json.load(file)
    while True:
        print('1. Получить данные по ID продукта.\n2. Получить данные по ID категории.\n3. Заполнить таблицу Suppliers данными.\n0. Выход.')
        index = input('Введите номер команды: ')
        if index == '0':
            file.close()
            break
        elif index == '1':
            print(getters.get_product_by_id(config, input('Введите ID продукта: ')))
        elif index == '2':
            print(getters.get_category_by_id(config, input('Введите ID категории: ')))
        elif index == '3':
            try:
                data = loader.loader(config, 'suppliers.json', 'suppliers')
                updater.updater(config, data)
            except:
                print('Таблица уже была заполнена данными.')
            else:
                print('Таблица заполнена успешно.')