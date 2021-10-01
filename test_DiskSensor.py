import DiskSensor
import pytest


def test_data():
    sens = DiskSensor.DiskSensor()
    data = sens.load_data()
    assert 0 <= data[3] <= 100


def test_parser():
    sens = DiskSensor.DiskSensor()
    data = (47868325888, 10504130560, 34902138880, 23.1)
    res = sens.parser(data)
    excpect = {"disk": 23.1}
    assert res == excpect


def test_parser_wrong_value_1():
    sens = DiskSensor.DiskSensor()
    data = (47868325888, 10504130560, 34902138880, 523.1)
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_2():
    sens = DiskSensor.DiskSensor()
    data = (47868325888, 34902138880, 23.1)
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_3():
    sens = DiskSensor.DiskSensor()
    data = ()
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_get_data():
    sens = DiskSensor.DiskSensor()
    data = sens.get_data()
    expect = {"disk": 93.1}
    assert data.keys() == expect.keys()
    assert 0 <= data["disk"] <= 100

