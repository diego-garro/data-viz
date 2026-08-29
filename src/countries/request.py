import requests

REST_EU_ROOT_URL = "https://api.restcountries.com/countries/v5"


def REST_country_request(field="all", name=None, params=None):

    # headers = {"User-Agent": "Mozilla/5.0"}
    headers = {"Authorization": "Bearer rc_live_demo"}

    if not params:
        params = {}

    if field == "all":
        response = requests.get(REST_EU_ROOT_URL + "/all")
        return response.json()

    url = "%s/%s/%s" % (REST_EU_ROOT_URL, field, name)
    print("Requesting URL: " + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception("Request failed with status code " + str(response.status_code))

    return response.json()


response = REST_country_request("currency", "usd")
print(response)
