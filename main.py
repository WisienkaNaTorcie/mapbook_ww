users:list[dict] = [
    {'name': 'Wika', 'location': 'Radzyń Podlaski', 'posts': 1, },
    {'name': 'Daria', 'location': 'Łosice', 'posts': 500, },
    {'name': 'Kuba', 'location': 'Płock', 'posts': 200, }
]


def get_user_info(users_data: list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]} postów')

get_user_info(users)