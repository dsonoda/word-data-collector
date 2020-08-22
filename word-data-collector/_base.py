import requests
import os


class BaseGetter:
    """
    base getter class
    """

    url = None

    request_method = None

    headers = None

    payload = None

    def __init__(self, search_text: str, payload: dict = None,
                 api_key: str = None, save_path: str = None):
        """
        constructor

        :param search_text: search text.
        :param payload: request data.
        :param api_key: rapidapi api_key.
            see: https://rapidapi.com/
        :param save_path: directory path to save the data acquired by API.
        """

        self.__search_text = search_text.strip()
        self.__set_payload(payload)
        self.set_search_text(search_text)

        if not api_key:
            api_key = os.environ.get("WORDDATACOLLECTOR_API_KEY")
        self.set_api_key(api_key)

        if not save_path:
            save_path = os.environ.get("WORDDATACOLLECTOR_SAVE_DIR")
        self.__save_path = save_path

    def __set_payload(self, payload: dict = None):
        payload = payload or {}
        self.payload = {k: payload.get(k) if payload.get(k, None) else v for
                        k, v in self.payload.items()}

    @staticmethod
    def make_dir(path: str):
        if not os.path.isdir(path):
            os.makedirs(path)

    def get_response(self):
        params = {
            "method": self.request_method,
            "url": self.url,
            "headers": self.headers,
        }
        if self.request_method.lower() == "get":
            params["params"] = self.payload
        else:
            params["data"] = self.payload
        return requests.request(**params)

    def get_save_dir(self):
        save_dir_name = self.__class__.__name__.lower()
        search_text = self.__search_text.strip().replace(' ', '_')
        return '/'.join([self.__save_path, save_dir_name, search_text])

    def set_api_key(self, api_key: str):
        raise NotImplementedError()

    def set_search_text(self, search_text: str):
        raise NotImplementedError()

    def get_save_file_path(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()

