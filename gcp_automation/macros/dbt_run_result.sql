
{% macro dbt_run_result(results) %}

    {% set ns = namespace(errorlevel=6) %}
    {% if execute %}

        {% for res in results -%}

            {% if res.status != "success" %}

                {% if res.status != "pass" %}
                   {% set ns.errorlevel = 3 %}

                {% endif %}  
            {% endif %}
        {% endfor %}
    {% endif %}

{{ return(ns.errorlevel) }}

{% endmacro %}