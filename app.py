import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from resources.users import ResUsers
from model.users import Users


def user_loader(username, password):
    print(username, password)
    _Users = Users()
    logged_user = _Users.authenticate(username, password)
    if logged_user:
        return {'username': logged_user['name']}
    else:
        return None


auth_backend = BasicAuthBackend(user_loader)
auth_middleware = FalconAuthMiddleware(auth_backend,
                                       exempt_routes=['/exempt'],
                                       exempt_methods=['HEAD'])

app = falcon.API(middleware=[auth_middleware])

users = ResUsers()
app.add_route("/users", users)
