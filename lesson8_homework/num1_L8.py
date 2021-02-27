class Data:
    @classmethod
    def num_transform(cls):
        data_str = input('Введите число в формате день-месяц-год:')
        numbers = cls.validation(data_str)
        try:
            print(f'День: {int(numbers[0])} Месяц: {int(numbers[1])} Год: {int(numbers[2])}')
        except TypeError:
            print('Программа выполнена некорректно')

    @staticmethod
    def validation(d_str):
        try:
            date_list = d_str.split('-')
            if not 1 <= int(date_list[0]) <= 31:
                print('Некорректный формат ввода дня')
                return None
            elif not 1 <= int(date_list[1]) <= 12:
                print('Некорректный формат ввода месяца')
                return None
            elif not 1900 <= int(date_list[2]) <= 2020:
                print('Некорректный формат ввода года')
                return None
        except ValueError:
            return None
        else:
            return date_list


num1 = Data()
num1.num_transform()
