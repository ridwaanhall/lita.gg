import requests
from FetchURL.headers_urls import BASE_URL

class DataFetcher:
    def __init__(self, endpoint):
        self.url = BASE_URL + endpoint
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,mt;q=0.8",
            "accesstoken": "",
            "appplat": "Web",
            "appversion": "2.0.0",
            "dnt": "1",
            "l-app-id": "Lita",
            "l-app-platform": "3",
            "l-locale": "in",
            "l-nonce": "F6Kjdp",
            "l-sign": "73e55bb18ca533f",
            "l-timestamp": "1736401973469",
            "l-trace-id": "67719792e69afb51f9bcbab77c7e3a57",
            "l-user-locale": "in",
            "l-user-token": "DeHujIL76cSdXl+RD0+EDEAZEZu+gXhk5eBuXBzgxMe19nv8pngXjnhY1nVXyWaRI6HdPV09z0CWGBK+ghVGLgvy07uiB0GwtcgWeCoTg58=",
            "locale": "in",
            "origin": "https://www.lita.gg",
            "priority": "u=1, i",
            "proxyheader": "eyJjaGVjayI6IkJCQzI0NTJGMTlEQkIyOTFDOUQ2OEEwMUREMTQ1Qjg5IiwidGltZSI6MTczNjQwMTk3MzI0NSwidXNlckxvY2FsZSI6ImluLUlEIiwidmVyc2lvbiI6IjIuMCJ9",
            "referer": "https://www.lita.gg/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "shumeideviceid": "ad06bd58-3608-4195-b6e7-3abee8661301",
            "subappplat": "pc",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
            "userlocale": "in"
        }

    def fetch_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                json_data = response.json()
                if 'status' in json_data and json_data['status'] == '1':
                    status_code = 400
                else:
                    status_code = response.status_code
                return json_data, status_code
            else:
                return response.json(), response.status_code
        except Exception as e:
            print(f"An error occurred: {e}")
            return e, None