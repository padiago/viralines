import yaml
from crewai import Agent
from langchain_openai import ChatOpenAI

class ViralAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
        # Cargamos el archivo YAML al iniciar la oficina
        with open('config/agents.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def matematico_agent(self):
        return Agent(
            role=self.config['matematico']['role'],
            goal=self.config['matematico']['goal'],
            backstory=self.config['matematico']['backstory'],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def director_creativo_agent(self):
        return Agent(
            role=self.config['director_arte']['role'],
            goal=self.config['director_arte']['goal'],
            backstory=self.config['director_arte']['backstory'],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )