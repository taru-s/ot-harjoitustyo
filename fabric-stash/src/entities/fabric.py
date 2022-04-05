class Fabric:
    def __init__(self, name, width=0, length=0, washed=False) -> None:
        self.name = name
        self.width = width
        self.length = length
        self.washed = washed

    def __str__(self) -> str:
        return f"{self.name}, {self.width}cm x {self.length}cm"