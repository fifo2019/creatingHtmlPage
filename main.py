from tags import HTML, TopLevelTag, Tag

# TODO: Убрать именованное значение у output
# TODO: Добавить возможность вводить атрибуты для Tag
with HTML(output="print") as doc:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head += title
    doc += head

    with TopLevelTag("body") as body:
        with Tag("h1", klass=("main-text",)) as h1:
            h1.text = "Test"
            body += h1

    with TopLevelTag("div", klass=("container", "container-fluid"), id="lead") as div:
        with Tag("p") as paragraph:
            paragraph.text = "another test"
            div += paragraph

        with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
            div += img

        body += div

    doc += body


# TODO: Сделать вывод через __name__
# def start_ontext_manager(output):
#     """ Запускает контекстный менеджер """
#     with HTML(output) as doc:
#         with TopLevelTag("head") as head:
#             with Tag("title") as title:
#                 title.text = "hello"
#                 head += title
#             doc += head
#
#         with TopLevelTag("body") as body:
#             with Tag("h1", klass=("main-text",)) as h1:
#                 h1.text = "Test"
#                 body += h1
#
#             with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
#                 with Tag("p") as paragraph:
#                     paragraph.text = "another test"
#                     div += paragraph
#
#                 with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
#                     div += img
#
#                 body += div
#
#             doc += body
#
#
# if __name__ == '__main__':
#     try:
#         start_ontext_manager(sys.argv[1])
#     except IndexError:
#         print("Укажите куда выводить страницу: \n "
#               "- print - если хотите вывести результат страницы на экран терминала\n"
#               " - 'НАЗВАНИЕ ФАЙЛА БЕЗ РАСШИРЕНИЯ' - если хотите сохранить страницу в файл\n")
#         try:
#             user_answer = input('Ввод: ')
#             user_answer = user_answer.replace(' ', '')
#             if user_answer != '':
#
#                 start_ontext_manager(user_answer)
#             else:
#                 print('Вы ничего не ввели. Для повтора запустите программу заного.')
#         except KeyboardInterrupt:
#             pass

