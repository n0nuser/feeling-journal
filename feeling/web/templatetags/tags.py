from django import template
import datetime
from json import loads

register = template.Library()


@register.filter()
def field_name_to_label(value):
    return value.replace("_", " ").capitalize()


@register.filter()
def typeof(value):
    return str(type(value))


@register.filter()
def date_or_string(value):
    not_date_types = (str, int, float, bool)
    for value_type in not_date_types:
        if isinstance(value, value_type):
            return value
    return value.strftime("%d/%m/%Y %H:%M:%S")


@register.filter
def get_obj_attr(obj, attr):
    """
    Improvement of https://stackoverflow.com/a/32158083/16612992 for foreign keys.
    """
    # Get data from a foreign key
    if "__" in attr:
        attr = attr.split("__")
        for a in attr:
            obj = getattr(obj, a)
        return obj
    # Return field value
    return getattr(obj, attr)


@register.filter()
def todict(value):
    try:
        return loads(value.replace("'", '"'))
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
