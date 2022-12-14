{% extends 'UKpracaApp/base.html' %}
{% load static %}


{% block tittle %} View List {% endblock %}

{% block content %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>UKpraca</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
    <link rel="stylesheet" href="{% static 'UKpracaApp/styles.css' %}">



</head>
<body class="bg-light">

    <div class="container">
        <div class="row mt-5">
            <div class="col-md-8 offset-md-2">

                <div class="card">
                    <div class="card-header shadow-sm bg-white">
                   <h1 class="display-5 text-info"><i class="fas fa-check-double"></i> UKpraca </h1>
                    </div>
                    <div class="card-body"></div>
                    <form action="{% url 'insert_praca_user' %}" method="post" autocomplete="off">
                        {% csrf_token %}
                        <div class="input-group">
                            <input type="name" class="form-control" name="name" placeholder="Twoje Imię">
                            <div class="input-group-append text-info">
                                <span class="input-group-text bg-white py-0">
                                    <button type="submit" class="btn btn-sm text-info">
                                        <i class="fa fa-plus-circle fa-lg"></i>

                                    </button>
                                </span>
                            </div>
                        </div>


                        </form>

                </div>


            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
            integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"></script>



</body>

{% endblock %}

</html>