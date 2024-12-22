import google.generativeai as genai
from django.conf import settings

from apps.check_scanner.utils.recommendations_utils import process_recommendations

genai.configure(api_key=settings.GOOGLE_TOKEN)
model = genai.GenerativeModel(model_name='gemini-1.5-pro')

def generate_text(text: str) -> str:
    message = ('Write me recommendations in 100 words on how ' +
               'I could reduce my spending when buying groceries: ' +
               text + ',  after the recommendations write me a text in 50 words, ' +
               'motivation, where I could usefully spend the money.')
    response = model.generate_content(message)
    processed_recommendations = process_recommendations(response.text)
    return processed_recommendations