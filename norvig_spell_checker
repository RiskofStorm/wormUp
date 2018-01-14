class SpellCheker(object):
    def __init__(self, model):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.model = SpellCheker.train()

    @staticmethod
    def train():
        data = re.findall('[a-z]+', open('big_train.txt').read().lower())
        model = collections.defaultdict(lambda: 1)
        for word in data:
            model[word] += 1
        return model

    def stochastic(self, word):
        n = len(word)
        deletion = [word[0:i] + word[i + 1:] for i in range(n)]
        transposition = [word[i] + word[i + 1] + word[:i] + word[i + 2:] for i in range(n - 1)]
        alteration = [word[:i] + a + word[i + 1:] for i in range(n) for a in self.alphabet]
        insertion = [word[:i] + a + word[i:] for i in range(n + 1) for a in self.alphabet]
        probability = set(deletion + transposition + alteration + insertion)
        return probability

    def prob_count(self, word):
        return set(b for a in self.stochastic(word) for b in self.stochastic(a) if b in self.model)

    def known_words(self, words):
        return set(a for a in words if a in self.model)

    def correct(self, word):
        simillar = self.known_words([word]) or self.known_words(self.stochastic(word)) or self.prob_count(word) or [
            word]
        return max(simillar, key=lambda a: self.model[a])
