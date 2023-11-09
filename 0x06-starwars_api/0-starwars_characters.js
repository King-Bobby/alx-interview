#!/usr/bin/node

import requests
import sys


def get_movie_characters(movie_id):
    api_url = f"https://swapi-api.alx-tools.com/api/films/{movie_id}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        movie_data = response.json()

        characters = movie_data.get("characters", [])

        for character_url in characters:
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()

            print(character_data["name"])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_movie_characters(movie_id)
