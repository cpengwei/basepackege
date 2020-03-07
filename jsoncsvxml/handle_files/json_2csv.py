# encoding:utf-8

import csv
import os


class HandleCsv(object):

    def __init__(self, out_put='output', filename='movies.csv'):
        basepath = os.path.abspath(os.getcwd())
        self.file = '{}/{}/{}'.format(basepath,out_put, filename)

    def write_csv(self, data):
        rows = list(data)
        try:
            with open(self.file, 'w', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                if len(rows) < 1:
                    print('data error')
                    return
                header = rows[0].keys()
                csv_writer.writerow(header)
                for item in rows:
                    row = item.values()
                    csv_writer.writerow(row)
        except Exception as e:
            print(e)
            return

    def write_csv_dict(self,data):
        rows = list(data)
        try:
            with open(self.file,'w',encoding='utf8') as csvfile:
                if len(rows) < 1:
                    print('error data')
                    return
                header = rows[0].keys()
                csv_writer = csv.DictWriter(csvfile, fieldnames=header)
                csv_writer.writeheader()
                csv_writer.writerows(rows)
        except Exception as e:
            print(e)

    def read_csv(self):
        with open(self.file,'r',encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                print(row)

