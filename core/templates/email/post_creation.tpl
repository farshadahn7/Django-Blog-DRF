{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ username }}
{% endblock %}

{% block body %}
Your post has been successfully created. If The status sets to pub, It is published on the net.
{% endblock %}

