from _base import BaseGetter


class Voice(BaseGetter):
    """
    Get and save voice data of English words.

    see: https://rapidapi.com/HiBrainy/api/text-to-speech5
    """

    url = "https://text-to-speech5.p.rapidapi.com/api/tts"

    request_method = "post"

    headers = {
        "x-rapidapi-host": "text-to-speech5.p.rapidapi.com",
        "content-type": "application/x-www-form-urlencoded",
        "x-rapidapi-key": None,
    }

    payload = {
        "tech": "deep",
        "language": "en",
        "text": None,
    }

    def set_api_key(self, api_key: str):
        self.headers["x-rapidapi-key"] = api_key

    def set_search_text(self, search_text: str):
        self.payload['text'] = search_text

    def get_save_file_path(self):
        return '/'.join([self.get_save_dir(), 'voice.mp3'])

    def save(self):
        Voice.make_dir(self.get_save_dir())
        res = self.get_response()
        with open(self.get_save_file_path(), mode='wb') as f:
            f.write(res.content)
