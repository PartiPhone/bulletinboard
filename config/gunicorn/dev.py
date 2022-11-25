wsgi_app = 'bboard.wsgi:application'
workers = 2
loglevel = 'debug'
capture_output = True
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=siteparser.settings'
daemon = True
