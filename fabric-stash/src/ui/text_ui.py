from services import fabric_service


class TextUI:
    def __init__(self) -> None:
        self._service = fabric_service.FabricService()
        self.commands = {"x": "exit",
                         "add": "add new fabric",
                         "list": "list all fabrics",
                         "s": "search for fabric by name"}

    def print_commands(self):
        print("\ncommands: ")
        for command, definition in self.commands.items():
            print(f"{command} - {definition}")

    def start(self):
        print("Fabric stash manager")
        while True:
            self.print_commands()
            user_input = input(" > ")

            if user_input == "x":
                break
            elif user_input == "add":
                self._add_fabric()
            elif user_input == "list":
                self._list_fabrics()
            elif user_input == "s":
                self._search_by_name()

    def _add_fabric(self):
        name = input("give fabric name: ")
        width = input("give fabric width in cm: ")
        length = input("give fabric length in cm: ")
        washed_str = input("is fabric washed? y/n ")
        if washed_str == "y":
            washed = True
        else:
            washed = False

        self._service.add_fabric(name, width, length, washed)

    def _list_fabrics(self):
        fabrics = self._service.get_all_fabrics()
        for fabric in fabrics:
            print(fabric)

    def _search_by_name(self):
        name = input("give fabric name: ")
        fabric_found = self._service.get_fabric_by_name(name)
        if fabric_found:
            print(fabric_found)
        else:
            print("no fabric found with the name provided")
