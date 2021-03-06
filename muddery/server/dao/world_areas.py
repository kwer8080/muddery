"""
Query and deal common tables.
"""

from muddery.server.dao.base_query import BaseQuery


class WorldAreas(BaseQuery):
    """
    All areas in the game world.
    """
    table_name = "world_areas"
