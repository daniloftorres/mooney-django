from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'admin', 'mooney.routes.admin', name='admin-django'),
    host(r'api', 'mooney.routes.urls_api', name='api'),
)
