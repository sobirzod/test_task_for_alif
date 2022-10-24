class Task:
    def __init__(self, filename) -> None:
        self.filename = filename

    def open_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
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
        items = self.open_file()
        new_file = items + '\n' + new_item
        self.save_file(new_file)
    
    def edit(self, correct_item):
        new_items_list = self.processing(correct_item)
        self.save_file('\n'.join(new_items_list))


    def delete(self, item):
        new_items_list = self.processing(item, delete=True)
        self.save_file('\n'.join(new_items_list))

    def summ(self):
        items = self.open_file().split('\n')
        summ = 0
        for item in items:
            try:
                summ += float(item.split()[1])
            except:
                summ += 0
        print(summ)

t = Task('test.txt')
t.add('Apple 150')
t.edit('Apple 300')
# t.delete('Apple')
t.summ()

# t = Task(input('Введите названия файла: '))
# operations = input('Выберите операцию(add, edit, delete, summ): ')

# if operations == 'add':
#     new_item = input('Введите название и цену через пробел: ')
#     t.add(new_item)
# elif operations == 'edit':
#     new_item = input('Введите название и цену через пробел: ')
#     t.edit(new_item)
# elif operations == 'delete':
#     new_item = input('Введите название: ')
#     t.delete(new_item)
# elif operations == 'summ':
#     print(t.summ())
