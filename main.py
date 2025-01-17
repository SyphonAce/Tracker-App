import requests
import json

class Agent:
    def __init__(self, name, description, role, abilities, releaseDate):
        self.name = name
        self.description = description
        self.role = role
        self.abilities = abilities
        self.releaseDate = releaseDate
        


url = f"https://valorant-api.com/v1/agents"


response = 