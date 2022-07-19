import os


# Задание 1
def cook_file_to_dict(file_name_, encoding_='utf-8'):
    FILE_NAME = file_name_
    ROOT_PATH = os.getcwd()
    full_path_f = os.path.join(ROOT_PATH, FILE_NAME)
    with open(full_path_f, encoding=encoding_) as file_:
        line_list = []  # Наполняем список всеми строками из файла
        for line in file_:
            line_list.append(line)
        list_recipes = []  # Список списков с рецептами
        recipe = []  # Список для одного рецепта
        for line in line_list:
            if not line == '\n':  # Пока нет пустой строки наполняем список для одного рецепта
                recipe.append(line.strip())  # Добавляем строки в список одного рецепта
                if line == line_list[-1]:  # Если строка последняя в файле, то добавляем последний рецепт в список
                    list_recipes.append(recipe)
            else:
                list_recipes.append(recipe)  # Добавляем в список списков очередной рецепт
                recipe = []  # Очистка списка одного рецепта под следующий рецепт
    cook_book = {}
    for recipe in list_recipes:
        v_list = []
        for i in range(2, len(recipe)):
            list1 = recipe[i].split(' | ')
            v_list.append({'ingredient_name': list1[0], 'quantity': int(list1[1]), 'measure': list1[2]})
        cook_book[recipe[0]] = v_list
    return cook_book


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_file_to_dict('recipes.txt')
    list_ingredient = []
    for k, v in cook_book.items():
        if k in dishes:
            for ing in v:
                list_ingredient.append(ing)
    shop_dict = {}
    for dict_ing in list_ingredient:
        if not dict_ing['ingredient_name'] in shop_dict:
            shop_dict[dict_ing['ingredient_name']] = ({'measure': dict_ing['measure'],
                                                       'quantity': dict_ing['quantity'] * person_count})
        else:
            shop_dict[dict_ing['ingredient_name']]['quantity'] += dict_ing['quantity'] * person_count
    return shop_dict


print(cook_file_to_dict('recipes.txt'))
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))


# Задание 3
# Функция получения списка файлов(с указанным расширением) из директории в текущем каталоге.
def dict_filename_size(dir_, extension_, encoding_):
    ROOT_PATH = os.getcwd()
    DIR = dir_
    full_path_dir = os.path.join(ROOT_PATH, DIR)
    list_short_filename = []  # Список с именами файлов
    list_full_filename = []  # Список с абсолютными путями к файлам
    for filename in os.listdir(full_path_dir):
        if extension_ in filename and 'result.txt' != filename:
            list_short_filename.append(filename)
            list_full_filename.append(os.path.join(ROOT_PATH, DIR, filename))
    dict_file_size = {}
    for i in range(len(list_short_filename)):
        with open(list_full_filename[i], encoding=encoding_) as file:
            dict_file_size[list_short_filename[i]] = len(file.readlines())
    #  Сортировка списка {файл: кол-во строк} по значению.
    sort_dict_file_size = {}
    sort_k = sorted(dict_file_size, key=dict_file_size.get)
    for w in sort_k:
        sort_dict_file_size[w] = dict_file_size[w]
    return sort_dict_file_size


# Функция записи результата из всех указанных файлов папки, в файл result.txt
def write_sort_file(dir_, extension_, encoding_):
    sort_dict_file_size = dict_filename_size(dir_, extension_, encoding_)
    ROOT_PATH = os.getcwd()
    DIR = dir_
    full_path_result = os.path.join(ROOT_PATH, DIR, 'result.txt')
    f = open(full_path_result, 'w', encoding=encoding_)
    f.write('')  # Первоначальная очистка очистка файла result.txt
    with open(full_path_result, 'a', encoding=encoding_) as result:
        count = 0
        for k, v in sort_dict_file_size.items():
            count += 1
            full_path_file = os.path.join(ROOT_PATH, DIR, k)
            with open(full_path_file, encoding=encoding_) as file:
                result.write(k + '\n')
                result.write(str(v) + '\n')
                for s in file:
                    result.write(s)
            if count != len(sort_dict_file_size):
                result.write('\n')  # После записи содержимого одного файла(кроме последнего) - перевод строки.
    return


write_sort_file('task_sort_file', '.txt', 'utf-8')  # Результат в папке task_sort_file текущего каталога.




