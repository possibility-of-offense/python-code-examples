class Counting:
    line_counts = 0

    def __init__(self):
        print('I have a child class')

    def increase_line_counts(self, n):
        self.line_counts = n

# Operation class

class Operation(Counting):
    def __init__(self):
        self.stuff = list()
        super().__init__()

    def operate(self, handler, to_put):
        with open(handler, encoding="utf-8") as f:
            read_data = f.read()

            for line in read_data.split('\n'):
                if line.startswith('From zqian'):
                    self.increase_line_counts(self.line_counts + 1)
                    self.stuff.append(line)
                else:
                    continue

            with open(to_put, 'w', encoding="utf-8") as p:
                p.write('\n'.join(self.stuff))

                print(self.line_counts)


reading = Operation()
reading.operate('../mailbox.txt', '../froms.txt')