import psutil


class SensorMemory:
    def __init__(self):
        pass

    @staticmethod
    def parser(data):
        if not len(data) > 1 or not (0 <= data[2] <= 100):
            raise ValueError("Invalid data")
        return {"memory": data[2]}

    @staticmethod
    def load_data():
        return psutil.virtual_memory()

    def get_data(self):
        return self.parser(self.load_data())

