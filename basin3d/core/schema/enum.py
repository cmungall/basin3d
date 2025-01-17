"""
`basin3d.core.schema.enum`
***************************

.. currentmodule:: basin3d.core.schema

:platform: Unix, Mac
:synopsis: BASIN-3D Enumeration Schema
:module author: Val Hendrix <vhendrix@lbl.gov>
:module author: Danielle Svehla Christianson <dschristianson@lbl.gov>

.. contents:: Contents
    :local:
    :backlinks: top


"""
from enum import Enum

from basin3d.core.types import SpatialSamplingShapes

# From https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
PANDAS_TIME_FREQUENCY_MAP = {
    'YEAR': 'A',
    'MONTH': 'M',
    'DAY': 'D',
    'HOUR': 'H',
    'MINUTE': 'T',
    'SECOND': 'S'
}


class BaseEnum(Enum):
    """Base Enumeration Class that adds some helper methods"""

    @classmethod
    def values(cls):
        role_names = [member.value for role, member in cls.__members__.items()]
        return role_names

    @classmethod
    def names(cls):
        return cls._member_names_


class TimeFrequencyEnum(str, BaseEnum):
    """
    Enumeration for time frequencies
    """
    # ToDo: Check OGC for correct term (i.e., replace TimeFrequency)

    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"


class FeatureTypeEnum(str, BaseEnum):
    """Enumeration for Feature Types"""
    REGION = "REGION"
    SUBREGION = "SUBREGION"
    BASIN = "BASIN"
    SUBBASIN = "SUBBASIN"
    WATERSHED = "WATERSHED"
    SUBWATERSHED = "SUBWATERSHED"
    SITE = "SITE"
    PLOT = "PLOT"
    HORIZONTAL_PATH = "HORIZONTAL PATH"
    VERTICAL_PATH = "VERTICAL PATH"
    POINT = "POINT"


FEATURE_SHAPE_TYPES = {
    SpatialSamplingShapes.SHAPE_POINT: [FeatureTypeEnum.POINT],
    SpatialSamplingShapes.SHAPE_CURVE: [FeatureTypeEnum.HORIZONTAL_PATH, FeatureTypeEnum.VERTICAL_PATH],
    SpatialSamplingShapes.SHAPE_SURFACE: [FeatureTypeEnum.REGION, FeatureTypeEnum.SUBREGION, FeatureTypeEnum.BASIN,
                                          FeatureTypeEnum.SUBBASIN,
                                          FeatureTypeEnum.WATERSHED,
                                          FeatureTypeEnum.SUBWATERSHED, FeatureTypeEnum.SITE, FeatureTypeEnum.PLOT],
    SpatialSamplingShapes.SHAPE_SOLID: []
}


class ResultQualityEnum(str, BaseEnum):
    """Enumeration for Result Quality"""

    #: The result has been checked for quality
    CHECKED = "CHECKED"

    #: The result is raw or unchecked for quality
    UNCHECKED = "UNCHECKED"

    #: The result contains checked and unchecked portions
    PARTIALLY_CHECKED = "PARTIALLY_CHECKED"


class StatisticEnum(str, BaseEnum):
    """Enumeration for Statistics"""
    INSTANT = "INSTANT"
    MEAN = "MEAN"
    MIN = "MIN"
    MAX = "MAX"
    TOTAL = "TOTAL"