from requests import Response
import json

"""Методы для проверки наших запросов"""

class Checking():
    
    @staticmethod    # метод для проверки статус кода, статический метод мы не привязываемся ни к одному классу, поэтому self не нужен             
    # обращаемся к библиотеке reqeusts и 2 обязательных параметра, один status_code ожидаемый который мы будем задавать и 2 ответ от сервера
    def check_status_code(response: Response, status_code):     
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно! Наш статус код равен = " + str(response.status_code))
        else:
            print("Провал! Наш статус код не равен = " + str(response.status_code))



    """Метод для проверки обязательных полей в ответе запроса"""

    @staticmethod

    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)  #json модуль преобразует строку в формат json и мы импортировали функцию loads, ккоторая преобразует наш ответ из текств json
        """с помощью list мы получим все наши поля и значения из ответа"""
        assert list(token) == expected_value
        print("все поля присутствуют")


    """Метод для проверки значений в обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value): #field_name значение поля кторое прверяем
        check = response.json()  # check хранит в себе ответ в виде Json
        check_info = check.get(field_name)  #просим вернуть нам вернуть значение поля field_name(к примеру поля status, place_id и т д)
        assert check_info == expected_value
        print(field_name + " верен!")


    """Метод для проверки значений в обязательных полей в ответе запроса по заданому слову"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word): #field_name значение поля кторое прверяем и ключевое слово по которому ищем
        check = response.json()  # check хранит в себе ответ в виде Json
        check_info = check.get(field_name)  #просим вернуть нам вернуть значение поля field_name(к примеру поля status, place_id и т д)
        if search_word in check_info: 
            print("Слово " + search_word + " присутствует!") 

        else:
            print("Слово " + search_word + " отсутстует!")




