from garpixcms.urls import *  # noqa

urlpatterns = [
    #  garpix_faq
    path('', include(('garpix_faq.urls', 'garpix_faq'), namespace='garpix_faq')),  # noqa:F405
] + urlpatterns  # noqa
