import SensorMemory
import pytest


def test_data():
    sens = SensorMemory.SensorMemory()
    data = sens.loadData()
    assert 0 <= data[2] <= 100


def test_parser():
    sens = SensorMemory.SensorMemory()
    data = (17073377280, 1185316864, 93.1, 15888060416, 1185316864)
    res = sens.parser(data)
    expect = {"memory": 93.1}
    assert res == expect


def test_parser_wrong_value_1():
    sens = SensorMemory.SensorMemory()
    data = (17073377280, 1185316864, 100.1, 15888060416, 1185316864)
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_2():
    sens = SensorMemory.SensorMemory()
    data = (17073377280, 1185316864, 15888060416, 1185316864)
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_3():
    sens = SensorMemory.SensorMemory()
    data = ()
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_get_data():
    sens = SensorMemory.SensorMemory()
    data = sens.getData()
    expect = {"memory": 93.1}
    assert data.keys() == expect.keys()
    assert 0 <= data["memory"] <= 100

