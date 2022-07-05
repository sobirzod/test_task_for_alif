import json


def writer(file_name, data):
    
    with open(f'{file_name}.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def open_file(file_name):
    
    with open(f'{file_name}.json', 'r') as file:
        data = json.load(file)
    return data


def find_product(file_name, product_name):
    
    data = open_file(file_name)
    list_data = data['Product']
    for i, product in enumerate(list_data):
        for key in product.keys():
            if key == product_name:
                return i


def add(file_name, product):
    
    data = open_file(file_name)
    data['Product'].append(product)

    writer(file_name, data)


def create_file(file_name, product_name, amount):
    
    data = {'Product': [{product_name: amount}]}

    writer(file_name, data)


def edit(file_name, product_name, amount):
    
    product_idx = find_product(file_name, product_name)
    data = open_file(file_name)
    data['Product'][product_idx][product_name] = amount

    writer(file_name, data)


def delete(file_name, product_name):
    
    product_idx = find_product(file_name, product_name)
    data = open_file(file_name)
    data['Product'].pop(product_idx)

    writer(file_name, data)


def summ(file_name):
   
    data = open_file(file_name)
    list_data = data['Product']
    summ = 0
    for _, product in enumerate(list_data):
        for value in product.values():
            summ += value

    print(summ)


def main():
    file_name = input('Введите название файла ')
    action = input('Введите комманду ')

    if action == 'Add':
        try:
            product_name = input('Название продукта ')
            amount = int(input('Количество '))
            add(file_name, {product_name: amount})
        except FileNotFoundError:
            create_file(file_name, file_name, amount)
    if action == 'Edit':
        edit(file_name, input('Название продукта '), int(input('Количество ')))
    if action == 'Delete':
        delete(file_name, input('Название продукта '))
    if action == 'Summ':
        summ(file_name)


if __name__ == '__main__':
    main()
