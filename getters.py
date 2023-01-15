import psycopg2


def get_product_by_id(config, prod_id):
    """
    :param config: Файл с настройками для подключения к БД
    :param prod_id: Значение product_id, запрашиваемое у пользователя
    :return: Возвращает выборку из БД по запросу в формате json-строки
    """
    result = {}
    with psycopg2.connect(host=config["host"], database=config["database"], user=config["user"], password=config["password"]) as conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT product_id, product_name, categories.category_name, unit_price FROM products JOIN categories USING(category_id) WHERE product_id={prod_id}')
            for i in cur:
                result["product_id"] = i[0]
                result["product_name"] = i[1]
                result["category_name"] = i[2]
                result["unit_price"] = i[3]

        return result


def get_category_by_id(config, cat_id):
    """
    :param config: Файл с настройками для подключения к БД
    :param cat_id: Значение category_id, запрашиваемое у пользователя
    :return: Возвращает выборку из БД по запросу в формате json-строки
    """
    result = {}
    res_list = []
    with psycopg2.connect(host=config["host"], database=config["database"], user=config["user"], password=config["password"]) as conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT category_id, category_name, description, products.product_name FROM categories JOIN products USING(category_id) WHERE category_id={cat_id}')

            for i in cur:
                res_list.append(i[3])
                result["category_id"] = i[0]
                result["category_name"] = i[1]
                result["description"] = i[2]
                result["product_name"] = res_list
    return result
