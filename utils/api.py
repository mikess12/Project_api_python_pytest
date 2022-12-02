from utils.http_method import Http_methods

""""Методы для тестирования Google_map_api"""

base_url = "https://rahulshettyacademy.com"         #  базовая url
key = "?key=qaclick123"                           # одинаквый параметр для всех url  знак вопросы обязательно т к это говорит что это параметр

class Google_map_api():
    """метод для создания новой локации"""
    @staticmethod
    def create_new_location():
        json_for_create_new_location = {
            "location": { 
                "lat": -38.383494, 
                "lng": 33.427362 
            }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
                "shoe park", 
                "shop"
            ],
            "website": "http://google.com", 
            "language": "French-IN"

        }

        post_resource = "/maps/api/place/add/json"    # ресурс метода post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post


    """метод для проверки новой локации"""
    
    @staticmethod
    def check_new_location(place_id):               # сообщаем нашей системе что когда мы вызваем данный метод, обязательно передать "place_id"

        get_resource = "/maps/api/place/get/json"    #ресурс метода get

        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        """создаем запрос get для этого обращаемся к созданному нами классу Http_methods и вызываем оттуда метод get и передаем в него наш get_url"""
        result_get = Http_methods.get(get_url) 

        print(result_get.text)
        return result_get


    """метод изменения новой локации"""
    
    @staticmethod
    def put_new_location(place_id):            # сообщаем нашей системе что когда мы вызваем данный метод, обязательно передать "place_id"

        put_resource = "/maps/api/place/update/json"    #ресурс метода put
        put_url = base_url + put_resource + key
        print(put_url)
        """создаем переменую с параметрами json для передачи в теле запроса put"""
        json_for_update_location = {
            "place_id": place_id,                        
            "address": "100 Lenina street, RU", 
            "key": "qaclick123"

        }
        
        result_put = Http_methods.put(put_url, json_for_update_location)
        print(result_put.text)
        return result_put

        
    """метод удаления новой локации"""
    

    @staticmethod
    def delete_new_location(place_id):  # сообщаем нашей системе что когда мы вызваем данный метод, обязательно передать "place_id"

        delete_resource = "/maps/api/place/delete/json"    #ресурс метода delete

        delete_url = base_url + delete_resource + key
        print()
        json_for_delete_location = {
            "place_id" :place_id
        }

        result_delete = Http_methods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete










