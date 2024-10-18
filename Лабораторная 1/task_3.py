list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

sred_index = len(list_players) // 2

first_team = list_players[:sred_index]
second_team = list_players[sred_index:]

print(f"Первая команда {first_team}")
print(f"Вторая команда {second_team}")
