# 4
# Начните работу над проектом «Склад оргтехники».
# Создайте класс «Склад».
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка:
# Постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Storage:
    def __init__(self):
        self.items = []

    def __str__(self):
        [print(i) for i in self.items]
        return ''

    def __get_ids(self):
        return [i.id for i in self.items]

    def __get_item_by_id(self, _id: int) -> object or None:
        _list = [i for i in self.items if i.id == _id]
        return _list[0] if _list else None

    def add_items(self, *items):
        ids = self.__get_ids()
        [self.items.append(i) for i in items if i.id not in ids]

    def remove_item_by_id(self, _id: int):
        ids = self.__get_ids()
        if _id in ids:
            self.items.pop(ids.index(_id))

    def change_price(self, _id: int, price: int):
        item = self.__get_item_by_id(_id)
        item.set_price(price)

    def change_place(self, _id: int, place: str):
        item = self.__get_item_by_id(_id)
        item.set_place(place)

    def change_inner_param(self, _id: int, param: str):
        item = self.__get_item_by_id(_id)
        item.set_inner_param(param)


class AutoId:
    __id = -1

    def __new__(cls):
        cls.__id += 1
        return cls.__id


class OfficeEquipment:
    __default_place = 'all'

    def __init__(self, _id: int, price: int, _type: str, place: str):
        self.id = _id
        self.price = price
        self.type = _type
        self.place = place

    def set_price(self, price: int):
        self.price = price

    def set_place(self, place: str):
        self.place = self.__default_place if place == 'default' else place


class Printer(OfficeEquipment):
    __default_owner = '-'

    def __init__(self, price: int, place='all', owner='-'):
        super().__init__(AutoId(), price, 'printer', place)
        self.owner = owner

    def __str__(self):
        return f'Тип: {self.type}, Инв.номер (id): {self.id}, Стоимость: {self.price},' \
               f' Расположение: {self.place}, Владелец: {self.owner}'

    def set_owner(self, owner: str):
        self.owner = owner

    def set_inner_param(self, param='default'):
        o = self.__default_owner if param == 'default' else param
        self.set_owner(o)


class Scanner(OfficeEquipment):
    __default_model = '-'

    def __init__(self, price: int, place='all', model='-'):
        super().__init__(AutoId(), price, 'scanner', place)
        self.model = model

    def __str__(self):
        return f'Тип: {self.type}, Инв.номер (id): {self.id}, Стоимость: {self.price},' \
               f' Расположение: {self.place}, Модель: {self.model}'

    def set_model(self, model: str):
        self.model = model

    def set_inner_param(self, param='default'):
        m = self.__default_model if param == 'default' else param
        self.set_model(m)


class Xerox(OfficeEquipment):
    __default_country = '-'

    def __init__(self, price: int, place='all', country='-'):
        super().__init__(AutoId(), price, 'xerox', place)
        self.country = country

    def __str__(self):
        return f'Тип: {self.type}, Инв.номер (id): {self.id}, Стоимость: {self.price},' \
               f' Расположение: {self.place}, Страна производства: {self.country}'

    def set_country(self, country: str):
        self.country = country

    def set_inner_param(self, param='default'):
        c = self.__default_country if param == 'default' else param
        self.set_country(c)


class InitStorage:
    def __init__(self):
        self.items = []

        self.__type = 0
        self.__qty = 0
        self.__price = []
        self.__place = []
        self.__inner_param = []

        self.start()

    def __call__(self):
        return self.items

    def start(self):
        self.__get_type()
        self.__get_qty()

        for i in range(self.__qty):
            print(f'Введите данные по технике-{i + 1}:')
            self.__get_price()
            self.__get_place()
            self.__get_inner_param()

        self.__make_obj()
        self.__to_init_position()
        self.__repeat()

    def __get_type(self):
        while True:
            try:
                print('Выберите тип техники, которую следует поместить на склад:')
                print('1 - принтер, 2 - сканнер, 3 - ксерокс')
                t = int(input('Введите число от 1 до 3: '))

                if t not in range(1, 4):
                    raise ValueError
            except ValueError:
                print('Ошибка! Следует ввести целое число от 1 до 3!')
            else:
                self.__type = t
                break

    def __get_qty(self):
        while True:
            try:
                q = int(input('Количество: '))
                if q not in range(1, 11):
                    raise ValueError
            except ValueError:
                print('Ошибка! Следует ввести целое число от 1 до 10!')
            else:
                self.__qty = q
                break

    def __get_price(self):
        while True:
            try:
                p = int(input('Стоимость: '))
                if not p:
                    raise ValueError
            except ValueError:
                print('Ошибка! Следует ввести целое число больше 0!')
            else:
                self.__price.append(p)
                break

    def __get_place(self):
        print('Можно ввести позже. Чтобы пропустить, нажмите Enter.')
        p = input('Расположение: ')
        self.__place.append(p if p != '' else 'all')

    def __get_inner_param(self):
        _dict = {1: 'Владелец', 2: 'Модель', 3: 'Страна производства'}
        print('Можно ввести позже. Чтобы пропустить, нажмите Enter.')
        p = input(f'{_dict[self.__type]}: ')
        self.__inner_param.append(p if p != '' else '-')

    def __make_obj(self):
        _dict = {1: Printer, 2: Scanner, 3: Xerox}
        for i in range(self.__qty):
            price, place, param = self.__price[i], self.__place[i], self.__inner_param[i]
            item = _dict[self.__type](price, place, param)
            self.items.append(item)

    def __to_init_position(self):
        self.__type = 0
        self.__qty = 0
        self.__price = []
        self.__place = []
        self.__inner_param = []

    def __repeat(self):
        __r = 0
        while True:
            try:
                print('Хотите добавить другую технику на склад?')
                print('1 - Да (продолжить), 2 - Нет (завершить процесс)')
                __r = int(input('Введите число 1 или 2: '))
                if __r not in [1, 2]:
                    raise ValueError
            except ValueError:
                print('Ошибка! Следует ввести целое число 1 или 2!')
            else:
                break
        if __r == 1:
            self.start()


items = InitStorage()
s = Storage()
s.add_items(*items())
print(s)
