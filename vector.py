import math
from decimal import *

getcontext()
Context(prec=10, rounding=ROUND_HALF_DOWN, Emin=-999999999, Emax=999999999,
        capitals=1, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
getcontext().prec=10
class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,vector):
        l = [x+y for x,y in zip(self.coordinates, vector.coordinates)]

        # l = list()
        # for i,a in enumerate(self.coordinates):
        #     l.append(a + vector.coordinates[i])

        return Vector(l)

    def minus(self,vector):
        l = [x-y for x,y in zip(self.coordinates, vector.coordinates)]

        return Vector(l)

    def times_scalar(self,num):
        l = [Decimal(num)*x for x in self.coordinates]

        return Vector(l)

    # Calculates the 'magnitude' of the Vector.
    # The magnitude represents the total distance
    # covered by the Vector. It is calculated using
    # the Pythagoras Theorem
    def magnitude(self):
        squares = [x**2 for x in self.coordinates]
        return Decimal(math.sqrt(sum(squares)))

    # Calculates the 'direction' or 'normalization' of the Vector.
    # The direction is a normalized Vector, with magnitude of 1,
    # which points in the same direction as the original Vector
    def normalized(self):
        try:
            mag = self.magnitude()
            return self.times_scalar(Decimal('1.0')/mag)
        except ZeroDivisionError:
            raise Exception(CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    # Calculates the 'dot product' between two vectors
    def dot(self, vector):
        return sum([x*y for x,y in zip(self.coordinates, vector.coordinates)])

    # Calculates the angle formed between two Vectors, considering both have the same
    # origin point. The smallest angle is considered
    def angle_with(self, vector, in_degrees=False):
        # try:
            # My Way
            # product = self.dot(vector)
            # mag1 = self.magnitude()
            # mag2 = vector.magnitude()
            # angle_in_radians = math.acos(product / (mag1 * mag2))

            # Udacity's way
            u1 = self.normalized()
            u2 = vector.normalized()
            angle_in_radians = math.acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        # except Exception as e:
        #     if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
        #         raise Exception('Cannot compute an angle with the zero vector')
        #     else:
        #         raise e

    # Check whether this Vector is a 'Zero Vector',
    # that is, a Vector with a magnitude of 0.
    # We use a tolerance in this function
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, vector):
        return (self.is_zero() or
                vector.is_zero() or
                math.isclose(self.angle_with(vector), 0, abs_tol=1e-3) or
                math.isclose(self.angle_with(vector),math.pi, abs_tol=1e-3))

    # Check whether a Vector is orthogonal to another Vector.
    # Two vectors are orthogonals to each other if they form
    # a 90 degrees angle. This happens when their dot product is
    # equal to 0 (in this method we compare the dot product with
    # a very small number close to zero, in order to avoid
    # negative falses).
    def is_orthogonal_to(self, vector, tolerance=1e-10):
        return abs(self.dot(vector)) < tolerance

v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print (v1.is_parallel_to(v2))
print (v1.is_orthogonal_to(v2))

v3 = Vector([-2.029, 9.97, 4.172])
v4 = Vector([-9.231, -6.639, -7.245])
print (v3.is_parallel_to(v4))
print (v3.is_orthogonal_to(v4))

v5 = Vector([-2.328, -7.284, -1.214])
v6 = Vector([-1.821, 1.072, -2.94])
print (v5.is_parallel_to(v6))
print (v5.is_orthogonal_to(v6))

v7 = Vector([-2.328, -7.284, -1.214])
v8 = Vector([0,0,0])
print (v7.is_parallel_to(v8))
print (v7.is_orthogonal_to(v8))
