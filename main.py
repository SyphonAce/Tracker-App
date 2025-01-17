import requests
import json

class Agent:
    def __init__(self, name, description, role, abilities, releaseDate):
        self.name = name
        self.description = description
        self.role = role
        self.abilities = abilities
        self.releaseDate = releaseDate

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Descirption: {self.description}")
        print(f"Role: {self.role}")
        print(f"Abilities: {self.abilities}")
        print(f"Release Date: {self.releaseDate}")
        

    def fetch_agent_data(agent_name):
        url = f"https://valorant-api.com/v1/agents"
        response = requests.get(url)

        if response.status_code == 200:
            agent_data = response.json()
            return agent_data
        else:
            print(f"Error fetching data for {agent_name}.")
            return None



