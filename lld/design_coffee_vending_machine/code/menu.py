from eums.menu_options import MenuOption


class Menu:
    def __init__(self):
        self.__name = None
        self.__options = MenuOption.NORMAL_USER

    def show_menu(self):
        return self.__options

    def add_menu_item(self):
        pass

    def remove_menu_item(self):
        pass
