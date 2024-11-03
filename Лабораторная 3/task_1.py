
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def items(find,list):
    if find in list:
        index_item = list.index(find)
    else:
        index_item = None
    return index_item

for find_item in ['банан', 'груша', 'персик']:
    index_item = items(find_item,items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
