import CPUSensor
import pytest


def test_data():
    sens = CPUSensor.CPUSensor()
    data = sens.load_data()
    assert 0 <= data[2] <= 100


def test_parser():
    sens = CPUSensor.CPUSensor()
    data = [29.5, 15.25, 10.25]
    res = sens.parser(data)
    expect = {"cpu": 10.25}
    assert res == expect


def test_parser_wrong_value_1():
    sens = CPUSensor.CPUSensor()
    data = [29.5, 15.25, 100.25]
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_2():
    sens = CPUSensor.CPUSensor()
    data = [29.5, 10.25]
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_parser_wrong_value_3():
    sens = CPUSensor.CPUSensor()
    data = []
    with pytest.raises(ValueError):
        res = sens.parser(data)


def test_get_data():
    sens = CPUSensor.CPUSensor()
    data = sens.get_data()
    expect = {"cpu": 93.1}
    assert data.keys() == expect.keys()
    assert 0 <= data["cpu"] <= 100

