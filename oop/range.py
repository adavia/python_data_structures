class Range:
    """A class that mimic s the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.
        Semantics is similar to built-in range class.
        """

        if step == 0:
            raise ValueError('Step cannot be 0')
        
        if stop == None:              # special case of range(n) 
            start, stop = 0, start    # should be treated as if range(0,n)

        # Calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""

        return self._length

    def __getitem__(self, key):
        """Return entry at index k (using standard interpretation if negative)."""

        if key < 0:
            key += len(self)  # attempt to convert negative index

        if not 0 <= key < self._length:
            raise IndexError('Index out of range')

        return self._start + key * self._step


r = Range(2, 10, 2)
print(len(r))
print(r[2])
