class PasswordManager:
    def __init__(self):
        self.password = None

    def create_password(self, new_password):
        self.password = new_password

    def change_password(self, new_password):
        if self.password is not None:
            self.password = new_password
        else:
            print("Es wurde noch kein Passwort erstellt.")

    def delete_password(self):
        self.password = None
