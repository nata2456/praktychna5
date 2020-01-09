class Text:
    def __init__(self, text, subject):
        self.text = text
        self.sub = subject

    def set_text(self, sym):
        self.text = sym

    def get_text(self):
        return self.text

    def set_sub(self, word):
        self.text = word

    def get_sub(self):
        return self.sub

    def word_count(self):
        return len(str(self.text))

    def gap_count(self):
        return self.text.count(' ')

    def let_replace(self):
        return self.text.replace('g', 'h')

    def __str__(self):
        return str(self.text)


t = Text('goodbye, my darling', 'polite words')
print('message: ', t)
t1 = t.word_count()
print('count of letters: ', t1)
t2 = t.gap_count()
print('count of gaps: ', t2)
t3 = t.let_replace()
print('replace letters: ', t3)

