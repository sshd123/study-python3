import pandas as pd
from sqlalchemy import create_engine

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

conn = config['test']
engine = create_engine(str(r"mysql+pymysql://%s:" + '%s' + "@%s:%s/%s?charset=utf8") % (
    conn['user'], conn['password'], conn['host'], conn['port'], conn['database']))


def seed_group():
    table_name = 'group'
    columns = ('description', 'name', 'type')
    datas = [('admin', '管理员', 'ADMIN'),
             (None, '学生', 'CUSTOM'),
             (None, '老师', 'TEACHER')]
    df = pd.DataFrame(datas, columns=columns)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


def seed_feature():
    table_name = 'app'
    columns = ['name', 'enabled']

    def _create_dict(name, enabled):
        return {'name': name, 'enabled': enabled}

    datas = []
    features = {
        'APP1': 0,
        'APP2': 1
    }
    for feature in features.items():
        datas.append(_create_dict(feature[0], feature[1]))
    df2 = pd.DataFrame.from_records(datas, columns=columns)
    df2.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=100)


def main():
    seed_group()
    seed_feature()


if __name__ == '__main__':
    main()
