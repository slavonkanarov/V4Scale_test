# content of test_sample.py
import pytest
import SensorMemory
import CPUSensor
import DiskSensor
import BD
import sqlite3

import test_BD


def test_main(tmpdir):
    tmpdir.join("test_BD")
    path = str(tmpdir)+"test_BD"
    memsens = SensorMemory.SensorMemory()
    cpusens = CPUSensor.CPUSensor()
    disksens = DiskSensor.DiskSensor()
    data = {**memsens.get_data(), **cpusens.get_data(), **disksens.get_data()}
    excpect = {'memory': 62.5, 'cpu': 10.25, 'disk': 23.2}
    assert data.keys() == excpect.keys()
    assert 0 <= data["memory"] <= 100
    assert 0 <= data["cpu"] <= 100
    assert 0 <= data["disk"] <= 100

    bd = BD.BD(path)
    bd.add_value(data)
    del bd

    d = test_BD.checkBDhasTable(path)
    assert len(d) == 1
    assert d[0][0] == data["memory"]
    assert d[0][1] == data["cpu"]
    assert d[0][2] == data["disk"]
