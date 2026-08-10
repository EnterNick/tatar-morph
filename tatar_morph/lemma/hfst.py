class HFSTLemmatizer:
    def lemmatize(self, word: str) -> str:
        return word.split("<", maxsplit=1)[0]
