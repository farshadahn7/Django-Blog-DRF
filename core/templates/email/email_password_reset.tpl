{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ username }}
{% endblock %}

{% block body %}
Your password is reset. please click on link below to confirm a new password.
<a href="http://127.0.0.1:8001/accounts/api/v1/reset-password/{{ access_token }}/" target=blank> click for password reset </a>
{% endblock %}

