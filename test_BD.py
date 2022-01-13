import BD
import pytest
import sqlite3

@pytest.fixture()
def initBDpath(tmpdir):
    tmpdir.join("test_BD")
    path = str(tmpdir)+"test_BD"
    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()
    yield path

def checkBDhasTable(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    con.close()
    return d

def test_init(initBDpath):
    bd = BD.BD(initBDpath)
    del bd
    checkBDhasTable(initBDpath)


def test_add_value(initBDpath):
    bd = BD.BD(initBDpath)
    bd.add_value({'memory': 62.5, 'cpu': 10.25, 'disk': 23.2})
    del bd

    d = checkBDhasTable(initBDpath)
    assert len(d) == 1
    assert d[0][0] == 62.5
    assert d[0][1] == 10.25
    assert d[0][2] == 23.2


def test_add_value_wrong_value_1(initBDpath):
    bd = BD.BD(initBDpath)
    with pytest.raises(ValueError):
        bd.add_value({'memry': 62.5, 'cpu': 10.25, 'disk': 23.2})
    del bd

    d = checkBDhasTable(initBDpath)
    assert len(d) == 0


def test_add_value_wrong_value_2(initBDpath):
    bd = BD.BD(initBDpath)
    with pytest.raises(ValueError):
        bd.add_value({'cpu': 10.25, 'disk': 23.2})
    del bd

    d = checkBDhasTable(initBDpath)
    assert len(d) == 0


def test_add_value_wrong_value_3(initBDpath):
    bd = BD.BD(initBDpath)
    with pytest.raises(ValueError):
        bd.add_value({'memory': 62.5, 'cpu|disk': 10.25, 'disk': 23.2})
    del bd

    d = checkBDhasTable(initBDpath)
    assert len(d) == 0


def test_add_value_wrong_value_4(initBDpath):
    bd = BD.BD(initBDpath)
    with pytest.raises(ValueError):
        bd.add_value({'memory': 62.5, 'cpu': 10.25, 'cpu': 23.2})
    del bd

    d = checkBDhasTable(initBDpath)
    assert len(d) == 0
