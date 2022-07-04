from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        country = ""
        if 'capital' in dic:
            capital_name = dic['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital_name)
            data = r.json()
            for country_data in data:
                country = country_data['name']['common']

            message = f" {capital_name} is the capital of  {country}"

        else:
            message = "Please provide me with a capital name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
