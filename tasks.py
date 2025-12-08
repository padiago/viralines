import yaml
from crewai import Task

class ViralTasks:
    def __init__(self):
        # Cargamos el archivo YAML de tareas
        with open('config/tasks.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def task_inventar_problema(self, agent):
        return Task(
            description=self.config['inventar_problema']['description'],
            expected_output=self.config['inventar_problema']['expected_output'],
            agent=agent
        )

    def task_crear_prompt_visual(self, agent, context_task):
        return Task(
            description=self.config['crear_prompt_visual']['description'],
            expected_output=self.config['crear_prompt_visual']['expected_output'],
            agent=agent,
            context=[context_task]
        )
    
    def task_redactar_caption(self, agent, context_tasks):
        return Task(
            description=self.config['redactar_caption']['description'],
            expected_output=self.config['redactar_caption']['expected_output'],
            agent=agent,
            context=context_tasks, # Le pasamos TODO el contexto anterior
            output_file='caption_post.txt' # <-- ¡OJO! Esto guarda el archivo automáticamente
        )