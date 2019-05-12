"""
Query and deal common tables.
"""

from __future__ import print_function

from evennia.utils import logger
from django.apps import apps
from django.conf import settings
from muddery.utils import defines
from muddery.worlddata.dao.common_mapper_base import ObjectsMapper


class ObjectPropertiesMapper(object):
    """
    Object's properties.
    """
    def __init__(self):
        self.model_name = "object_properties"
        self.model = apps.get_model(settings.WORLD_DATA_APP, self.model_name)
        self.objects = self.model.objects

    def get_properties(self, object):
        """
        Get object's properties.

        Args:
            object: (string) object's key.
        """
        properties = {}
        records = self.objects.filter(object=object)
        for record in records:
            properties[record.attribute] = record.value
        return properties


OBJECT_PROPERTIES = ObjectPropertiesMapper()
