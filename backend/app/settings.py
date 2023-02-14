from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa:F405
    'garpix_faq'
]

MIGRATION_MODULES.update({  # noqa:F405
    'fcm_django': 'app.migrations.fcm_django',
    'garpix_faq': 'app.migrations.garpix_faq'
})
