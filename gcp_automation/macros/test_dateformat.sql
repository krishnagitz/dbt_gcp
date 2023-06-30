{% macro test_assert_date_format (model,column_name,condtion) %}

with results as (
SELECT
  REGEXP_CONTAINS(Dt_Customer, r'^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$') AS expression
FROM
  `ey-poc.ext_table.ey_poc_ext_market_stg`)

select * from results where expression != {{condtion}}

{% endmacro %}