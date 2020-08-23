import os, sys, hashlib, requests
from base import BaseGetter


class Image(BaseGetter):
    """
    Get and save image data of English words.

    see: https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/bing-image-search1?endpoint=apiendpoint_8f590b01-7545-47e7-840d-1b01d6c89a0d
    """

    url = "https://bing-image-search1.p.rapidapi.com/images/search"

    request_method = "get"

    headers = {
        "x-rapidapi-host": "bing-image-search1.p.rapidapi.com",
        "x-rapidapi-key": None,
    }

    payload = {
        "offset": "0",
        "count": "3",
        "mkt": "ja-JP",
        "q": None
    }

    def set_api_key(self, api_key: str):
        self.headers["x-rapidapi-key"] = api_key

    def set_search_text(self, search_text: str):
        self.payload['q'] = search_text

    def get_save_file_path(self, url):
        extension = os.path.splitext(url)[-1]
        hashed_url = hashlib.md5(url.encode('utf-8')).hexdigest()
        return os.path.join(self.get_save_dir(),
                            hashed_url + extension.lower())

    def save(self):
        Image.make_dir(self.get_save_dir())
        response = self.get_response()
        res = response.json()
        url_list = [v['contentUrl'] for v in res['value']]
        self.__save_files(url_list)

    def __save_files(self, url_list: list):
        for url in url_list:
            try:
                res = requests.get(url, stream=True)
                if res.status_code == 200:
                    file_save_path = self.get_save_file_path(url)
                    with open(file_save_path, 'wb') as f:
                        f.write(res.content)
            except Exception as e:
                print(str(e.with_traceback(sys.exc_info()[2])))
                continue
