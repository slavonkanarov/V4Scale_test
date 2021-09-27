import psutil


class CPUSensor:
    def __init__(self):
        pass

    def loadData(self):
        return [x/psutil.cpu_count() * 100 for x in psutil.getloadavg()]

    def parser(self, data):
        if not len(data) == 3 or not (0 <= data[2] <= 100):
            raise ValueError("Invalid data")
        return {"cpu": data[2]}

    def getData(self):
        return self.parser(self.loadData())

