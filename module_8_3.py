class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class Car:
    def __init__(self, model, vin, numbers):

        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):

            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')

        else:
            pass

    def __is_valid_vin(self, vin_number):
        try:
            if isinstance(vin_number, float):
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True

    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
