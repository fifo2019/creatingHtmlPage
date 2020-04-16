class Tag:
    def __init__(self, tag, parent=False, is_single=False, *args, **kwargs):
        self.tag = tag
        self.childern = []
        self.text = ""
        self.parent = parent
        self.is_single = is_single
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if self.kwargs:
            # TODO: ОТЛАДИТЬ ТУТ - РАБОТАЕТ НЕ КОРРЕКТНО - ЗАТИРАЕТ ВЛОЖЕННЫЙ ТЕКСТ!!!!
            print(self.kwargs)
            attrs = []
            for attr in self.kwargs.keys():
                if attr not in attrs:
                    attrs.append(f' {attr}="')
                    if type(self.kwargs.get(attr)) != str:
                        attrs.append(' '.join(self.kwargs.get(attr)) + '"')
                    else:
                        attrs.append(self.kwargs.get(attr) + '"')
            attrs = "".join(attrs).replace('klass', 'class')
            element = []
            for cild in self.childern:
                element.append(f'\t\t{cild}\n')
            element = ''.join(element)
            return f'\t<{self.tag}{attrs}>\n{element}\t\t</{self.tag}>'
        elif self.parent:
            element = []
            for cild in self.childern:
                element.append(f'\t{cild}\n')
            element = ''.join(element)
            return f'\t<{self.tag}>\n{element}\t</{self.tag}>'
        elif self.is_single:
            return f'\t<{self.tag}>'
        else:
            return f"\t<{self.tag}>{self.text}</{self.tag}>"

    def __iadd__(self, other):
        self.childern.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return self


class HTML(Tag):
    def __init__(self, tag='html', output=None):
        super().__init__(tag)
        self.output = output

    def __str__(self):
        element = [f'<{self.tag}>\n']
        for cild in self.childern:
            element.append(f'{cild}\n')
        element.append(f'</{self.tag}>\n')
        return ''.join(element)

    def __exit__(self, *args, **kwargs):
        if self.output == 'print':
            print(self)
        elif self.output is not None:
            try:
                # TODO: Убрать перезапись  на х
                with open(f'{self.output}.html', 'w', encoding='utf-8') as file:
                    element = []
                    for cild in self.childern:
                        element.append(f'{cild}\n')
                    element = ''.join(element)
                    file.write(f'<{self.tag}>\n{element}</{self.tag}>\n')
            except FileExistsError:
                print('Файл с таким именем уже существует!')
        else:
            print('Нет названия!')


class TopLevelTag(Tag):
    def __init__(self, tag, parent=True, *args, **kwargs):
        super().__init__(tag, parent, *args, **kwargs)

