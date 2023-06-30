
{% macro dbt_audit_details(results) %}
    {% set slno = namespace(serialnm=0) %}
    {% if execute %}
        { 
        "dbt_version": "{{ dbt_version }}",
        "env": {{ env|replace("'", "''") }},
        "modelbuilds": [
                        {% for res in results -%}
                            {
                                      {% set slno.serialnm = slno.serialnm + 1 %}
                                      "slno": "{{ slno.serialnm }}",
                                      "node": "{{ res.node.unique_id }}",
                                    "status": "{{ res.status }}",
                                   "message": "{{ res.message|replace("\\", "/")|replace("\n", "\\\\n")|replace("'", "''")|replace("\"", "\\\\\\\"") }}",
                            "execution_time": "{{ res.execution_time }}",
                          "adapter_response":{
                                                     "code":"{{ res.adapter_response.code }}",
                                            "rows_affected":"{{ res.adapter_response.rows_affected }}",
                                                 "query_id":"{{ res.adapter_response.query_id }}"
                                             },
                                    "timing": [
                                                {% for restm in res.timing -%}             
                                                    {       "name":"{{ restm.name }}",
                                                      "started_at":"{{ restm.started_at }}",
                                                    "completed_at":"{{ restm.completed_at }}"
                                                    }{% if not loop.last %},{% endif %}                 
                                                {% endfor %}
                                              ]
                            }{% if not loop.last %},{% endif %}
                        {% endfor %}
                       ] 
        }
    {% endif %}

{% endmacro %}

