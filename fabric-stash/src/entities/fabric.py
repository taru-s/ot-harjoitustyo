class Fabric:
    def __init__(self, name, width=0, length=0, washed=0) -> None:
        """Creates a Fabric object

        Args:
            name (str): name of the fabric
            width (int, optional): Width of fabric in centimeters. Defaults to 0.
            length (int, optional): Length of fabric in centimeters. Defaults to 0.
            washed (int, optional): Has the fabric been washed? Can be 0 for false
                                    or 1 for true. Defaults to 0.
        """
        self._name = name
        self._width = width
        self._length = length
        self._washed = washed

    def __str__(self) -> str:
        if self.washed == 1:
            washed = "yes"
        else:
            washed = "no"

        return f"{self.name}, {self.width}cm x {self.length}cm, washed: {washed}"

    @classmethod
    def properties_and_types(cls):
        properties_and_types = {
            "name": str,
            "width": int,
            "length": int,
            "washed": bool
        }
        return properties_and_types

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: int):
        if isinstance(width, int):
            self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: int):
        if isinstance(length, int):
            self._length = length

    @property
    def washed(self):
        return self._washed

    @washed.setter
    def washed(self, washed):
        if washed in (1, 0):
            self._washed = washed

    def get_values(self):
        values = [self.name, self.width, self.length, self.washed]
        return values
