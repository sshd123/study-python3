import pymysql
from appdirs import unicode

batch_num = 4
config = {
    'test': {
        "host": '127.0.0.1',
        "port": 3306,
        'user': 'root',
        'password': '',
        'database': 'testdb',
        'charset': 'utf8'
    }
}


def _connect(conn):
    return pymysql.connect(database=conn['database'],
                           host=conn['host'],
                           user=conn['user'],
                           password=conn['password'],
                           port=int(conn['port']),
                           charset='utf8')


def create_insert_query(table_name, columns, values):
    col_names = ','.join(columns)
    return "INSERT INTO %s (%s) VALUES %s" % (table_name, col_names, values)


def format_data(data):
    ret = []
    for d in data:
        if isinstance(d, (int, float, bool)):
            ret.append(str(d))
        elif isinstance(d, (str, unicode)):
            ret.append('"' + d + '"')
        else:
            print("unsupport value: {}".format(d))
    return '({})'.format(','.join(ret))


def format_datas(datas):
    return ','.join([format(data) for data in datas])


def batch_insert(conn, table_name, columns, datas):
    try:
        with conn.cursor() as cursor:
            batch_list = []
            count = 0
            for data in datas:
                batch_list.append(data)
                if len(batch_list) == batch_num or len(datas) == datas.index(data) + 1:
                    sql = create_insert_query(table_name, columns, format_datas(batch_list))
                    cursor.execute(sql)
                    conn.commit()
                    count += len(batch_list)
                    batch_list = []
                    print('{} insert count: {}'.format(table_name, count))
    finally:
        conn.close()


def seed_group(conn):
    table_name = 'group'
    columns = ('description', 'name', 'type')
    datas = [('cmo', '管理员', 'ADMIN'),
             ('', '学生', 'STUDENT'),
             ('', '老师', 'TEACHER')]
    batch_insert(conn, table_name, columns, datas)


def main():
    conn = _connect(config['test'])
    seed_group(conn)


if __name__ == '__main__':
    main()
