from elasticsearch import Elasticsearch

from idunn.places import POI
from idunn.utils.settings import Settings
from idunn.api.utils import fetch_es_poi, DEFAULT_VERBOSITY

def get_poi(id, es: Elasticsearch, settings: Settings, lang=None) -> POI:
    """Handler that returns points-of-interest"""
    if not lang:
        lang = settings['DEFAULT_LANGUAGE']
    lang = lang.lower()

    es_poi = fetch_es_poi(id, es)
    return POI(es_poi).load_place(lang, verbosity=DEFAULT_VERBOSITY)
