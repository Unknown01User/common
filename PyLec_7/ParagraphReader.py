class ParagraphReader:
    def __init__(self, text, paragraph_sign = "@"):
        self._text = text.split(paragraph_sign)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._text):
            paragraph, self._index = self._text[self._index], self._index + 1
            return paragraph
        raise StopIteration


text = " paragraph #1@ paragraph #2@ paragraph #3"
reader = ParagraphReader(text)
for paragraph in reader:
    print(paragraph)
