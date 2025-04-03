# myapp/forms.py

from django import forms

class ImmigrationForm(forms.Form):
    RELIGION_CHOICES = [
        ('muslim_sunni', 'مسلم سني'),
        ('muslim_shia', 'مسلم شيعي'),
        ('christian', 'مسيحي'),
        ('none', 'بدون انتماء ديني'),
        ('other', 'أخرى'),
    ]

    SECT_CHOICES = [
        ('sunni', 'سني'),
        ('shia', 'شيعي'),
        ('none', 'بدون مذهب'),
        ('other', 'أخرى'),
    ]

    ETHNICITY_CHOICES = [
        ('arab', 'عربي'),
        ('kurdish', 'كردي'),
        ('persian', 'فارسي'),
        ('turkish', 'تركي'),
        ('armenian', 'أرمني'),
        ('other', 'أخرى'),
    ]

    POLITICAL_CHOICES = [
        ('liberal', 'ليبرالي'),
        ('conservative', 'محافظ'),
        ('secular', 'علماني'),
        ('islamist', 'إسلامي'),
        ('none', 'بدون انتماء سياسي'),
    ]

    PURPOSE_CHOICES = [
        ('study', 'دراسة'),
        ('work', 'عمل'),
        ('asylum', 'لجوء'),
        ('family', 'لمّ شمل عائلي'),
        ('other', 'أخرى'),
    ]

    religion = forms.ChoiceField(choices=RELIGION_CHOICES, required=True, label="الديانة")
    sect = forms.ChoiceField(choices=SECT_CHOICES, required=False, label="المذهب")
    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES, required=True, label="القومية")
    language = forms.CharField(label="اللغة الأم", required=True)
    political_view = forms.ChoiceField(choices=POLITICAL_CHOICES, required=False, label="التوجه السياسي")
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES, required=True, label="سبب الهجرة")
