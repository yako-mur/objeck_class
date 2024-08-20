#with open('recipes.txt', 'r', encoding='utf-8') as f:
def final():
    out = {}
    text = open_file()
    dish_list = text_1(text)
    dish = [text_2(i) for i in dish_list]
    for i in dish:
        out.update(dict(i))
    return out

def open_file():
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        return f.read()


def text_1(text):
    return [i.splitlines() for i in text.split('\n\n')]


def text_2(lst):
    return lst[:1] + [i.replace(' ', '').split('|') for i in lst[2:]]


def dict(lst):
    return {lst[0]: [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[2:]]}

result = final()

print(result)



