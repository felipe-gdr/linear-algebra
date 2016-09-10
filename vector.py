import math
from decimal import *

getcontext()
Context(prec=6, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999,
        capitals=1, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
getcontext().prec=6
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

    # Check whether two vectors are parallel to each other
    # by verifying if the angle they form is equal to 0 or
    # 180 degrees
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

    # Finds out the Vector which is the parallel
    # projection of self to a basis vector
    # 'proj b (v) or v||'
    def component_parallel_to(self, basis):
        norm_b = basis.normalized()
        weight = self.dot(norm_b)
        return norm_b.times_scalar(weight)

    # Finds out the Vector which is the orthogonal
    # projection of self to a basis vector
    # 'v perp'
    def component_orthogonal_to(self, basis):
        proj = self.component_parallel_to(basis)
        return self.minus(proj)

    # Finds out the 'cross product' between 2 Vectors.
    # Cross Product is a vector which is orthogonal
    # (perpendicular) to both vectors
    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                              -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1 ]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack' :
                self_embedded_in_R3 = Vector(self.coordinates + (0,))
                v_embedded_in_R3 = Vector(v.coordinates + (0,))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                raise Exception('Only denifed in 2 or 3 dimensions')

    # Finds out the area covered by the parallelogram
    # formed by 2 Vectors
    def area_of_parallelogram_with(self, v):
        return self.cross(v).magnitude()

    # Finds out the area covered by the rectangle
    # formed by 2 Vectors. This area is half the
    # area of the parallelogram formed by both Vectors
    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])
print( v1.cross(v2))

v3 = Vector([-8.987, -9.838, 5.031])
v4 = Vector([-4.268, -1.861, -8.866])
print( v3.area_of_parallelogram_with(v4) )

v5 = Vector([1.5, 9.547, 3.691])
v6 = Vector([-6.007, 0.124, 5.772])
print( v5.area_of_triangle_with(v6) )
