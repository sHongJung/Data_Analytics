from mrjob.job import MRJob


class BaconCounter(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    BaconCounter.run()
