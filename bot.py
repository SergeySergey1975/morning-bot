import requests

token = "8938508342:AAHVpGbmzjgko0FOk-uKF1kBSYd52jJlbOQ"
chat_id = "5114179830"

tekst = "Доброе утро, Сергей! ☀️\nПора потратить 15 минут на Python. Ты отлично справляешься! 🚀"

url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={tekst}"
response = requests.get(url)

if response.json().get('ok'):
    print("Успешно отправлено!")
else:
    print("Ошибка:", response.json())
