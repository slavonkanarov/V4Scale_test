import psutil


class DiskSensor:
    def __init__(self):
        pass

    def loadData(self):
        return psutil.disk_usage("/")

    def parser(self, data):
        if not len(data) == 4 or not (0 <= data[3] <= 100):
            raise ValueError("Invalid data")
        return {"disk": data[3]}

    def getData(self):
        return self.parser(self.loadData())
