class Operation:
    stuff = list()

    def operate(self, handler, to_put):
        with open(handler, encoding="utf-8") as f:
            read_data = f.read()

            for line in read_data.split('\n'):
                if line.startswith('From zqian'):
                    self.stuff.append(line)
                else:
                    continue

            with open(to_put, 'w', encoding="utf-8") as p:
                p.write('\n'.join(self.stuff))


reading = Operation()

reading.operate('../mailbox.txt', '../froms.txt')