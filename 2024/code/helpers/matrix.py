from collections import defaultdict
from itertools import product

DIRS_URDL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS_DIAG = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

class Matrix:
    """
    A multi-dimensional matrix with customizable default values, wrapping, and support for neighbors.

    Attributes:
        size (tuple): Dimensions of the matrix.
        default (any): Default value for unset positions.
        wrap (bool): Whether to wrap around indices that are out of bounds.
    """

    def __init__(self, size, default=0, wrap=False):
        """
        Initialize the Matrix.

        Args:
            size (tuple): The dimensions of the matrix.
            default (any): The default value for unset positions (default: 0).
            wrap (bool): Whether indices should wrap around (default: False).
        """
        self.size = size
        self.default = default
        self.wrap = wrap
        self.matrix = defaultdict(lambda: default)

    def _convert_pos(self, pos):
        """
        Convert a position to a string key, applying wrapping if enabled.

        Args:
            pos (list): The position in the matrix.

        Returns:
            str: The converted position as a key.
        """
        out = []
        if self.wrap:
            for i, elem in enumerate(pos):
                out.append(str(elem % self.size[i]))
        else:
            out = list(map(str, pos))
        return ",".join(out)

    def set(self, pos, val):
        """
        Set the value at a specific position in the matrix.

        Args:
            pos (list): The position in the matrix.
            val (any): The value to set.

        Raises:
            Exception: If the size of `pos` does not match the matrix dimensions.
        """
        if len(pos) != len(self.size):
            raise Exception("Size of pos does not match initialized size.")
        if not self._is_in_bounds(pos):
            return None  # raise IndexError("Cannot SET outside bounds of matrix.")
        self.matrix[self._convert_pos(pos)] = val

    def get(self, pos):
        """
        Get the value at a specific position in the matrix.

        Args:
            pos (list): The position in the matrix.

        Returns:
            any: The value at the position.

        Raises:
            Exception: If the size of `pos` does not match the matrix dimensions.
        """
        if len(pos) != len(self.size):
            raise Exception("Size of pos does not match initialized size.")
        if not self._is_in_bounds(pos):
            return None  # raise IndexError("Cannot GET outside bounds of matrix.")
        return self.matrix[self._convert_pos(pos)]

    def findall(self, val):
        """
        Find all positions in the matrix that contain a specific value.

        Args:
            val (any): The value to search for.

        Yields:
            list: Positions where the value is found.
        """
        out = []
        for k, v in self:
            if val == v:
                out.append(k)
        return out

    def _is_in_bounds(self, pos):
        """
        Check if a position is within the matrix bounds.

        Args:
            pos (list): The position to check.

        Returns:
            bool: True if the position is within bounds, otherwise False.
        """
        if not self.wrap:
            for i in range(len(self.size)):
                if pos[i] < 0 or pos[i] >= self.size[i]:
                    return False
        return True

    def __str__(self):
        """
        Get a string representation of the matrix.

        Returns:
            str: A formatted string of the matrix contents.

        Raises:
            IndexError: If dimensions are not supported for printing.
        """
        out = []
        if len(self.size) == 1:
            for i in range(self.size[0]):
                out.append(str(self.matrix[f"{i}"]))
            return " ".join(out)
        elif len(self.size) == 2:
            for i in range(self.size[0]):
                temp = []
                for j in range(self.size[1]):
                    temp.append(str(self.matrix[f"{i},{j}"]))
                out.append(" ".join(temp))
            return "\n".join(out)
        else:
            raise IndexError("Dimensions do not support printing.")

    def __iter__(self):
        """
        Iterate through all positions and values in the matrix.

        Yields:
            tuple: A tuple containing the position and value.
        """
        pos = [0 for _ in self.size]
        while pos != [x - 1 for x in self.size]:
            yield tuple(pos), self.get(pos)
            i = -1
            pos[i] += 1
            while True:
                if pos[i] == self.size[i]:
                    pos[i] = 0
                    i -= 1
                    pos[i] += 1
                else:
                    break

    def __setitem__(self, key, value):
        """
        Set a value using item assignment syntax.

        Args:
            key (tuple): The position in the matrix.
            value (any): The value to set.
        """
        self.set(list(key), value)

    def __getitem__(self, item):
        """
        Get a value using item access syntax.

        Args:
            item (tuple): The position in the matrix.

        Returns:
            any: The value at the position.
        """
        return self.get(list(item))

    def neighbors(self, pos, diag=False):
        """
        Get the neighbors of a specific position in the matrix.

        Args:
            pos (list): The position to find neighbors for.
            diag (bool): Whether to include diagonal neighbors (default: False).

        Yields:
            tuple: A tuple containing the neighbor position and value.
        
        2024-12-11: I made a breaking change, pos is now a tuple, and the order of outputs is reversed 
        """
        deltas = product([-1, 0, 1], repeat=len(self.size))
        for delta in deltas:
            if not diag and sum(abs(d) for d in delta) != 1:
                continue
            if diag and all(d == 0 for d in delta):
                continue

            neighbor_pos = tuple(p + d for p, d in zip(pos, delta))
            yield neighbor_pos, self.get(neighbor_pos)



def from_grid(din, data_type=str):
    """
    Create a Matrix from a 2D grid.

    Args:
        din (str): A string representing the grid.

    Returns:
        Matrix: The initialized matrix.
    """
    din = din.split("\n")
    M = Matrix((len(din), len(din[0])))
    for y in range(len(din)):
        for x in range(len(din[0])):
            M.set((y, x), data_type(din[y][x]))
    return M
