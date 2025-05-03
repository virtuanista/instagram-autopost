import os
from instagrapi import Client

# Configuración
USERNAME = "your_username"  # Cambia esto por tu nombre de usuario de Instagram
PASSWORD = "your_password"  # Cambia esto por tu contraseña de Instagram
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "imagenes")
POSTED_DIR = os.path.join(os.path.dirname(__file__), "publicadas")

def main():
    # Crear carpetas si no existen
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(POSTED_DIR, exist_ok=True)

    images = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not images:
        # No hay imágenes, salir sin hacer nada ni conectarse a Instagram
        return

    cl = Client()
    cl.login(USERNAME, PASSWORD)

    image_to_post = images[0]
    image_path = os.path.join(IMAGES_DIR, image_to_post)
    caption = ""  # Caption vacío, opcional

    try:
        cl.photo_upload(image_path, caption)
        os.rename(image_path, os.path.join(POSTED_DIR, image_to_post))
        print(f"Publicado: {image_to_post}")
    except Exception as e:
        print(f"Error publicando {image_to_post}: {e}")

if __name__ == "__main__":
    main()