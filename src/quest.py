from bs4 import BeautifulSoup
from unicodedata import normalize

import requests
import wikipedia

erro = """Você acessou uma palavra que já não existe ou está procurando uma página que mudou de endereço."""


class search():

    def __init__(self):
        super(search, self).__init__()
        self.query = ""
        self.suggest = ""
        self.content = ""

    def wiki(self, query):

        self.query = query.lower()

        wikipedia.set_lang("pt")

        self.suggest = str(", ".join([i.lower() for i in wikipedia.search(self.query, results=3)]))

        if self.query in self.suggest:
            self.content = wikipedia.summary(self.query, sentences=2)

        return {"sugestão": self.suggest,
                "pesquisa": self.content
                }

    def dicio(self, query):

        self.query = (normalize('NFKD', query).encode('ASCII', 'ignore').decode('ASCII')).lower()

        html = requests.get("https://www.dicio.com.br/" + self.query)

        bsObj = BeautifulSoup(html.text, "html.parser")

        self.content = str(bsObj.p.get_text()).capitalize()

        if self.content == erro:
            self.suggest = [i.get_text() for i in bsObj.find_all("a", "_sugg")]
            return "Você quis dizer: {}".format(", ".join(self.suggest))
        else:
            return self.content
