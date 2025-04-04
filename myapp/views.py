# myapp/views.py

from django.shortcuts import render
from .forms import ImmigrationForm
import requests
import markdown


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
            اقترح أفضل 3 دول للهجرة لشخص لديه الخصائص التالية:
            - الديانة: {user_data['religion']}
            - المذهب: {user_data['sect']}
            - القومية: {user_data['ethnicity']}
            - اللغة الأم: {user_data['language']}
            - التوجه السياسي: {user_data['political_view']}
            - المستوى الدراسي: {user_data['education_level']}
            - الشهادات الجامعية: {user_data['academic_degrees']}
            - الحالة الاجتماعية: {user_data['family_status']}
            - هل يمتلك جواز سفر: {user_data['has_passport']}
            - الجنسية: {user_data['nationality']}
            - الوضع المالي: {user_data['financial_status']}
            - سبب الهجرة: {user_data['purpose']}

            رجاءً أجب باللغة العربية فقط، وبصيغة تقرير مفصلة.  
            استخدم التنسيق التالي:
            - عناوين للدول
            - نقاط واضحة تحت كل عنوان
            - توصية ختامية

            استخدم رموز Markdown مثل **، ###، - لتنسيق النص.
            """

            headers = {
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }

            response = requests.post("https://api.deepseek.com/v1/chat/completions", json=payload, headers=headers)

            if response.status_code == 200:
                markdown_text = response.json()['choices'][0]['message']['content']
                result = markdown.markdown(markdown_text)  # ✅ تحويل Markdown إلى HTML
            else:
                result = "❌ حدث خطأ أثناء الاتصال بواجهة DeepSeek."

    else:
        form = ImmigrationForm()

    return render(request, 'myapp/immigration_form.html', {'form': form, 'result': result})
