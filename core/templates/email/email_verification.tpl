{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ username }}
{% endblock %}

{% block body %}
Thanks for registration. For completing the registration process you have to click on the link below to verify your account.
<a href="http://127.0.0.1:8001/accounts/api/v1/user-verification/{{ access_token }}/" target=blank> click for verification </a>
{% endblock %}

