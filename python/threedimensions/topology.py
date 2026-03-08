from __future__ import annotations

from .mesh import Mesh


def laplacian_smooth(mesh: Mesh, iterations: int = 1, strength: float = 0.5):
    """Laplacian smoothing in pure Python."""
    for _ in range(max(1, int(iterations))):
        mesh.sculpt_filter("smooth", strength=float(strength))
    return mesh
