import cv2
from personal_data_generation import \
    generate_vin_number, \
    generate_registration_number, \
    generate_name, \
    generate_passport_number, \
    generate_auto_mark

''' Генерирует документ с заполнением данных и возвращает изображение (Альфа - страхование) '''


def alpha_image_generator(template_image_path):
    img = cv2.imread(template_image_path)
    font = cv2.FONT_HERSHEY_COMPLEX

    # Инъекция vin-нормера
    cv2.putText(img, generate_vin_number(), (1650, 2670), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция регистрационного номера автомобиля
    cv2.putText(img, generate_registration_number(), (3450, 2670), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция имён
    cv2.putText(img, generate_name(), (300, 2065), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (300, 2265), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (600, 3545), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция паспортных данных
    cv2.putText(img, generate_passport_number(), (2500, 3545), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция марки автомобиля
    cv2.putText(img, generate_auto_mark(), (550, 2565), font, 2, color=(0, 0, 0), thickness=3)

    return img


'''Генерирует документ с заполнением данных и возвращает изображение (Ингосстрах)'''


def ingos_image_generator(template_image_path):
    img = cv2.imread(template_image_path)
    font = cv2.FONT_HERSHEY_COMPLEX

    # Инъекция vin-номера
    cv2.putText(img, generate_vin_number(), (1850, 2210), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция регистрационного номера автомобиля
    cv2.putText(img, generate_registration_number(), (3400, 2275), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция имён
    cv2.putText(img, generate_name(), (800, 1680), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (800, 1850), font, 2, color=(0, 0, 0), thickness=3)
    # cv2.putText(img, name_surname_gen(), (600,3545), font,2, color = (0,0,0), thickness=3)

    # Инъекция паспортных данных
    cv2.putText(img, generate_passport_number(), (1850, 2480), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция марки автомобиля
    cv2.putText(img, generate_auto_mark(), (550, 2210), font, 2, color=(0, 0, 0), thickness=3)

    return img


''' Генерирует документ с заполнением данных и возвращает изображение (Ренессанс)'''


def renessance_image_generator(template_image_path):
    img = cv2.imread(template_image_path)
    font = cv2.FONT_HERSHEY_COMPLEX

    # Инъекция vin-номера
    cv2.putText(img, generate_vin_number(), (1850, 2165), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция регистрационного номера автомобиля
    cv2.putText(img, generate_registration_number(), (3150, 2165), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция имён
    cv2.putText(img, generate_name(), (800, 1500), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (800, 1725), font, 2, color=(0, 0, 0), thickness=3)
    # cv2.putText(img, name_surname_gen(), (600,3545), font,2, color = (0,0,0), thickness=3)

    # Инъекция паспортных данных
    cv2.putText(img, generate_passport_number(), (2500, 3545), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция марки автомобиля
    cv2.putText(img, generate_auto_mark(), (550, 2165), font, 2, color=(0, 0, 0), thickness=3)

    return img


''' Генерирует документ с заполнением данных и возвращает изображение (РЕСО - страхование) '''


def reso_image_generator(template_image_path):
    img = cv2.imread(template_image_path)
    font = cv2.FONT_HERSHEY_COMPLEX

    # Инъекция vin-номера
    cv2.putText(img, generate_vin_number(), (1860, 2680), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция регистрационного номера автомобиля
    cv2.putText(img, generate_registration_number(), (3450, 2680), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция имён
    cv2.putText(img, generate_name(), (300, 2035), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (300, 2265), font, 2, color=(0, 0, 0), thickness=3)
    cv2.putText(img, generate_name(), (600, 3700), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция паспортных данных
    cv2.putText(img, generate_passport_number(), (2700, 3800), font, 2, color=(0, 0, 0), thickness=3)

    # Инъекция марки автомобиля
    cv2.putText(img, generate_auto_mark(), (550, 2680), font, 2, color=(0, 0, 0), thickness=3)

    return img
