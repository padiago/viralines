import os
import requests
from datetime import datetime
from crewai_tools import tool
from openai import OpenAI

class ViralTools:
    
    @tool("Generador de Imágenes DALL-E 3")
    def generar_imagen_dalle(prompt: str):
        """
        Útil para crear imágenes visuales basadas en un prompt detallado.
        Recibe un prompt de texto, genera la imagen con DALL-E 3, 
        la guarda localmente y devuelve la ruta del archivo.
        """
        print(f"🎨 PINTANDO: {prompt[:50]}...") # Log para que veas que funciona

        # 1. Configurar cliente (toma la clave del .env automáticamente)
        client = OpenAI()

        try:
            # 2. Solicitar la imagen a OpenAI
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            # 3. Obtener la URL de la imagen generada
            image_url = response.data[0].url

            # 4. Descargar la imagen
            img_data = requests.get(image_url).content

            # 5. Generar nombre de archivo único (con fecha y hora)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"viral_puzzle_{timestamp}.png"
            
            # 6. Guardar en disco
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            
            return f"Imagen generada exitosamente y guardada como: {filename}"

        except Exception as e:
            return f"Error al generar imagen: {str(e)}"