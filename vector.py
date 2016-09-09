import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus (self,vector):
        l = [x+y for x,y in zip(self.coordinates, vector.coordinates)]

        # l = list()
        # for i,a in enumerate(self.coordinates):
        #     l.append(a + vector.coordinates[i])

        return Vector(l)

    def minus (self,vector):
        l = [x-y for x,y in zip(self.coordinates, vector.coordinates)]

        return Vector(l)

    def times_scalar (self,num):
        l = [num*x for x in self.coordinates]

        return Vector(l)

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus (self,vector):
        l = [x+y for x,y in zip(self.coordinates, vector.coordinates)]

        # l = list()
        # for i,a in enumerate(self.coordinates):
        #     l.append(a + vector.coordinates[i])

        return Vector(l)

    def minus (self,vector):
        l = [x-y for x,y in zip(self.coordinates, vector.coordinates)]

        return Vector(l)

    def times_scalar (self,num):
        l = [num*x for x in self.coordinates]

        return Vector(l)

    # Calculates the 'magnitude' of the Vector.
    # The magnitude represents the total distance
    # covered by the Vector. It is calculated using
    # the Pythagoras Theorem
    def magnitude (self):
        squares = [x*x for x in self.coordinates]
        squareSum = 0
        for x in squares:
            squareSum = squareSum + x

        return math.sqrt(squareSum)

    # Calculates the 'direction' or 'normalization' of the Vector.
    # The direction is a normalized Vector, with magnitude of 1,
    # which points in the same direction as the original Vector
    def direction(self):
        mag = self.magnitude()

        return self.times_scalar(1/mag)

print Vector([-0.221,7.437]).magnitude()
print Vector([8.813, -1.331, -6.247]).magnitude()
print Vector([5.581, -2.136]).direction()
print Vector([1.996, 3.108, -4.554]).direction()
