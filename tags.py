class Tag:
    def __init__(self, tag, is_parent=False, is_single=False, *args, **kwargs):
        self.tag = tag
        self.childern = []
        self.text = ""
        self.is_parent = is_parent
        self.is_single = is_single
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if self.kwargs:
            # Если в теги есть атрибуты
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
            if self.is_single:
                # Если тег одиночный
                return f'\t<{self.tag}{attrs}/>'
            if self.is_parent:
                # Если тег является родителем
                element = []
                for cild in self.childern:
                    element.append(f'\t{cild}\n')
                element = '\t'.join(element)
                return f'\t<{self.tag}{attrs}>\n\t{element}\t\t</{self.tag}>'
            else:
                # Если тег вложенный и с атрибутами
                return f'\t<{self.tag}{attrs}>{self.text}</{self.tag}>'
        elif self.is_single:
            # Если тег одиночный и без атрибутов
            return f'\t<{self.tag}/>'
        elif self.is_parent:
            # Если тег является родителем и без атрибутов
            element = []
            for cild in self.childern:
                element.append(f'{cild}\n')
            element = '\t'.join(element)
            return f'\t<{self.tag}>\n\t{element}\t</{self.tag}>'
        else:
            # Если тег вложенный и без атрибутов
            return f"\t<{self.tag}>{self.text}</{self.tag}>"

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
    def __init__(self, tag, is_parent=True, *args, **kwargs):
        super().__init__(tag, is_parent, *args, **kwargs)

