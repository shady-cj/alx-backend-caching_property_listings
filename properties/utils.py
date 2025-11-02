from django.core.cache import cache
from .models import Property

import logging

logger = logging.getLogger(__name__)



def get_all_properties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)
    
    return queryset
        

def get_redis_cache_metrics():
    from django_redis import get_redis_connection
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)


    if hits + misses == 0:
        hit_ratio = None  # avoid division by zero
    else:
        hit_ratio = hits / (hits + misses)

    logger.info(
            f"Redis cache stats: hits={hits}, misses={misses}, hit_ratio={hit_ratio:.2%}"
        )
    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }
    return metrics
