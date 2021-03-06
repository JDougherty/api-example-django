from datetime import timedelta

from django.db.models.fields import BLANK_CHOICE_DASH


def get_user_access_token(user, provider='drchrono'):
    return user.social_auth.get(provider=provider).extra_data.get('access_token')


def add_blank_to_choices(choices):
    return BLANK_CHOICE_DASH + list(choices)


def choices_with_title(choices):
    return map(lambda x: (x, x.title().replace('_', ' ')), choices)


def format_timedelta(td):
    # Source: http://stackoverflow.com/a/8408947/1025963
    if td < timedelta(0):
        return '-' + format_timedelta(-td)
    else:
        # Change this to format positive timedeltas the way you want
        return str(td)
