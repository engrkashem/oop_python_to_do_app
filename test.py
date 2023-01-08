

class Test:

    def __init__(self) -> None:
        self.name = ''
        self.all_test = []

    def __repr__(self) -> str:
        return self.name

    def entry(self, name):
        self.name = name
        self.all_test.append(name)


t = Test()
t.entry('hablu')
t.entry('chalak')
t.entry('gadha')

for item in t.all_test:
    print(item)
