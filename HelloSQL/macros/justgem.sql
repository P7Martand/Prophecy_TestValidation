
{%- macro justgem(parameter1) -%}
    select * from {{ parameter1 }}
{%- endmacro -%}
