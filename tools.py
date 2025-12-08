import os
import requests
from datetime import datetime
from crewai_tools import tool
from openai import OpenAI
from dotenv import load_dotenv # <--- 1. IMPORTANTE

# 2. CARGAR VARIABLES DE ENTORNO
load_dotenv()

class ViralTools:
    
    @tool("Generador de Imágenes DALL-E 3")
    def generar_imagen_dalle(prompt: str):
        """
        Útil para crear imágenes visuales basadas en un prompt detallado.
        Recibe un prompt de texto, genera la imagen con DALL-E 3, 
        la guarda localmente y devuelve la ruta del archivo.
        """
        print(f"🎨 PINTANDO: {prompt[:50]}...") 

        client = OpenAI() # Toma la clave automáticamente gracias a load_dotenv()

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            img_data = requests.get(image_url).content

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"viral_puzzle_{timestamp}.png"
            
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            
            return f"Imagen generada exitosamente y guardada como: {filename}"

        except Exception as e:
            return f"Error al generar imagen: {str(e)}"
    
    @tool("Notificador de Telegram")
    def enviar_telegram(ruta_imagen: str, texto_caption: str):
        """
        Envía una foto local y un texto a un chat de Telegram.
        Args:
            ruta_imagen: La ruta del archivo .png en el ordenador.
            texto_caption: El texto que acompañará a la foto.
        """
        # Ahora sí encontrará las claves porque hicimos load_dotenv() arriba
        token = os.getenv('TELEGRAM_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not token or not chat_id:
            return "Error: Faltan credenciales de Telegram en .env"

        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        
        try:
            # Abrimos la imagen en modo lectura binaria ('rb')
            with open(ruta_imagen, 'rb') as foto:
                payload = {'chat_id': chat_id, 'caption': texto_caption}
                files = {'photo': foto}
                
                resp = requests.post(url, data=payload, files=files)
                
            if resp.status_code == 200:
                return "Notificación enviada a Telegram con éxito."
            else:
                return f"Error Telegram: {resp.text}"
                
        except Exception as e:
            return f"Error enviando a Telegram: {str(e)}"