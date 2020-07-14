import json

class HealthCheck(object):
    def on_get(self, req, resp):

        msg = {
            "message": req.params["name"]
        }
        print(req.params["name"])
        resp.body = json.dumps(msg)



