from chaeum import cnx_pool


def fetch_one_from_db(query):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Exception as e:
        raise e


def fetch_all_from_db(query):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise e
