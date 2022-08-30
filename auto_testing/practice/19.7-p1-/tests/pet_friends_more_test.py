from api import PetFriends
#from settings import valid_email, valid_password, invalid_email, invalid_password, no_register_email, no_register_password, invalid_auth_key
import os
from settings import UserData, PetsData
pf = PetFriends()
data= UserData()
pets_data = PetsData()
"""Все тесты используют корректный тип данных - строка"""


def test_get_auth_key_invalid_email(email= data.invalid_email, password= data.valid_password):
    """Проверяем запрос ключа с непрвавильным email и верным паролем, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_auth_key_invalid_password(email= data.valid_email, password = data.invalid_password):
    """Проверяем запрос ключа с неправильным паролем и верным email, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_auth_key_no_register_email(email= data.no_register_email, password= data.no_register_password ):
    """Проверяем запрос api ключа для не зарегистрированного email, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_auth_key_empty_email(email= '', password= data.valid_password):
    """Проверяем запрос на получение api ключа с не заполненым email, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_auth_key_empty_password(email= data.valid_email, password= ''):
    """Проверяем запрос на получение api  ключа с валидным email ине заполненым паролем, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_auth_key_empty_email_empty_password(email= '', password= ''):
    """Проверяем запрос на получение api ключа с не заполнеными email и паролем, ожидаем статус ответа 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

def test_get_list_pets_invalid_auth_key(filter= 'my_pets'):
    """Проверяем запрос на получение списка питомцес с невалидным ключом, ожидаем статус ответа 403"""

    status, result = pf.get_list_of_pets(data.invalid_auth_key, filter)

    assert status == 403

def test_add_new_pets_name_animal_type_latin(name = pets_data.name_latin, animal_type= pets_data.animal_type_latin,age= '3',
                                             pet_photo= 'images\Lohmatyi_Sapog.jpg'):
    """Проверяем добавление питомца, входные данные(все тип строка) имя и тип, написаны латиницей(заодно проверка букв в верхнем и нижнем  регистре
    конечно возможно лучше будет вынести это в отдельный тест), ответ со статусом 200, и проверку наличия
    нового питомца по имени и типу"""
    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key,name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == pets_data.name_latin
    assert result['animal_type'] == pets_data.animal_type_latin



def test_add_new_pets_name_animal_type_cyrilic(name = pets_data.name_cyrillic, animal_type= pets_data.animal_type_cyrillic,
                                               age = '12', pet_photo= 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем  добавление нового питомца, входные данные(все тип строка) имя и тип, написанны  киррилицей(заодно проверка букв в верхнем и нижнем  регистре), ответ со статусом 200, проверка наличия
    нового питомца по  имени и типу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key =  pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key,name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == pets_data.name_cyrillic
    assert result['animal_type'] == pets_data.animal_type_cyrillic

def test_add_new_pets_name_simbol(name= pets_data.name_symbol, animal_type = pets_data.animal_type_latin, age = '5',
                                  pet_photo= 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, входные данные(все тип строка) имя написанно символамиб тип латиницей, ответ статус 400"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key,name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pets_animal_type_symbol(name= pets_data.name_latin, animal_type= pets_data.animal_type_symbol, age= '9',pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, входные данные(все тип строка)  имя написанно латиницей, тип спецсимволами, ответ статус  400"""
    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key,name, animal_type,  age, pet_photo)

    assert status == 400

def test_add_new_pets_age_leter(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_leter,
                                pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, вхлдные данные(все тип строка) имя и тип латиницей,  возраст буквами,
    ожидается ответ со статусом 400"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pets_age_symbol(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_symbol,
                                pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, вхлдные данные имя и тип латиницей,  возраст спецсимволами,
    ожидается ответ со статусом 400"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key =  pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type,age, pet_photo)

    assert status == 400

def test_add_new_pets_age_big(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_big,
                                pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, вхлдные данные имя и тип латиницей,  возраст 5000 цифр,
    ожидается ответ со статусом 400"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pets_age_huge(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_huge,
                                pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, вхлдные данные имя и тип латиницей,  возраст 1000000 цифр,
        ожидается ответ со статусом 400"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pets_age_empty(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_empty,
                                pet_photo = 'images/Lohmatyi_Sapog.jpg'):
    """Проверяем добавление нового питомца, вхлдные данные имя и тип латиницей,  возраст пустая строка,
            ожидается ответ со статусом 400(по моему мнению данные питомца не должны быть пустыми)"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pets_photo_txt(name=pets_data.name_latin, animal_type= pets_data.animal_type_latin, age= pets_data.age_norm,
                                pet_photo = 'images/Text.txt'):
    """Проверяем добавление новоги питомца, входные данные имя латиница, тип питомца латиница, возраст 2, фото расширение txt - все данные тип строка"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status  == 400 # я предпологаю, что 400 ведь в документации 400 - Код ошибки означает, что предоставленные данные неверны
                            # а не верны формат фото это вроде как не верные данные

"""Все тесты используют корректный тип данных - строка, в модуле 20 я уже подсмотрел, что важней проверять ввод не корректного
типа данных(int вместо строки и пт)"""



def test_clear_list_pest():
    """Оищаем список от созданных питомцев после тестов(пока так, позже нужно переделать на удаление после создания"""
    _, auth_key = pf.get_api_key(data.valid_email, data.valid_password)
    while True:

        _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
        pet_id = list_my_pets['pets'][0]['id']
        pf.delete_from_database(auth_key, pet_id)
        _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

        if len(list_my_pets['pets']) == 0:#
            break

        _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert len(list_my_pets['pets'])==0
















