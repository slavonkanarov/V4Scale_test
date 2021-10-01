# content of test_sample.py
import pytest
import SensorMemory
import CPUSensor
import DiskSensor
import BD
import sqlite3

import test_BD


def test_main():
    memsens = SensorMemory.SensorMemory()
    cpusens = CPUSensor.CPUSensor()
    disksens = DiskSensor.DiskSensor()
    data = {**memsens.get_data(), **cpusens.get_data(), **disksens.get_data()}
    excpect = {'memory': 62.5, 'cpu': 10.25, 'disk': 23.2}
    assert data.keys() == excpect.keys()
    assert 0 <= data["memory"] <= 100
    assert 0 <= data["cpu"] <= 100
    assert 0 <= data["disk"] <= 100

    con = sqlite3.connect(test_BD.path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(test_BD.path)
    bd.add_value(data)
    del bd

    con = sqlite3.connect(test_BD.path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 1
    assert d[0][0] == data["memory"]
    assert d[0][1] == data["cpu"]
    assert d[0][2] == data["disk"]
    con.close()
