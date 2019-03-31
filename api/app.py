import responder
from changing_country import ChangingCountry

api = responder.API()
country = ChangingCountry()


@api.route("/")
def get_country(req, resp):
    resp.media = country.country


if __name__ == "__main__":
    api.run(port=5000)
