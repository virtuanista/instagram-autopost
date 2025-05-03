# Instagram Autopost

Este proyecto es un autopublicador de imágenes en Instagram usando Python y la librería `instagrapi`. Permite publicar automáticamente imágenes desde una carpeta específica en tu cuenta de Instagram, ideal para automatizar publicaciones periódicas.

## Requisitos

- Python 3.7 o superior
- Una cuenta de Instagram
- Acceso a un servidor (Linux recomendado para automatización con cron)

## Instalación

1. **Clona o descarga este repositorio en tu servidor o PC.**

2. **Instala las dependencias:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Configura tus credenciales:**

   Edita el archivo `autopost.py` y reemplaza:
   ```python
   USERNAME = "your_username"  # Cambia esto por tu nombre de usuario de Instagram
   PASSWORD = "your_password"  # Cambia esto por tu contraseña de Instagram
   ```

4. **Coloca las imágenes a publicar:**

   - Pon las imágenes que quieras publicar en la carpeta `imagenes/`.
   - Los formatos soportados son `.jpg`, `.jpeg` y `.png`.

5. **Ejecución manual:**

   Puedes ejecutar el script manualmente con:
   ```sh
   python autopost.py
   ```
   Si hay imágenes en la carpeta `imagenes/`, publicará la primera y la moverá a la carpeta `publicadas/`.

## Automatización con cron (Linux)

Para publicar automáticamente varias veces al día, puedes usar `cron`:

1. Edita el crontab:
   ```sh
   crontab -e
   ```

2. Añade la siguiente línea para publicar a las 07:00, 16:00 y 20:00:
   ```
   0 7,16,20 * * * /usr/bin/python3 /root/instagram/autopost.py >> /root/instagram/autopost.log 2>&1
   ```
   Ajusta la ruta a tu script y a tu Python si es necesario.

## Funcionamiento del código

- El script revisa la carpeta `imagenes/`.
- Si hay imágenes, se conecta a Instagram y publica la primera imagen encontrada (alfabéticamente).
- Tras publicar, mueve la imagen a la carpeta `publicadas/`.
- Si no hay imágenes, el script termina sin conectarse a Instagram.
- El caption de la publicación es vacío, pero puedes modificarlo en el código si lo deseas.

## Notas de seguridad
- No compartas tu usuario y contraseña de Instagram.
- Considera usar variables de entorno o un archivo `.env` para mayor seguridad.

## Problemas comunes
- Si Instagram detecta actividad sospechosa, puede pedir verificación o bloquear temporalmente la cuenta.
- No publiques demasiado seguido para evitar restricciones (1-3 veces al día es seguro).

## Licencia


<p align="center">
	Repositorio generado por <a href="https://github.com/sabiopobre" target="_blank">virtu 🎣</a>
</p>

<p align="center">
	<img src="https://open.soniditos.com/cat_footer.svg" />
</p>

<p align="center">
	Copyright &copy; 2025
</p>

<p align="center">
	<a href="/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>