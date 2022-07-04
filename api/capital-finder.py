from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        capital = ""
        if 'country' in dic:
            country_name = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country_name)
            data = r.json()
            for country_data in data:
                country_capital = country_data['capital'][0]
                capital = country_capital

            message = f"the capital of {country_name} is {capital}"

        else:
            message = "Please provide me with a country name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
