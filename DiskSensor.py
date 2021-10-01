import psutil


class DiskSensor:
    def __init__(self):
        pass

    @staticmethod
    def load_data():
        return psutil.disk_usage("/")

    @staticmethod
    def parser(data):
        if not len(data) == 4 or not (0 <= data[3] <= 100):
            raise ValueError("Invalid data")
        return {"disk": data[3]}

    def get_data(self):
        return self.parser(self.load_data())
