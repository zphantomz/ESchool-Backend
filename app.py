import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from falcon_cors import CORS

from resources import UsersResource, measures, places
from model.users import UsersModel

cors = CORS(allow_all_origins=True)


def user_loader(username, password):
    print(username, password)
    Users = UsersModel()
    logged_user = Users.authenticate(username, password)
    if logged_user:
        return {'username': logged_user['name']}
    else:
        return None


auth_backend = BasicAuthBackend(user_loader)
auth_middleware = FalconAuthMiddleware(auth_backend,
                                       exempt_routes=['/exempt'],
                                       exempt_methods=['HEAD'])

app = falcon.API(middleware=[auth_middleware,
                             cors.middleware])

users = UsersResource()

app.add_route("/users", users)
app.add_route("/measures/{place_id}", measures.Collection())
app.add_route("/places/{place_id}", places.Collection())
