from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from config.settings import EMAIL_HOST_USER, WORKER_LIST


def send_message(db, email_host_user=EMAIL_HOST_USER, worker_list=WORKER_LIST):
    html_context = render_to_string(
        'email/email_feedback.html',
        {
            'name': db.get('name', 'Пользователь не указал ФИО'),
            'phone': db.get('phone', 'Пользователь не указал телефон'),
            'participant': db.get('participant', 'Пользователь не указал питомца'),
            'email': db.get('email', 'Пользователь не указал почту'),
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новая заявка на получение питомца',
        body='',
        from_email=email_host_user,
        to=worker_list,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()
