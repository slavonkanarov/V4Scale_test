import psutil
import os
import sqlite3
import SensorMemory
import CPUSensor
import DiskSensor
import BD
import test_BD
import time


def main():
    # Use a breakpoint in the code line below to debug your script.
    bd = BD.BD("main.sqlite")

    memsens = SensorMemory.SensorMemory()
    cpusens = CPUSensor.CPUSensor()
    disksens = DiskSensor.DiskSensor()
    data = {**memsens.getData(), **cpusens.getData(), **disksens.getData()}
    print(data)
    bd.addValue(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
