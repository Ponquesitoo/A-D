'''
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class TranslateDocumentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_translate_valid_pdf(self):
        with open('doc_translate_API/test_files/sample.pdf', 'rb') as pdf:
            file = SimpleUploadedFile("sample.pdf", pdf.read(), content_type='application/pdf')
            response = self.client.post(
                reverse('translate_document'),
                {'document': file}
            )
        print("✔ test_translate_valid_pdf →", response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'%PDF', response.content)  # Esperamos que vuelva un PDF

    def test_translate_invalid_file_type(self):
        file = SimpleUploadedFile("notes.txt", b"Texto plano", content_type='text/plain')
        response = self.client.post(
            reverse('translate_document'),
            {'document': file}
        )
        print("✔ test_translate_invalid_file_type →", response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_translate_no_file_uploaded(self):
        response = self.client.post(reverse('translate_document'), {})
        print("✔ test_translate_no_file_uploaded →", response.status_code)
        self.assertEqual(response.status_code, 400)

'''
