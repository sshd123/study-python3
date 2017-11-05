# -*- coding: utf-8 -*-
import petl as etl
from pandas import DataFrame
from petl import Table


def upsert_many(table, rows, keys, ensure=None, types=None):
    if isinstance(rows, Table):
        rows = etl.dicts(rows)
    elif isinstance(rows, DataFrame):
        rows = rows.to_dict(orient='records')
    for row in rows:
        table.upsert(row, keys, ensure, types)
