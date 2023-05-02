import string
import random


# Генерирует случайный VIN-номер
def generate_vin_number():
    digits_count = 16
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(random.choices(alphabet, k=digits_count))


# Генерирует случайный регистрационный номер автомобиля
def generate_registration_number():
    get_digit = lambda: str(random.randint(1, 999)).zfill(3)

    reg_literals = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
    get_literal = lambda amount: ''.join(random.choices(reg_literals, k=amount))

    get_region = lambda: str(random.randint(1, 99)).zfill(2)

    return '{}{}{}{}'.format(get_literal(1), get_digit(), get_literal(2), get_region())


# Генерирует случайное имя
def generate_name():
    names_list = ['ПЕТР', 'ИВАН', 'АНДРЕЙ', 'АЛЕКСАНДР', 'КОНСТАНТИН', 'ИЛЬЯ', 'НИКИТА', 'ЕГОР', 'ВЛАДИМИР', 'НИКОЛАЙ',
                  'ВАСИЛИЙ', 'ПАВЕЛ']
    last_list = ['ИВАНОВ', 'АНДРЕЕВ', 'АЛЕКСАНДРОВ', 'ГЛУШКО', 'ШУМКОВ', 'МАКСИМОВ', 'ЧАК', 'ПЕТРИЦЫН', 'ИПАТОВ',
                 'СЕРГЕЕВ', 'ШОЛОХОВ']
    middle_name = ['ПЕТРОВИЧ', 'ИВАНОВИЧ', 'АНДРЕЕВИЧ', 'АЛЕКСАНДРОВИЧ', 'КОНСТАНТИНОВИЧ', 'ИЛЬИЧ', 'НИКИТОВИЧ',
                   'ЕГОРОВИЧ', 'ВЛАДИМИРОВИЧ', 'НИКОЛАЕВИЧ', 'ВАСИЛИЕВИЧ', 'ПАВЛОВИЧ']

    return ' '.join([random.choice(l) for l in [names_list, middle_name, last_list]])


# Генерирует случайный номер паспорта в соотвествии с ГОСТом
def generate_passport_number():
    return str(random.randint(4100, 4910)) + " " + str(random.randint(1, 999999)).zfill(6)


# Генерирует марку автомобиля
def generate_auto_mark():
    auto_list = ['BMW', 'TESLA', 'MERCEDES', 'VOLVO', 'RENAULT', 'MAZDA', 'TOYOTA']
    return random.choice(auto_list)
