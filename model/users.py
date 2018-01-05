users = [{'name': 'user1', 'password': 'user1', 'description': 'descrizione utente1'},
         {'name': 'user2', 'password': 'user2', 'description': 'descrizione utente2'}
         ]


class Users(object):
    def __init__(self):
        self.users = users

    def authenticate(self, username, password):
        user = [u for u in self.users
                if u['name'] == username and u['password'] == password]
        print(user)
        if len(user) > 0:
            return user[0]
        else:
            return None
