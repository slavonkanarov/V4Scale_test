import SensorMemory
import CPUSensor
import DiskSensor
import BD


def main():
    bd = BD.BD("main.sqlite")

    memsens = SensorMemory.SensorMemory()
    cpusens = CPUSensor.CPUSensor()
    disksens = DiskSensor.DiskSensor()
    data = {**memsens.get_data(), **cpusens.get_data(), **disksens.get_data()}
    print(data)
    bd.add_value(data)


if __name__ == '__main__':
    main()
