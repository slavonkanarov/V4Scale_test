import BD
import pytest
import sqlite3

path = "test_BD"


def test_init():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()

    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 0
    con.close()

    bd = BD.BD(path)
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    con.close()


def test_add_value():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(path)
    bd.add_value({'memory': 62.5, 'cpu': 10.25, 'disk': 23.2})
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 1
    assert d[0][0] == 62.5
    assert d[0][1] == 10.25
    assert d[0][2] == 23.2
    con.close()


def test_add_value_wrong_value_1():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(path)
    with pytest.raises(ValueError):
        bd.add_value({'memry': 62.5, 'cpu': 10.25, 'disk': 23.2})
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 0
    con.close()


def test_add_value_wrong_value_2():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(path)
    with pytest.raises(ValueError):
        bd.add_value({'cpu': 10.25, 'disk': 23.2})
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 0
    con.close()


def test_add_value_wrong_value_3():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(path)
    with pytest.raises(ValueError):
        bd.add_value({'memory': 62.5, 'cpu|disk': 10.25, 'disk': 23.2})
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 0
    con.close()


def test_add_value_wrong_value_4():
    global path

    con = sqlite3.connect(path)
    cur = con.cursor()
    tables = list(cur.execute("select name from sqlite_master where type is 'table'"))
    cur.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()

    bd = BD.BD(path)
    with pytest.raises(ValueError):
        bd.add_value({'memory': 62.5, 'cpu': 10.25, 'cpu': 23.2})
    del bd

    con = sqlite3.connect(path)
    cur = con.cursor()
    assert cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='data';").fetchall()[0][0] == 1
    d = cur.execute("SELECT * FROM data;").fetchall()
    assert len(d) == 0
    con.close()
