import requests
import allure
from utils.logger import Logger

""""Список http методов, составили кастомные запросы 4 методов HTTP"""
class Http_methods:
    headers = {'Cjntent-Type': 'application/json'}
    cookie = ""

    @staticmethod              # статичный метод без self тоесть мы можем его вызывать откуда угодно
    def get(url):                #  метод get будет возвражать ответ содержащийся в result
        with allure.step("GET"):
            Logger.add_request(url, "GET")  # каждый раз когда мы вызываем наш квстомный метод get, в логах будет появляться название GET
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)            #логирунтся результат нашего ответа
            return result

    @staticmethod                 
    def post(url, body):                
        with allure.step("POST"):
            Logger.add_request(url, "POST")
            result = requests.get(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie) 
            Logger.add_response(result)
            return result

    @staticmethod                
    def put(url, body):                
        with allure.step("PUT"):
            Logger.add_request(url, "PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie) 
            Logger.add_response(result)
            return result

    @staticmethod     
    def delete(url, body):                
        with allure.step("DELETE"):
            Logger.add_request(url, "DELETE")
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result