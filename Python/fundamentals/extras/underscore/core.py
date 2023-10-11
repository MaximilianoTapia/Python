class Underscore:
    def map(self, iterable, callback):
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None

    def filter(self, iterable, callback):
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    def reject(self, iterable, callback):
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result

# Creemos una instancia de nuestra clase
_ = Underscore()

# Ejemplos de uso
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)  # Debería devolver [2, 4, 6]

squared = _.map([1, 2, 3, 4, 5], lambda x: x**2)
print(squared)  # Debería devolver [1, 4, 9, 16, 25]

first_even = _.find([1, 3, 5, 7, 8, 9], lambda x: x % 2 == 0)
print(first_even)  # Debería devolver 8

odd_numbers = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(odd_numbers)  # Debería devolver [1, 3, 5]
