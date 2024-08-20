from pprint import pprint

def introspection_info(obj):

    # Тип объекта
    type_obj = type(obj).__name__

    # Атрибуты объекта
    attributes_obj = dir(obj)
    attributes_obj = [method for method in attributes_obj if not callable(getattr(obj, method))]

    # Методы объекта
    methods_obj = dir(obj)
    methods_obj = [method for method in methods_obj if callable(getattr(obj, method))]

    # Модуль, к которому принадлежит объект
    module = obj.__class__.__module__

    # Индификатор объекта
    address_obj = id(obj)

    # Документационная строка
    doc_obj = obj.__doc__

    # Словарь с полученной информацией
    info_about_obj = {'Тип' : type_obj, 'Атрибуты' : attributes_obj, 'Методы' : methods_obj, 'Модуль' : module,
                      'Индификатор' : address_obj, 'Документационная строка' : doc_obj }

    pprint(info_about_obj)


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=bool):
        self.__color = list(color)  # список цветов RGB
        self.__sides = [sides for _ in range(self.sides_count)]  # список сторон, int
        self.filled = filled  # не/закрашенный, bool

    def get_color(self):
        print(f'Цвет фигуры (RGB): {self.__color}')  # геттер возвращает список RGB цветов

    @staticmethod
    def __is_valid_color(r, g, b):
        """"статический метод принимает параметры r, g, b, который
        проверяет корректность переданных значений перед установкой
        нового цвета. Корректным цвет: все значения r, g и b - целые числа
        в диапазоне от 0 до 255 (включительно)."""
        return True if 0 < r < 255 and 0 < g < 255 and 0 < b < 255 else False

    def set_color(self, r, g, b):
        """ Данный сеттер принимает параметры r, g, b - числа и изменяет
                атрибут __color на соответствующие значения"""
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, my_list):
        """служебный, принимает неограниченное кол-во сторон,
               возвращает True если все стороны целые положительные
               числа и кол-во новых сторон совпадает с текущим"""
        if len(my_list) == self.sides_count:
            for i in my_list:
                if i < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        print(f'Список сторон фигуры: {self.__sides}')   # геттер возвращает списо сторон

    def __len__(self):
        print(f'Периметр фигуры : {sum(self.__sides)}')

    def set_sides(self, *new_sides):
        my_list = [*new_sides]
        """ Данный сеттер принимает неограниченное кол-во сторон,
         проверяет корректность переданных данных"""
        if self.__is_valid_sides(my_list) is True:
            self.__sides = my_list


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__radius = sides / (2 * 3.1415)

    def get_square(self):
        print(f'Площадь фигуры (круга): {3.1415 * (self.__radius**2)}') # метод возвращает площадь круга


some_obj_of_class = Circle((200, 200, 100), 10)
some_number = 1
some_string = 'qwerty'
some_function = introspection_info

introspection_info(some_obj_of_class)
# introspection_info(some_number)
# introspection_info(some_string)
# introspection_info(some_function)

