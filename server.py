import falcon
from falcon_cors import CORS
import pg_plans


cors_public = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True, allow_credentials_all_origins=True)
api = falcon.API(middleware=[cors_public.middleware])


class PGResource:
    cors = cors_public
    def on_get(self, req, resp):
        resp.body = pg_plans.return_sql()


class Hello:
    cors = cors_public
    def on_get(self, req, resp):
        nameString = req.get_param("name")
        lastString = req.get_param("last")
        resp.body = "Hello, " + nameString + " " + lastString



api.add_route('/pg', PGResource())
api.add_route('/hello', Hello())
