import psutil


class CPUSensor:
    def __init__(self):
        pass

    @staticmethod
    def load_data():
        return [x/psutil.cpu_count() * 100 for x in psutil.getloadavg()]

    @staticmethod
    def parser(data):
        if not len(data) == 3 or not (0 <= data[2] <= 100):
            raise ValueError("Invalid data")
        return {"cpu": data[2]}

    def get_data(self):
        return self.parser(self.load_data())

