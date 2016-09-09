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
        # l = list()
        # for i,a in enumerate(self.coordinates):
        #     l.append(a - vector.coordinates[i])

        return Vector(l)

    def times_scalar (self,num):
        l = [num*x for x in self.coordinates]
        # l = list()
        # for i,a in enumerate(self.coordinates):
        #     l.append(a * num)

        return Vector(l)

print Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111]))
print Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878]))
print Vector([1.671, -1.012, -0.318]).times_scalar(7.41)
