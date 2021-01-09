# https://en.wikipedia.org/wiki/ISO_639-1
#pip install translate
from translate import Translator
translator=Translator(from_lang='English',to_lang='Ur')
result=translator.translate('Sponsored')
print(result)
