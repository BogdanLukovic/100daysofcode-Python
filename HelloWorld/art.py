import game_data

a = game_data.resources
print(f"a: {a}")
print(f"game data resources: {game_data.resources}")
a["water"] = 999
print(f"a: {a}")
print(f"game data resources: {game_data.resources}")

