from google.cloud import translate

# Crea una instancia del cliente de Translate
client = translate.TranslationServiceClient()

# Tu proyecto de Google Cloud y tu región
#AIzaSyDpOgAzBDstYHfZNoDzi5evK-0NtQk8iCk
project_id ="AIzaSyDpOgAzBDstYHfZNoDzi5evK-0NtQk8iCk"
location = "global" # Ejemplo: "global"

# Texto que quieres traducir y el idioma al que quieres traducirlo
texto_a_traducir = "Hello, Welcome to our rustic duck farm!"
idioma_destino = "es"  

# Prepara la solicitud de traducción
parent = f"projects/{project_id}/locations/{location}"
response = client.translate_text(
    parent=parent,
    contents=[texto_a_traducir],
    target_language_code=idioma_destino,
)
traduccion = response.translations[0].translated_text

print(f"Texto original: {texto_a_traducir}")
print(f"Traducción: {traduccion}")
