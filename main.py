class GeneratorIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield self.generator(item)

    def generator(self, item):
        return item ** 2

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    gen_iterable = GeneratorIterable(data)
    for result in gen_iterable:
        print(result)
