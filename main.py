import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Importamos nuestras nuevas clases
from agents import ViralAgents
from tasks import ViralTasks

# Cargar claves
load_dotenv()

def run():
    # 1. Instanciar (crear) las fábricas de agentes y tareas
    agents = ViralAgents()
    tasks = ViralTasks()

    # 2. Crear los agentes específicos
    matematico = agents.matematico_agent()
    director = agents.director_creativo_agent()

    # 3. Crear las tareas y asignarles los agentes
    tarea1_logica = tasks.task_inventar_problema(matematico)
    tarea2_visual = tasks.task_crear_prompt_visual(director, tarea1_logica)

    # 4. Formar el equipo (Crew)
    equipo = Crew(
        agents=[matematico, director],
        tasks=[tarea1_logica, tarea2_visual],
        verbose=True,
        process=Process.sequential
    )

    # 5. Ejecutar
    print("🤖 Iniciando workflow modular...")
    resultado = equipo.kickoff()
    
    print("\n\n########################")
    print("## RESULTADO FINAL ##")
    print("########################\n")
    print(resultado)

# Esto es una buena práctica: asegura que el código solo corre si ejecutas este archivo directamente
if __name__ == "__main__":
    run()