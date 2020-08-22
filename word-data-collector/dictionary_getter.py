from _base import BaseGetter


class Word(BaseGetter):
    """
    Get and save word data of English words.

    see: https://rapidapi.com/dpventures/api/wordsapi?endpoint=54b6af68e4b02f9493f90b22
    """

    url = "https://wordsapiv1.p.rapidapi.com/words/{}"

    request_method = "get"

    headers = {
        "x-rapidapi-host": "wordsapiv1.p.rapidapi.com",
        "x-rapidapi-key": None,
    }

    payload = {}

    def set_api_key(self, api_key: str):
        self.headers["x-rapidapi-key"] = api_key

    def set_search_text(self, search_text: str):
        self.url = self.url.format(search_text)

    def get_save_file_path(self):
        return '/'.join([self.get_save_dir(), 'word.json'])

    def save(self):
        Word.make_dir(self.get_save_dir())
        res = self.get_response()
        with open(self.get_save_file_path(), mode='wb') as f:
            f.write(res.text.encode())


class Translation(BaseGetter):
    """
    Get and save word translation data of English words.

    see: https://rapidapi.com/googlecloud/api/google-translate1?endpoint=apiendpoint_a5764907-04b6-4d61-869b-79dc5325c739
    """

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    request_method = "post"

    headers = {
        "x-rapidapi-host": "google-translate1.p.rapidapi.com",
        "x-rapidapi-key": None,
        "accept-encoding": "application/gzip",
        "content-type": "application/x-www-form-urlencoded"
    }

    payload = {
        "target": "ja",
        "model": "nmt",
        "format": "text",
        "source": "en",
        "q": None,
    }

    def set_api_key(self, api_key: str):
        self.headers["x-rapidapi-key"] = api_key

    def set_search_text(self, search_text: str):
        self.payload["q"] = search_text

    def get_save_file_path(self):
        return '/'.join([self.get_save_dir(), 'translation.json'])

    def save(self):
        Word.make_dir(self.get_save_dir())
        res = self.get_response()
        with open(self.get_save_file_path(), mode='wb') as f:
            f.write(res.text.encode())
