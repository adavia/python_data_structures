class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""

        self._coords = [0] * d

    def __len__(self):
        """Return the dimention of the vector"""

        return len(self._coords)

    def __getitem__(self, key):
        """Return item coordinate of vector."""

        return self._coords[key]

    def __setitem__(self, key, value):
        """Set item coordinate of vector to given value."""

        self._coords[key] = value

    def __add__(self, other):
        """Return sum of two vectors."""

        if len(self) != len(other):
            raise ValueError('Dimentions of both vectors must be equal')

        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] + other[i]

        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""

        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""

        return not self == other

    def __str__(self):
        """Produce string representation of vector."""

        return  "<{}>".format(str(self._coords)[1:-1])

a = Vector(3)
a[0] = 2
a[1] = 5
a[2] = 3
b = Vector(3)
b[0] = 2
b[1] = 5
b[2] = 3

print(a + b)

print(range(8, 140, 5))
    



        

