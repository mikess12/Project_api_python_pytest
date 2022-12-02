from utils.api import Google_map_api
from requests import Response
from utils.cheking import Checking
import json
import allure

""""Мы импортировали нами созданый модуль api и из него наш класс Google_map_api"""

""""Создание изменение и удаление новой локации"""

@allure.epic("Test create location")
class Test_create_location():

    @allure.description("Создание, изменение и удаление новой локации")
    def test_create_new_place(self):
        
        print("Метод Post")
        result_post: Response = Google_map_api.create_new_location()
        """это слудующий шаг для вызова place_id из ответа"""
        check_post = result_post.json()      #обращаемся к переменной result_post вернуть нам json ответ
        
        """Здесь задаем нашу переменую place_id из check_post вызовем метод get который будет возращать нам значение нашего ключа place_id"""
        place_id = check_post.get("place_id") 
        Checking.check_status_code(result_post, 200)  #вызываем наш метод, который мы создали для проверки статуса кода и передаем сюда наш ответ result_post и наш ожидаемый результат
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        #print(result_post.status_code)   #  фатический статус код на печать
        #token = json.loads(result_post.text)
        #print(list(token))
        Checking.check_json_value(result_post, 'status','OK')   # stusus это название нашего поля, ok это значение нашего поля из докуметации в ответе 

        print("Метод Get Post")
        """вызываем наш Класс и методом check_new_location и передаем в него наш place_id"""
        result_get: Response = Google_map_api.check_new_location(place_id) 
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        #token = json.loads(result_get.text) # для того чтобы не брать из документации, мы можем вывести обязательные поля на печать это просто для удобства
        #print(list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод Put")
        """вызываем наш Класс и методом check_new_location и передаем в него наш place_id"""
        result_put: Response = Google_map_api.put_new_location(place_id) 
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg']) # 'msg'обязательные поля берем из документации, какой должен быть ответ при запросе
        #token = json.loads(result_put.text)
        #print(list(token))
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print("Метод Get Put")
        """вызываем наш Класс и методом check_new_location и передаем в него наш place_id"""
        result_get: Response = Google_map_api.check_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print("Метод Delete")
        """вызываем наш Класс и методом check_new_location и передаем в него наш place_id"""
        result_delete: Response = Google_map_api.delete_new_location(place_id) 
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status','OK')

        
        print("Метод Get Delete")
        """вызываем наш Класс и методом check_new_location и передаем в него наш place_id"""
        result_get: Response = Google_map_api.check_new_location(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')  #имщем в ответе в поле 'msg' слово 'failed', если есть тест пройден

        print("Тестирование создание изменение и удаление новой локации, прошло успешно!")
        













