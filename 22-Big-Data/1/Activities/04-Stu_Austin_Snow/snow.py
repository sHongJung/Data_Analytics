from mrjob.job import MRJob

class Snow_Days(MRJob):

    def mapper(self, key, line):
        (staion, name, state, date, snow, tmax, tmin) = line.split(",")
        if snow and float(snow) > 0:
            yield date, 1

    def reducer(self, date, snow):
        yield date, sum(snow)

if __name__ == "__main__":
    Snow_Days.run()
