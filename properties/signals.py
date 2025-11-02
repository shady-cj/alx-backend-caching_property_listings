from .models import Property
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from django.core.cache import cache

# clear cache after saving a Property
@receiver(post_save, sender=Property)
def clear_property_cache_on_save(sender, instance, **kwargs):
    cache.delete("all_properties")

# clear cache after deleting a Property
@receiver(post_delete, sender=Property)
def clear_property_cache_on_delete(sender, instance, **kwargs):
    cache.delete("all_properties")