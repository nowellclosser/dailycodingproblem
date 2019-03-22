# This problem was asked by Microsoft.

# Implement the singleton pattern with a twist. First, instead of storing one
# instance, store two instances. And in every even call of getInstance(),
# return the first instance and in every odd call of getInstance(),
# return the second instance.


class Example():
    pass


class Doubleton():
    get_count = 0

    def __init__(self, cls):
        self.instance_1 = cls()
        self.instance_2 = cls()

    def get_instance(self):
        self.get_count += 1

        if self.get_count % 2 == 1:
            return self.instance_2

        return self.instance_1

if __name__ == '__main__':
    x = Doubleton(Example)
    print(
        x.get_instance(),
        x.get_instance(),
        x.get_instance(),
        x.get_instance()
    )


# Analysis: They disallow creation via the constructor and don't use a second
# class, which I think is closer to the true singleton pattern, but the core
# of this is the class variable to keep track of gets.
