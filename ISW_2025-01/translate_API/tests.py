from django.test import TestCase
import unittest
import requests
import os

class AzureTranslateAPITestCase(unittest.TestCase):
    def setUp(self):
        self.endpoint = "https://api.cognitive.microsofttranslator.com/translate"
        self.subscription_key = os.getenv("AZURE_TRANSLATE_KEY")  # Asegúrate de que esté seteada
        self.location = os.getenv("AZURE_TRANSLATE_REGION")       # Ejemplo: "eastus"
        self.headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Ocp-Apim-Subscription-Region": self.location,
            "Content-type": "application/json"
        }
        self.params = {
            "api-version": "3.0",
            "from": "en",
            "to": ["es"]
        }

    def test_translation(self):
        """Traducción básica de una frase simple"""
        body = [{"text": "Hello, world!"}]
        response = requests.post(self.endpoint, params=self.params, headers=self.headers, json=body)

        self.assertEqual(response.status_code, 200)
        translation = response.json()[0]['translations'][0]['text'].lower()
        self.assertIn("hola", translation)

    def test_empty_text(self):
        """Envia texto vacío"""
        body = [{"text": ""}]
        response = requests.post(self.endpoint, params=self.params, headers=self.headers, json=body)

        self.assertEqual(response.status_code, 200)
        translation = response.json()[0]['translations'][0]['text']
        self.assertEqual(translation, "")

    def test_multiple_texts(self):
        """Traduce múltiples textos en una sola solicitud"""
        body = [{"text": "Good morning"}, {"text": "Good night"}]
        response = requests.post(self.endpoint, params=self.params, headers=self.headers, json=body)

        self.assertEqual(response.status_code, 200)
        translations = [t['translations'][0]['text'].lower() for t in response.json()]
        self.assertIn("buenos días", translations[0])
        self.assertIn("buenas noches", translations[1])

    def test_invalid_language_code(self):
        """Envía un código de idioma inválido"""
        params = self.params.copy()
        params["to"] = ["invalid"]
        body = [{"text": "Hello"}]
        response = requests.post(self.endpoint, params=params, headers=self.headers, json=body)

        self.assertEqual(response.status_code, 400)  # Bad Request
        self.assertIn("error", response.json())

    def test_missing_api_key(self):
        """Prueba que falle si no se entrega clave API"""
        headers = {
            "Ocp-Apim-Subscription-Key": "",
            "Ocp-Apim-Subscription-Region": self.location,
            "Content-type": "application/json"
        }
        body = [{"text": "Hello"}]
        response = requests.post(self.endpoint, params=self.params, headers=headers, json=body)

        self.assertEqual(response.status_code, 401)  # Unauthorized
        self.assertIn("error", response.json())
