import re
from pathlib import Path
from pytesseract import pytesseract as tess
from pytesseract import Output
from preprocessor import *
import os 

def data_decryption(path_to_folder):
    files = Path(path_to_folder).glob('*')

    for file in files:
       
        file1 = str(os.path.basename(file).split('/')[-1])
        file = str(file)

        if  file1.split('-')[0] ==  'Альфа':
              
                tesseract(file,alfa_text_parser)
        if  file1.split('-')[0]  ==  'Ресо':
              
                tesseract(file,reso_text_parser)
        if  file1.split('-')[0]  ==  'Ренессанс':   
            
                tesseract(file,renessance_text_parser)
        if  file1.split('-')[0]  ==  'Ингосстрах':
               
                tesseract(file,ingos_text_parser)
       
# Парсинг данных из файла (Альфа-страхование)
def alfa_text_parser(image_from_generator):
    image = cv2.imread(image_from_generator)
    constraint_list = []
    # vin number constraint
    vin_image = image[2600:2700, 1630:2300] 
    # reg number constaraint
    reg_image    = image[2600:2700, 3400:3800]
    # car_model
    car_model = image[2500:2600, 300:1000]
    #name extractor 
    name_1 = image[2000:2090, 300:1700]
    #name extrator 2 
    name_2 = image[1970:2085, 300:1700]
    constraint_list = [vin_image, reg_image, car_model, name_1, name_2]

    return constraint_list

# Парсинг данных из файла (Ингосстрах)
def ingos_text_parser(image_from_generator):
    image = cv2.imread(image_from_generator)
    constraint_list = []
    #vin number constraint
    vin_image = image[2140:2230, 1730:2500] 
    #reg number constaraint
    reg_image   = image[2210:2280, 3200:3800]
    # car_model
    car_model = image[2140:2230, 500:1000]
    #name extractor 
    name_1 = image[1630:1700, 800:2100]
    #name extrator 2 
    name_2 = image[1800:1870, 800:2100]
    constraint_list = [vin_image, reg_image, car_model, name_1, name_2]

    return constraint_list


# Парсинг данных из файла (Ренессанс - страхлование)
def renessance_text_parser(image_from_generator):
    image = cv2.imread(image_from_generator)
    constraint_list = []
    # vin number constraint
    vin_image = image[2100:2200, 1730:2550] 
    # reg number constaraint
    reg_image    = image[2110:2180, 3100:3800]
    # car_model
    car_model = image[2110:2220, 500:1000]
    #name extractor 
    name_1 = image[1630:1800, 800:2100]
    #name extrator 2 
    name_2 = image[1410:1540, 800:2300]
    constraint_list = [vin_image, reg_image, car_model, name_1, name_2]

    return constraint_list

# Парсинг данных из файла (РЕСО- страхлование)
def reso_text_parser(image_from_generator):
    image = cv2.imread(image_from_generator)

    constraint_list = []
    vin_image = image[2620:2690, 1830:2600] 
    reg_image    = image[2620:2690, 3200:3800]
    car_model = image[2620:2690, 500:1000]
    name_1 = image[1950:2060,300:2100]
    name_2 = image[2180:2280,300:2100]
    constraint_list = [vin_image, reg_image, car_model, name_1, name_2]
    return constraint_list



# Парсер текста с помощью OCR
def tesseract(file,parser_type):
    for i in parser_type(file):
        text = tess.image_to_string(i, lang='rus+eng')
        print(text)

# Нахождение границ текста 
def rectangle_search(doc_path): 

    image = cv2.imread(doc_path)
    gray = get_grayscale(image)
    text = tess.image_to_string(gray, lang='rus+eng')
    data_out = tess.image_to_data(image, output_type=Output.DICT, lang="rus+eng")
    n_boxes = len(data_out['text'])
    for i in range(n_boxes):
        if int(data_out['conf'][i]) > 60:
            if re.match(data_out, data_out['text'][i]):
                (x, y, w, h) = (data_out['left'][i], data_out['top'][i], data_out['width'][i], data_out['height'][i])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 0, 0), thickness=5)
    return image