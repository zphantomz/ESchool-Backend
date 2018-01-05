import json


class ResUsers(object):
    auth = {'auth_disabled': True}

    def on_get(self, req, resp):
        users = {'name': 'pippo',
                 'description': 'descrizione'
                 }
        resp.body = json.dumps(users, ensure_ascii=False)
