import psycopg2


def updater(config, result_id):
    """
    :param config: Файл с настройками для подключения к БД
    :param result_id: Словарь со связью ID товара и ID поставщика, который возвращает файл loader
    """
    with psycopg2.connect(host=config["host"], database=config["database"], user=config["user"], password=config["password"]) as conn:
        with conn.cursor() as cur:
            big_sql = ''
            for k, v in result_id.items():
                big_sql += f'UPDATE products SET supplier_id={v} WHERE product_id={k};'
            cur.execute(big_sql)
