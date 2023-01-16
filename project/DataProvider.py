from typing import Union, Any
import requests


class DataProvider(object):
    def __init__(self, send_msg, my_settings):
        self.send_msg = send_msg
        self.setting = my_settings

    def get_url_data(self, title, *args) -> Union[None, Any]:
        result = {}
        try:
            url = self.setting["req_url"][title].format(*args)
            content = self.requests_data(url)
            if content is not None:
                result = content
        except:
            self.send_msg(msg=f"Title:{title}, Args:{args}, Url:{url}")
        return result

    def requests_data(self, url):
        with requests.Session() as session:
            try:
                respone = session.get(url, headers=self.setting["headers"], timeout=60)
                status_code = respone.status_code
                if status_code != 200:
                    self.send_msg(f"請求非200, Url: {url}, Status Code: {status_code}, Content:{respone.text}")
                    return None
            except:
                self.send_msg()
                return None
        return respone.json()
