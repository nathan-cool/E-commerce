from django.contrib.sitemaps import GenericSitemap
from store.sitemaps import StoreSitemap

sitemaps = {
    'store': StoreSitemap,
}
