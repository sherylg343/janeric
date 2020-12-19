from pytz import timezone
from datetime import datetime
from django.conf import settings
from urllib import parse


def common_variables(request):
    """ Declare time zone variable to store time zone abbreviation """
    tzname = request.COOKIES.get('timezone') or settings.CLIENT_DEFAULT_TIME_ZONE
    return {
       "timezone_name": datetime.now(timezone(parse.unquote(tzname))).tzname()
    }
