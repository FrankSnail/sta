# -*- encoding:utf-8 -*-


import datetime


class DateTransformer:
    def __init__(self, source):
        self.name = source.name
        self.source = source
        self.format = "%Y-%m-%d %H:%M:%S"

    def parse(self,datestr):
        datestr = datestr[:-2]
        d = datetime.datetime.strptime(datestr, self.format)
        return d

    def get(self):
        datestr = self.source.get()
        if
        return self.parse(datestr)


    def __iter__(self):
        for datestr in self.source:
            yield self.parse(datestr)