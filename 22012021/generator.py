class CardGenerator:
    @staticmethod
    def generate_card(self):
        from random import randint
        s = set()
        with open('generator_card.txt', 'r+', encoding='utf-8') as template:
            while len(s) < 15:
                template.seek(0)
                file = template.read()
                number = str(randint(1, 91))
                if number not in s:
                    s.add(number)
                    if len(number) == 1:
                        file = file.replace('**', ' ' + number, 1)
                    else:
                        file = file.replace('**', number, 1)
                    template.seek(0)
                    template.write(file)
                else:
                    continue