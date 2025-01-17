"""
`basin3d.core.types`
************************

.. currentmodule:: basin3d.core.synthesis

:platform: Unix, Mac
:synopsis: BASIN-3D ``DataSource`` type classes
:module author: Val Hendrix <vhendrix@lbl.gov>
:module author: Danielle Svehla Christianson <dschristianson@lbl.gov>

.. contents:: Contents
    :local:
    :backlinks: top

"""


class SpatialSamplingShapes(object):
    """
    Spatial sampling shape describing a spatial sampling feature

    Controlled CV list as defined by OGC Observation & Measurement GM_Shape.
    """

    #: The shape of a spatially extensive sampling feature which provides a complete sampling domain.
    SHAPE_SOLID = "SOLID"

    #: The shape of a spatially extensive sampling feature which provides a complete sampling domain.
    SHAPE_SURFACE = "SURFACE"

    #: The shape of a spatially extensive sampling feature which provides a complete sampling domain.
    SHAPE_CURVE = "CURVE"

    #: The shape of a spatially extensive sampling feature which provides a complete sampling domain.
    SHAPE_POINT = "POINT"


class SamplingMedium:
    """
    Types of sampling mediums for Observed Properties
    """

    SOLID_PHASE = "SOLID PHASE"
    WATER = "WATER"
    GAS = "GAS"
    OTHER = "OTHER"
    NOT_APPLICABLE = "N/A"
    SAMPLING_MEDIUMS = [WATER, GAS, SOLID_PHASE, OTHER, NOT_APPLICABLE]


