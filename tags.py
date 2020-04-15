class Tag:
    def __init__(self, tag, is_single=False, *args, **kwargs):
        self.tag = tag
        self.childern = []
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if self.kwargs.get('klass'):
            # TODO: Поставить реализацию из TopLevelTag, а оттуда убрать
            klass = self.kwargs.get('klass')
            attrs = []
            for value in klass:
                attrs.append(f'{value}')
            attrs = " ".join(attrs)
            return f'\t<{self.tag} class="{attrs}">{self.text}</{self.tag}>'
        elif self.is_single:
            print(self.kwargs)
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
    def __str__(self):
        if self.kwargs:
            attrs = []
            for attr in self.kwargs.keys():
                if attr not in attrs:
                    attrs.append(attr)
                    for value in self.kwargs.get('attr'):
            #             TODO: Доделать цикл чтобы сохранял в строку ключ и значение

            attrs = " ".join(attrs)
            element = []
            for cild in self.childern:
                element.append(f'\t\t{cild}\n')
            element = ''.join(element)
            return f'\t<{self.tag} {attrs}>\n{element}\t\t</{self.tag}>'
        else:
            element = []
            for cild in self.childern:
                element.append(f'\t{cild}\n')
            element = ''.join(element)
            return f'\t<{self.tag}>\n{element}\t</{self.tag}>'
