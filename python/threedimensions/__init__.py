"""
ThreeDimensions v1.1.1
Pure-Python 3D modeling engine.
"""

__version__ = "1.1.1"

from .mesh import (
    Mesh,
    TransformOptions,
    Vector3,
    create_cone,
    create_cube,
    create_cylinder,
    create_grid,
    create_icosphere,
    create_plane,
    create_sphere,
    create_torus,
    create_uv_sphere,
)
from .curves import BezierCurve, NURBSCurve, lathe
from .modifiers import ModifierStack, apply_array, apply_mirror, apply_subdivision, apply_weld
from .nodes import NodeGraph
from .sculpt import Sculpt
from .scene import Scene
from .topology import laplacian_smooth
from .viewer import viewer

CORE_MODE = "Python"

__all__ = [
    "__version__",
    "CORE_MODE",
    "Vector3",
    "TransformOptions",
    "Mesh",
    "create_cube",
    "create_sphere",
    "create_uv_sphere",
    "create_icosphere",
    "create_cylinder",
    "create_cone",
    "create_torus",
    "create_plane",
    "create_grid",
    "BezierCurve",
    "NURBSCurve",
    "lathe",
    "ModifierStack",
    "apply_subdivision",
    "apply_mirror",
    "apply_array",
    "apply_weld",
    "laplacian_smooth",
    "Sculpt",
    "Scene",
    "NodeGraph",
    "viewer",
]
