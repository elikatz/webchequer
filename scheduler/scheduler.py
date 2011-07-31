from django.core.exceptions import ValidationError
import re, datetime


def validateDayOfWeek(value):
    #Here we use U as Saturday for the last day of the week
    flag = bool(re.compile('^S?M?T?W?R?F?U?$').match(value))
    if not flag:
        raise ValidationError(u'%s is not a valid combination of days of the week' % value)

def validateModernAndExistingYear(value):
    if int(value) not in range(1940, datetime.datetime.now().year + 1):
        raise ValidationError('%s is not a valid year' % value)
    
    
    