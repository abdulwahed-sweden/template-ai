# myapp/views.py

from django.shortcuts import render
from .forms import ImmigrationForm
import requests

DEEPSEEK_API_KEY = "sk-773de8b532124106953e1e7ac0372cb9"

def home(request):
    return render(request, 'myapp/home.html')

def immigration_advisor(request):
    result = None
    if request.method == 'POST':
        form = ImmigrationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data

            prompt = f"""
Suggest the best 3 countries for immigration for a person with the following characteristics:
- Religion: {user_data['religion']}
- Sect: {user_data['sect']}
- Ethnicity: {user_data['ethnicity']}
- Native Language: {user_data['language']}
- Political View: {user_data['political_view']}
- Migration Purpose: {user_data['purpose']}

Please consider cultural compatibility, existing diaspora, integration levels, and safety.
Return only country names with short justification.
"""

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            }

            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }

            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                data = response.json()
                result = data['choices'][0]['message']['content']
            else:
                result = "حدث خطأ أثناء الاتصال بـ DeepSeek API."
    else:
        form = ImmigrationForm()

    return render(request, 'myapp/immigration_form.html', {'form': form, 'result': result})
