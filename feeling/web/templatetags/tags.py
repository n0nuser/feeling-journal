from django import template
from json import loads

register = template.Library()


@register.filter()
def field_name_to_label(value):
    return value.replace("_", " ").capitalize()


@register.filter()
def typeof(value):
    return str(type(value))


@register.filter()
def todict(value):
    try:
        return loads(value.replace("\'", "\""))
    except Exception:
        return value


@register.filter
def currency(value):
    if value is None:
        return None
    value = "{:,.2f}€".format(value)
    main_currency, fractional_currency = value.split(".")[0], value.split(".")[1]
    new_main_currency = main_currency.replace(",", ".")
    return f"{new_main_currency},{fractional_currency}"


@register.filter
def subtract(value, arg):
    return value - arg
