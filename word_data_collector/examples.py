from voice_getter import Voice
from image_getter import Image
from dictionary_getter import Word, Translation


search_text = "mountain"

voice = Voice(search_text=search_text)
voice.save()

image = Image(search_text=search_text, payload={"count": 2})
image.save()

word = Word(search_text=search_text)
word.save()

translation = Translation(search_text=search_text)
translation.save()
