from django.shortcuts import render
import requests
import os

def translate_text(request):
    translated_text = None
    error_message = None

    if request.method == 'POST':
        text_to_translate = request.POST.get('text', '').strip()
        to_lang = request.POST.get('to_lang', 'es').strip()

        if text_to_translate:
            subscription_key = os.getenv("AZURE_TRANSLATOR_KEY")
            endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
            location = os.getenv("AZURE_TRANSLATOR_LOCATION")

            path = '/translate'
            params = {
                'api-version': '3.0',
                'to': to_lang
            }

            constructed_url = endpoint + path

            headers = {
                'Ocp-Apim-Subscription-Key': subscription_key,
                'Ocp-Apim-Subscription-Region': location,
                'Content-type': 'application/json'
            }

            body = [{'text': text_to_translate}]
            response = requests.post(constructed_url, params=params, headers=headers, json=body)

            if response.status_code == 200:
                translated_text = response.json()[0]['translations'][0]['text']
            else:
                error_message = f"Error en la traducción: {response.status_code} - {response.text}"
        else:
            error_message = "Texto vacío. Por favor, ingrese algo para traducir."

    return render(request, 'translate.html', {
        'translated_text': translated_text,
        'error_message': error_message
    })
