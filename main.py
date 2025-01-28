import requests
import json

class Agent:
    def __init__(self, displayName, description, role, abilities, releaseDate):
        self.displayName = displayName
        self.description = description
        self.role = role
        self.abilities = abilities
        self.releaseDate = releaseDate

    def display_info(self):
        print(f"Name: {self.displayName}")
        print(f"Descirption: {self.description}")
        print(f"Role: {self.role}")
        for ability in self.abilities:
            print(f"Abilities: {ability["displayName"]}")


        print(f"Release Date: {self.releaseDate}")
        

def fetch_agent_data(agent_displayName):
        url = f"https://valorant-api.com/v1/agents"
        response = requests.get(url)
        if response.status_code == 200:
            agent_data = response.json()
            return agent_data
        else:
            print(f"Error fetching data for {agent_displayName}.")
            return None
        

def create_agent(agent_json):

        agent = Agent(
                        agent_json["displayName"],
                        agent_json["description"],
                        agent_json["role"]["displayName"],
                        agent_json["abilities"],
                        agent_json["releaseDate"]
                     )
        return agent
        


print()
print("Welcome to the Valorant Agent Tracker App!")
print("Track different data about your selected agent!")
print()

agents = []
releaseDates = []

while True:
    user_input = input("Enter an agents name: ").strip()
    print()

    agent_data = fetch_agent_data(user_input)["data"]

    for agent in agent_data:
        if user_input == agent["displayName"]:
            print(agent["displayName"])
            agent_obj = create_agent(agent)
            agent_obj.display_info()
            agents.append(agent_obj)
        
    print()
    Continue = input("Would you like to select another agent (y/n): ").strip()
    if Continue == "n":
         break
    



print()
print("Here's the agenst you have asked for during this session:")
for agent in agents:
     print(f"Agents: {agents}")
    

    

        


