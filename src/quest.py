import wikipedia


class wiki():

    def __init__(self):
        super(wiki, self).__init__()
        self.query = ""
        self.summary = ""
        self.suggest = ""

    def search(self, query):

        self.query = query

        wikipedia.set_lang("pt")

        self.suggest = wikipedia.search(self.query, results=3)

        self.suggest = [i.lower() for i in self.suggest]

        if str(self.query) in self.suggest:
            self.summary = wikipedia.summary(self.query, sentences=2)

        self.suggest = str(self.suggest)

    def __repr__(self):
        return 'Sugestão: {}\n\nPesquisa: {}'.format(self.suggest, self.summary)