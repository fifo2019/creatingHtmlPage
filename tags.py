class Tag:
    def __init__(self, tag, is_single=False, *args, **kwargs):
        self.tag = tag
        self.childern = []
        self.text = ""
        self.is_single = is_single
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        # Теги с атбрибутами
        if self.kwargs:
            attrs = []
            for attr in self.kwargs.keys():
                if attr not in attrs:
                    # Если атрибута нет в списке добавляем его
                    attrs.append(f' {attr}="'.replace('_', '-'))
                    if type(self.kwargs.get(attr)) != str:
                        # Получаем значения атрибута, если не является строкой распаковываем последовательность
                        attrs.append(' '.join(self.kwargs.get(attr)) + '"')
                    else:
                        # Если строка добавляем к атрибуту
                        attrs.append(self.kwargs.get(attr) + '"')
            # Собираем строку со всеми атрибутами и значениями для тега
            attrs = "".join(attrs).replace('klass', 'class')
            # Заполняем теги атрибутами
            if self.is_single:
                # Непарные теги с атрибутами
                return f'<{self.tag}{attrs}/>'
            else:
                # Парные теги с атрибутами
                if len(self.childern) > 0:
                    # Если тег с атрибутами и имеет вложенные теги
                    element = []
                    for cild in self.childern:
                        element.append(f'\n\t\t\t{cild}')
                    element = ''.join(element)
                    return f'<{self.tag}{attrs}>{element}\n\t\t</{self.tag}>'
                else:
                    # Если тег парный и с атрибутами
                    return f'<{self.tag}{attrs}>{self.text}</{self.tag}>'
        # Теги без атбрибутов
        elif self.is_single:
            # Непарные теги без атрибутов
            return f'<{self.tag}/>'
        else:
            # Парные теги без атрибутов
            # Если тег без атрибутов и имеет вложенные теги
            if len(self.childern) > 0:
                element = []
                for cild in self.childern:
                    element.append(f'\n\t\t\t{cild}')
                element = ''.join(element)
                return f'<{self.tag}>{element}\n\t\t</{self.tag}>'
            else:
                # Если тег парный и без атрибутов
                return f"<{self.tag}>{self.text}</{self.tag}>"

    def __iadd__(self, other):
        self.childern.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return self


class HTML(Tag):
    def __init__(self, tag='html', *args, **kwargs):
        super().__init__(tag, *args, **kwargs)
        self.output = self.kwargs.get('output')

    def __str__(self):
        elements = []
        for cild in self.childern:
            elements.append(f'{cild}')
        elements = ''.join(elements)
        return f'<{self.tag}>\n{elements}</{self.tag}>'

    def __exit__(self, *args, **kwargs):
        if self.output == 'print':
            print(self)
        elif self.output is not None:
            with open(f'{self.output}.html', 'w', encoding='utf-8') as file:
                file.write(f'{self}')
        else:
            print('Нет названия!')


class TopLevelTag(Tag):
    def __str__(self):
        elements = []
        for cild in self.childern:
            elements.append(f'\n\t\t{cild}')
        elements = ''.join(elements)
        return f'\t<{self.tag}>{elements}\n\t</{self.tag}>\n'


