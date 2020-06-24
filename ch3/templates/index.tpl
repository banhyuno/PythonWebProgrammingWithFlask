{% extends "layout.html" %}
{% block head %}
title
{% endblock %}
{% block body %}
    <ul>
    {% for user in users %}
        <li><a href="{{user.url}}">{{user.username}}</a></li>
    {% endfor %}
    </ul>
{% endblock %}
{% block footer %}
    blockbody2?
    body
    <hr/>
    {{data1}}<br>
    {{data2}}
    <hr/>
    <div>
        {% if True %}
        <br>TTTTTTT
        {% endif %}
        {# TODO : ~~~~~~ #}<br>
    </div>
    <hr/>
    {%- for item in seq -%}
        {{item}}
    {% endfor %}
{% endblock %}
