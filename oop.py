class Task:
    """
    Класс предназначен для добавления, редактирования, удаления и рассчета суммы
    продуктов.

    Объект класса принимает один аргумент: названия файла в формате "название.txt".

    Для добавления продукта используется метод add. 
    Для редактирования используется метод edit.
    Для удаления продукта используется метод delete.
    И для рассчета суммы продуктов используется метод summ.
    """
    def __init__(self, filename) -> None:
        self.filename = filename

    def open_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                opened_file = file.read()
        except:
            with open(self.filename, 'w+', encoding='utf-8') as file:
                opened_file = file.read()
        return opened_file


    def save_file(self, new_file):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(new_file)

    def processing(self, correct_item, delete=False):
        items = self.open_file()
        new_items_list = []
        for item in items.split('\n'):
            item_title = item.split(' ')[0]
            if item_title == correct_item.split(' ')[0]:
                if delete is False:
                    new_items_list.append(f"{item.split(' ')[0]} {correct_item.split(' ')[1]}")
            else:
                new_items_list.append(item)
        
        return new_items_list
    
    def add(self, new_item):
        """
        Принимает строку содержащую название и цену продукта через пробел.
        Формат ввода: Название Цена
        Пример: Яблока 200
        """
        items = self.open_file()
        new_file = items + '\n' + new_item
        self.save_file(new_file)
    
    def edit(self, correct_item):
        """
        Принимает строку содержащую название и цену продукта через пробел.
        Формат ввода: Название Цена
        Пример: Яблока 200
        """
        new_items_list = self.processing(correct_item)
        self.save_file('\n'.join(new_items_list))


    def delete(self, item):
        """
        Принимает строку содержащую название продукта.
        Пример: Яблоко
        """
        new_items_list = self.processing(item, delete=True)
        self.save_file('\n'.join(new_items_list))

    def summ(self):
        """
        Выводит на консоль сумму продуктов.
        """
        items = self.open_file().split('\n')
        summ = 0
        for item in items:
            try:
                summ += float(item.split()[1])
            except:
                summ += 0
        print(summ)

