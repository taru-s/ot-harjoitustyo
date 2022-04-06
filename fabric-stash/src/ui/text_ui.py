from services import fabric_service


class TextUI:
    def __init__(self) -> None:
        self._service = fabric_service.FabricService()

    def start(self):
        print("Fabric stash manager")
        while True:
            print("\ncommands:\nx - exit\nadd - add new fabric\nlist - list all fabrics")
            user_input = input(" > ")

            if user_input == "x":
                break
            elif user_input == "add":
                self._add_fabric()
            elif user_input == "list":
                self._list_fabrics()

    def _add_fabric(self):
        name = input("give fabric name: ")
        width = input("give fabric width in cm: ")
        length = input("give fabric length in cm: ")
        washed_str = input("is fabric washed? y/n ")
        if washed_str == "y":
            washed = True
        else:
            washed = False

        self._service.add_fabric(name, length, width, washed)

    def _list_fabrics(self):
        fabrics = self._service.get_fabrics()
        for fabric in fabrics:
            print(fabric)
