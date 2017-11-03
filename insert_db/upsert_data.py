# -*- coding: utf-8 -*-
import dataset


def upsert_many(table, rows, keys, ensure=None, types=None):
    for row in rows:
        table.upsert(row, keys, ensure, types)


db = dataset.connect('mysql+pymysql://root:@localhost/testdb')
print(db.tables)
table = db['users']

# print(dict(name='John Doe', age=37))
# table.insert(dict(name='John Doe', age=37))
upsert_many(table, [dict(name='kobe', age=37, hobby='play ball11'),
                    dict(name='booker', age=32, hobby='play ball12'),
                    dict(name='steve', age=30, hobby='play ball13')], keys=['age', 'name'])
