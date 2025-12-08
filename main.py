import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Importamos nuestras nuevas clases
from agents import ViralAgents
from tasks import ViralTasks

# Cargar claves
load_dotenv()

def run():
    agents = ViralAgents()
    tasks = ViralTasks()

    # 1. Crear Agentes
    matematico = agents.matematico_agent()
    director = agents.director_creativo_agent()
    redactor = agents.redactor_social_agent() # <-- NUEVO FICHAJE

    # 2. Crear Tareas
    tarea_logica = tasks.task_inventar_problema(matematico)
    tarea_visual = tasks.task_crear_prompt_visual(director, tarea_logica)
    
    # El redactor necesita saber qué pensó el matemático y qué pidió el director
    tarea_redaccion = tasks.task_redactar_caption(redactor, [tarea_logica, tarea_visual])

    # 3. Formar el Crew
    equipo = Crew(
        agents=[matematico, director, redactor],
        tasks=[tarea_logica, tarea_visual, tarea_redaccion],
        verbose=True,
        process=Process.sequential
    )

    # 4. Ejecutar
    print("🤖 Generando contenido viral completo...")
    resultado = equipo.kickoff()
    
    print("\n########################")
    print("## PROCESO TERMINADO ##")
    print("########################\n")

# Esto es una buena práctica: asegura que el código solo corre si ejecutas este archivo directamente
if __name__ == "__main__":
    run()