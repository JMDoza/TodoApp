from django import template
import datetime

register = template.Library()

def subtractor(value_1, value_2):
    value_3 = value_1 - value_2
    return value_3 > datetime.timedelta(seconds=1)

register.filter('subtractor', subtractor)