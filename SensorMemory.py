import psutil


class SensorMemory:
    def __init__(self):
        pass

    def parser(self, data):
        if not len(data) > 1 or not (0 <= data[2] <= 100):
            raise ValueError("Invalid data")
        return {"memory": data[2]}

    def loadData(self):
        return psutil.virtual_memory()

    def getData(self):
        return self.parser(self.loadData())

