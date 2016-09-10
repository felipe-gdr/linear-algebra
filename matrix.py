class Matrix(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = coordinates
            self.dimensionX = len(self.coordinates)
            self.dimensionY = len(self.coordinates[0])

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def rows(self):
        return self.dimensionX

    def columns(self):
        return self.dimensionY

    def multiply(self, matrix):
        if(self.columns() != matrix.rows()):
            raise Exception('Number of columns of one matrix should be equal to the number of rows of the other matrix')
        else:
            print ('resulting matrix will have ' + str(self.rows()) + ' rows, and ' + str(matrix.columns()) + ' columns')
            result = []
            for i,x in enumerate(self.coordinates):
                element = 0
                for j,z in enumerate(x):
                    element = element + (z * matrix.coordinates[j][0])
                result.append([element])
            return result

m1 = [[1,0,3,0],
      [0,6,0,8],
      [0,10,11,0],
      [13,0,0,16]]

m2 = [[2],
      [5],
      [4],
      [1]]

print (Matrix(m1).multiply(Matrix(m2)))
