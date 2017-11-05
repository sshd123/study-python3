# -*- coding: utf-8 -*-
from collections import OrderedDict

import dataset
import petl as etl
import pymysql

from etl.batch_upsert import upsert_many
from etl.config import src_db, dest_db


def dataset_connect(**kwargs):
    url = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(kwargs.get('user'),
                                                                   kwargs.get('password'),
                                                                   kwargs.get('host'),
                                                                   kwargs.get('port'),
                                                                   kwargs.get('database'),
                                                                   kwargs.get('charset'))
    return dataset.connect(url)


def connect(conn):
    return pymysql.connect(database=conn['database'],
                           host=conn['host'],
                           user=conn['user'],
                           password=conn['password'],
                           port=int(conn['port']),
                           charset=conn['charset'])


def test_sync_users(src_conn, dest_conn):
    src_table = etl.fromdb(src_conn, 'select * from auth_user limit 8')

    mapping = OrderedDict()
    mapping['org_id'] = lambda x: 1
    mapping['username'] = 'username'
    mapping['name'] = 'full_name'
    mapping['status'] = lambda x: 'ACTIVE'
    mapping['uid'] = 'username'
    mapping['type'] = lambda x: "STUDENT"
    dst_table = etl.fieldmap(src_table, mapping)
    upsert_many(dest_conn['auth_user'], dst_table, keys=['username'])


if __name__ == '__main__':
    try:
        src_conn = connect(src_db)
        dest_conn = dataset_connect(**dest_db)
        test_sync_users(src_conn, dest_conn)
        src_conn.close()
    except Exception as ex:
        print(ex)
