import requests
import json
#vk
user_id = '351297070'
access_token = 'a3cc68d2a3cc68d2a3cc68d25ba0db00e5aa3cca3cc68d2c61273f5e18643b9b0045357'

url = f'https://api.vk.com/method/users.get?user_ids={user_id}&access_token={access_token}&v=5.89'

try:
    response = requests.get(url).json()
    user_info = response['city'][0]

    print(user_info['city'])
    with open('.gitignore/user_vk.txt', 'w') as f:
        json.dump(user_info, f, indent=4)

except Exception as err:
        print("Error")
