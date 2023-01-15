import psycopg2
import json


def loader(config, file_name, table_name):
    """
    :param config: Файл с настройками для подключения к БД
    :param file_name: Имя файла, из которого загружаются данные в таблицу
    :param table_name: Имя создаваемой таблицы в БД
    :return: Возвращает словарь со связью ID товара и ID поставщика вида: {product_id:supplier_id}
    """
    suppliers_id = {}
    products_id = {}
    result_id = {}
    with psycopg2.connect(host=config["host"], database=config["database"], user=config["user"], password=config["password"]) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT product_name, product_id FROM products')
            for i in cur:
                products_id[i[1]] = i[0]

            with open(file_name) as ff:
                data = json.load(ff)
                i = 1
                for row in data:
                    cur.execute(f'INSERT INTO {table_name} (company_name, contact_name, contact_post, country, address, phone, fax, homepage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                                (row['company_name'], row['contact'][:row['contact'].find(',')], row['contact'][row['contact'].find(',') + 1:], row['address'][:row['address'].find(';')],
                                 row['address'][row['address'].find(';'):].lstrip('; '), row['phone'], row['fax'], row['homepage']))
                    suppliers_id[i] = row["products"]
                    i += 1

    for k, v in products_id.items():
        for x, y in suppliers_id.items():
            if v in y:
                result_id[k] = x
    return result_id


