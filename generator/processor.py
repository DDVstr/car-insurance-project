import cv2
from os import path, getcwd
from image_generators import \
    alpha_image_generator, \
    ingos_image_generator, \
    renessance_image_generator, \
    reso_image_generator

# Описание компании. Устанавливает:
# 1: название компании
# 2: название template-файда для генерации
COMPANY_DESCRIPTOR = [
    ('Альфа-страхование', 'Альфа-страхование.png', alpha_image_generator),
    ('Ингосстрах', 'Ингосстрах.png', ingos_image_generator),
    ('Ренессанс', 'Ренессанс.png', renessance_image_generator),
    ('Ресо', 'Ресо.png', reso_image_generator)
]
DEFAULT_TEMPLATES_PATH = 'templates'
DEFAULT_FILES_NUMBER = 10


def input_user_data(what, default=None):
    or_default_text = ', or press enter for {}'.format(default) if default is not None else ''
    res = input('Input {}{}: '.format(what, or_default_text)).strip()
    return default if default is not None and len(res) == 0 else res


def input_templates_path():
    return input_user_data('path to the templates folder', DEFAULT_TEMPLATES_PATH)


def input_files_count():
    return int(input_user_data('the needed number of files', DEFAULT_FILES_NUMBER))


def input_output_path():
    return input_user_data('path to the output folder')


# Cоздание синтетических данных и сохранение их в указанную директорию
def create_document_samples():
    templates_path = path.join(getcwd(), input_templates_path())
    files_count = input_files_count()
    output_path = path.join(getcwd(), input_output_path())

    for company_name, template_file_name, image_generator in COMPANY_DESCRIPTOR:
        for i in range(files_count):
            template_image_path = path.join(templates_path, template_file_name)
            generated_image = image_generator(template_image_path)
            output_image_path = path.join(output_path, '{}-{}.png'.format(company_name, i))
            cv2.imwrite(output_image_path, generated_image)

    return output_image_path


# Функция возвращает путь для сгенерированных синтетических данных
def path_to_samples():
    return path.join(getcwd(), input_output_path())
