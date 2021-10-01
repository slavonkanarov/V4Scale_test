import sqlite3
import copy


class BD:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE if not exists data
               (memory real, cpu real, disk real)''')
        self.con.commit()

    def add_value(self, value: dict):
        cur = self.con.cursor()
        keys = ["memory", 'cpu', 'disk']
        if len([0 for key in keys if key not in value.keys()]) != 0:
            raise ValueError("Invalid data")

        cur.execute(f"insert into data values ({value['memory']}, {value['cpu']}, {value['disk']})")
        self.con.commit()

    def __del__(self):
        self.con.close()
