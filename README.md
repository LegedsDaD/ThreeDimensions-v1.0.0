# ThreeDimensions

ThreeDimensions is a programmable 3D modeling library for Python.

Version: `1.0.0`

The package is now Python-only. No C++ extension build is required at install or runtime.

## Installation
```bash
pip install threedimensions
```


```bash
pip install .
```

Viewer extras (optional):

```bash
pip install ".[viewer]"
```

## Quick Start

```python
import threedimensions as td

mesh = td.create_cube(1.0)
mesh.extrude(distance=0.2)
mesh.bevel(width=0.05)
mesh.subdivide(1)
mesh.save("model.obj")
```

## Python API Highlights

- Primitives: `create_cube`, `create_plane`, `create_grid`, `create_sphere`, `create_uv_sphere`, `create_icosphere`, `create_cylinder`, `create_cone`, `create_torus`
- Mesh editing: extrude, inset, bevel, bridge, fill, grid fill, subdivide, loop cut, knife, bisect, spin, screw, solidify, wireframe
- Transforms and deformation: move/rotate/scale, mirror, bend, twist, taper, stretch, shear, warp, symmetrize
- Sculpt and topology: brush workflow (`inflate`, `smooth`, `mask`, etc.), `laplacian_smooth`, remesh, decimate, weld
- Curves: `BezierCurve`, `NURBSCurve`, `lathe`, curve-to-mesh conversion
- Procedural nodes: `NodeGraph`
- Viewer: `td.viewer(mesh)` or `with td.viewer() as scene: ...`

## Architecture

- `python/threedimensions/`: full implementation and public API
- `examples/`: sample modeling scripts and exported meshes

## License

MIT
