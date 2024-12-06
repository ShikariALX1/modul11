import matplotlib.pyplot as plt
import requests
import pprint

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("Данные успешно получены:")
    pprint.pprint(response.json())
else:
    print("Ошибка при получении данных:", response.status_code)

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o')
plt.title('Простой график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
