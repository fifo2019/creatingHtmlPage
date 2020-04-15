import os

class HTML:
    """ Определяет, куда сохранять вывод: на экран через print или в файл """
    def __init__(self, output):
        self.output = output

    def __str__(self):
        return f'{self.output}'

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.output == 'print':
            print(self)
        else:
            try:
                with open(f'{self.output}.html', 'x', encoding='utf-8') as file:
                    file.write(self.output)
            except FileExistsError:
                print('Файл с таким именем уже существует!')


class TopLevelTag:
    """ Создает теги которые не содержат внутреннего текста и всегда парные """
    pass


class Tag(TopLevelTag):
    """ Создает теги которые могут быть непарные или быть парные и содержать текст внутри себя """
    pass