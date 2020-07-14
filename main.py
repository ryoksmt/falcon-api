import falcon
from controller import health_check

app = falcon.API()
app.add_route("/", health_check.HealthCheck())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
