'''
import os
import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from azure.storage.blob import BlobServiceClient, ContentSettings

# Configurar claves y nombres de contenedores (se puede usar dotenv)
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
SOURCE_CONTAINER_NAME = "originales"  #  Cambiar por el nombre real de tu contenedor de archivos subidos
TRANSLATED_CONTAINER_NAME = "traducidos"  # Cambiar por el contenedor donde Azure guarda los traducidos

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES["documento"]

        # Generar nombre único para evitar sobrescribir
        filename = f"{uuid.uuid4()}_{uploaded_file.name}"

        # Subir archivo al contenedor de origen
        blob_client = blob_service_client.get_blob_client(container=SOURCE_CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(uploaded_file, overwrite=True, content_settings=ContentSettings(content_type=uploaded_file.content_type))

        # LLAMADA A LA API DE TRADUCCIÓN AQUÍ
        # -----------------------------------------------------
        # Acá deberías hacer un request POST/GET a tu API que se encarga
        # de leer el archivo desde Azure y devolver el nombre del archivo traducido
        # traducido_filename = call_translation_api(filename)
        # -----------------------------------------------------
        # Por ahora simulamos esto:
        traducido_filename = f"translated_{filename}"  # Simulación

        # Obtener URL del archivo traducido
        translated_blob_client = blob_service_client.get_blob_client(container=TRANSLATED_CONTAINER_NAME, blob=traducido_filename)
        translated_url = translated_blob_client.url

        return render(request, "upload.html", {
            "translated_url": translated_url,
            "archivo": uploaded_file.name
        })

    return render(request, "upload.html")
'''
