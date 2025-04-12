import requests

ip_address = input("Введіть IP-адресу: ")

url = f"https://worldtimeapi.org/api/ip/{ip_address}.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    
    print("Таймзона:", data["timezone"])
    print("День та час:", data['datetime'])
    print("День у році:", data['day_of_year'])
    
except requests.exceptions.RequestException as e:
    print("Помилка при запиті до API", e)
except KeyError:
     print("Неправильна IP-адреса")