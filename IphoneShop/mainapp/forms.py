from .models import Telephone, Employees, Clients, Models, Feedback
from django.forms import ModelForm, TextInput, Textarea, EmailInput, NumberInput
class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields=['name', 'numb', 'mail', 'color', 'count', 'empl']

        widgets = {
            'name': TextInput(attrs={
                'class': 'FIO',
                'placeholder': 'ФИО'
            }),
            'numb': NumberInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона в формате 7XXXXXXXXXX'
            }),
            'mail': EmailInput(attrs={
                'class': 'mail',
                'placeholder': 'Почта'
            }),
            'color': TextInput(attrs={
                'class': 'color',
                'placeholder': 'Цвет'
            }),
            'count': TextInput(attrs={
                'class': 'value',
                'placeholder': 'Количество'
            }),
            'empl': TextInput(attrs={
                'class': 'FIO-sot',
                'placeholder': 'ФИО Сотрудника(опционально)',
            })
        }
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields=['fio', 'feed']

        widgets = {
            'fio': TextInput(attrs={
                'class': 'iname',
                'placeholder': 'Ваше Имя Фамилия'
            }),
            'feed': Textarea(attrs={
                'class': 'itext',
                'placeholder': 'Текст отзыва'
            })

        }
