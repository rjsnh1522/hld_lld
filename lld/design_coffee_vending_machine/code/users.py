class Account:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, username, password):
        super(Admin, self).__init__(username, password)

    def add_menu_item(self):
        pass

    def remove_menu_item(self):
        pass

