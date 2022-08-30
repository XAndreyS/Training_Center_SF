from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_auth_key_valid_user(email=valid_email, password=valid_password):
    '''Проверяем что при вводе валидных данных пользователя ответ со статусом 200 и содержит слово key'''

    #Создаём переменные в которые сохраняем запрос на получение ключа и статус ответа
    status, result = pf.get_api_key(email, password)

    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert "key" in result #Вызываем проверку наличия слова key в результате ответа

def test_no_clear_list_of_pets_valid_key(filter= ''):
    '''Проверяем что по валидному ключуприходит ответ со статусом 200 и в нем не пустой список питомцев'''

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на получение списка питомцев, который созраняем в переменную result, а в переменную status сщхраняем статус ответа
    status, result  = pf.get_list_of_pets(auth_key, filter)

    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert len(result['pets']) > 0 #Вызываем проверку наличия питомцев в списке питомцев('pets' > 0)

def test_add_new_pet_valid_data(name= 'Lohmatiy', animal_type= 'Sapog', age='2', pet_photo= 'images/Lohmatyi_Sapog.jpg'):
    '''Проверяем добавление нового питомца с корректными данными'''

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на добавление нового питомца который созраняем в переменную result, а в переменныю status сохраняем статус ответа на на этот запрос
    status, result = pf.add__about_new_pet(auth_key, name, animal_type, age, pet_photo)

    ## Удаляем нового питомца
    _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = list_my_pets['pets'][0]['id']
    dele, _ = pf.delete_from_database(auth_key, pet_id)


    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert result['name'] == name #Вызываем проверку того что в переменной result имя питомца совпадает с тем именем питомца,которое мы указали при добавлении(name= 'Lohmatiy')


def test_delete_tet():
    """проверяем возможность удаление питомца"""

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на получение списка питомцев, который созраняем в переменную list_my_pets, а в переменную _ сoхраняем статус ответа(он нам не потребуется)
    _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    #Если в списке нет питомцев(длина списка равна нулю), то создаем нового питомца
    if len(list_my_pets)== 0:
        pf.add__about_new_pet('Volosatyi', 'Tatok', '23', 'images/Lisiy_Sapog.jpg')
        _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets') #Затем снова запрашиваем список своих питомцев и созраняем результат запроса в переменную list_my_pets, а в переменную _ сoхраняем статус ответа(он нам не потребуется)
    pet_id = list_my_pets['pets'][0]['id'] # Создаем перемнную pet_id в которую созраняем id первого в списке питомца

    # Запросна удаление питомца
    status,_ = pf.delete_from_database(auth_key, pet_id)

    # Запрос на получение списка питомцев, который созраняем в переменную list_my_pets, а в переменную _ сoхраняем статус ответа(он нам не потребуется)
    _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert pet_id not in list_my_pets.values() #Вызываем проверку того, что в списке питомцев нет питомца с id питомца которого мы удалили

def test_update_pet(name= 'Mudriy', animal_type= 'Valinok', age= 50):
    """Проверяем обновление  информации о питомце"""

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на получение списка питомцев, который созраняем в переменную list_my_pets, а в переменную _ сoхраняем статус ответа(он нам не потребуется)
    _, list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # если список не пустой,то пробуем обновить информациюо питомце

    assert len(list_my_pets['pets']) > 0 , "В списке нет питомцев" #Проверяем  наличие питомцев в списке

    #Запросна изменение питомца по id первого в списке питомцев, и  созраняем результат в переменныю  result, а в переменную status созраняем статус ответа
    status, result = pf.update_information_about_pet(auth_key, list_my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert result['name'] == name #Вызываем проверку того что в переменной result имя питомца совпадает с тем именем питомца,которое мы указали при исменении(name= 'Mudriy')


def test_add_new_pet_without_photo(name= 'Zak', animal_type= 'dump', age='37'):
    """Проверяем возможность добавления питомца без фото с корректными данными"""

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на добавление нового питомца без фото, который созраняем в переменную result, а в переменныю status сохраняем статус ответа на на этот запрос
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200 #вызываем проверку статуса ответа, который должен быть равен 200
    assert result['name'] == 'Zak' #Вызываем проверку того что в переменной result имя питомца совпадает с тем именем питомца,которое мы указали при добавлении(name= 'Zak')

def test_add_photo_of_pets_valid(pet_photo= 'images/Lisiy_Sapog.jpg'):
    """Проверяем возможность добавления нового фото для созданного питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # запрос на получения ключа, который сохраняем в переменную auth_key, в переменную _ сохранится статус ответа этого запроса(он нам не потребуется)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрос на получение списка питомцев, который созраняем в переменную list_my_pets, а в переменную _ сoхраняем статус ответа(он нам не потребуется)
    _,list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #Проверяем, если список питомцев пустой, то добавляем нового питомца (тут пользуемся методом add__about_new_pet)
    if len(list_my_pets['pets']) == 0:
        pf.add__about_new_pet(auth_key, 'Pol','MuadDib', '77', 'images/Lisiy_Sapog.jpg')
        _,list_my_pets = pf.get_list_of_pets(auth_key, 'my_pets') #Запрашиваем список питомцев

    pet_id = list_my_pets['pets'][0]['id'] # Создаем перемнную pet_id в которую созраняем id первого в списке питомца

    #Запрос на добавление нового фото для питомца id которого находится в переменно id
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    assert status == 200#вызываем проверку статуса ответа, который должен быть равен 200
    # Вызываем проверку того что новое фото соответствует тому фото,что мы добавили
    assert result['pet_photo'] == 'data:image/jpeg;base64,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'




