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

    EDUCATION_LEVEL_CHOICES = [
        ('primary', 'ابتدائي'),
        ('middle', 'إعدادي'),
        ('high_school', 'ثانوي'),
        ('bachelor', 'بكالوريوس'),
        ('master', 'ماجستير'),
        ('phd', 'دكتوراه'),
    ]

    FAMILY_STATUS_CHOICES = [
        ('single', 'أعزب'),
        ('married', 'متزوج'),
        ('divorced', 'مطلق'),
        ('widowed', 'أرمل'),
    ]

    FINANCIAL_STATUS_CHOICES = [
        ('excellent', 'ممتاز'),
        ('good', 'جيد'),
        ('average', 'متوسط'),
        ('weak', 'ضعيف'),
        ('very_weak', 'ضعيف جداً'),
    ]

    HAS_PASSPORT_CHOICES = [
        ('yes', 'نعم'),
        ('no', 'لا'),
    ]

    # الحقول المطلوبة
    religion = forms.ChoiceField(choices=RELIGION_CHOICES, required=True, label="الديانة")
    sect = forms.ChoiceField(choices=SECT_CHOICES, required=False, label="المذهب")
    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES, required=True, label="القومية")
    language = forms.CharField(label="اللغة الأم", required=True)
    political_view = forms.ChoiceField(choices=POLITICAL_CHOICES, required=False, label="التوجه السياسي")
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES, required=True, label="سبب الهجرة")

    education_level = forms.ChoiceField(choices=EDUCATION_LEVEL_CHOICES, required=True, label="المستوى الدراسي")
    academic_degrees = forms.CharField(label="الشهادات الجامعية", required=False)
    family_status = forms.ChoiceField(choices=FAMILY_STATUS_CHOICES, required=True, label="الحالة الاجتماعية")
    has_passport = forms.ChoiceField(choices=HAS_PASSPORT_CHOICES, required=True, label="هل تمتلك جواز سفر؟")
    nationality = forms.CharField(label="الجنسية", required=True)
    financial_status = forms.ChoiceField(choices=FINANCIAL_STATUS_CHOICES, required=True, label="الوضع المالي")
