import requests


class poke:
    def satosi(p):
        url2 = "https://pokeapi.co/api/v2/pokemon-species/"

        name_list = {}
        for i in range(151):
            response = requests.get(url2 + str(i + 1))
            pokemon_data = response.json()
            name_list[pokemon_data["names"][0]["name"]] = int(i) + 1

        response = requests.get(url2 + str(name_list[p]))
        pokemon_data = response.json()

        ja_name = pokemon_data["names"][0]["name"]

        url = "https://pokeapi.co/api/v2/pokemon/" + str(name_list[p])
        response = requests.get(url)
        pokemon_data = response.json()

        id = pokemon_data["id"]
        name = pokemon_data["name"]
        height = pokemon_data["height"] / 10
        weight = pokemon_data["weight"] / 10

        return id, ja_name, height, weight


while True:
    p = input("name")
    data = poke.satosi(p)
    print(F'図鑑番号 {data[0]} 名前 {data[1]} 高さ {data[2]}m 重さ　{data[3]}Kg')
    if p == "p":
        break
