from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from decimal import Decimal

register = template.Library()

@register.filter
def format_number(value):
    """Format number with commas"""
    if value is None:
        return '0'
    if isinstance(value, (int, float, Decimal)):
        return intcomma(int(value))
    return value

@register.filter
def format_currency(value):
    """Format currency value with $ and commas"""
    if value is None:
        return '$0.00'
    try:
        if isinstance(value, Decimal):
            num = float(value)
        elif isinstance(value, (int, float)):
            num = float(value)
        else:
            num = float(str(value))
        formatted = f"{num:,.2f}"
        return f"${formatted}"
    except (ValueError, TypeError):
        return '$0.00'

