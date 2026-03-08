# ThreeDimensions Manual

Version: `1.1.1`

This manual reflects the current Python-only implementation in `python/threedimensions`.

## 1. Installation

```bash
pip install .
```

Optional viewer dependencies:

```bash
pip install ".[viewer]"
```

## 2. Top-Level API (`import threedimensions as td`)

### 2.1 Constants

- `td.__version__`
- `td.CORE_MODE` (`"Python"`)

### 2.2 Types and Helpers

- `td.Vector3`
- `td.TransformOptions`
- `td.Mesh`
- `td.BezierCurve`
- `td.NURBSCurve`
- `td.ModifierStack`
- `td.Sculpt`
- `td.Scene`
- `td.NodeGraph`

### 2.3 Functional Helpers

- `td.apply_subdivision(mesh, levels=1)`
- `td.apply_mirror(mesh, axis="X")`
- `td.apply_array(mesh, count=2, offset=(1.0, 0.0, 0.0))`
- `td.apply_weld(mesh, tolerance=1e-6)`
- `td.laplacian_smooth(mesh, iterations=1, strength=0.5)`

### 2.4 Primitive Constructors

- `td.create_cube(size=1.0)`
- `td.create_plane(size=2.0, subdivisions=1)`
- `td.create_grid(size=2.0, x_subdivisions=10, y_subdivisions=10)`
- `td.create_sphere(radius=1.0, segments=32, rings=16)`
- `td.create_uv_sphere(radius=1.0, segments=32, rings=16)`
- `td.create_icosphere(radius=1.0, subdivisions=1)`
- `td.create_cylinder(radius=1.0, height=2.0, segments=16)`
- `td.create_cone(radius=1.0, height=2.0, segments=16)`
- `td.create_torus(main_radius=1.0, tube_radius=0.4, main_segments=32, tube_segments=16)`

## 3. Mesh Methods

### 3.1 Core

- `add_vertex(position)`
- `add_face(indices)`
- `calculate_normals()`
- `clone()`
- `clear()`
- `save(filepath)`

### 3.2 Transform

- `move(delta, options=None)` / `translate(...)`
- `rotate(angle, axis="Z", options=None)` / `rotate_x/y/z(angle)`
- `scale(...)`
- `mirror(axis="X")`
- `mirror_transform(axis="X")`

### 3.3 Selection

- `select_mode(mode)`
- `select_vertex(index, extend=False)`
- `select_edge((a, b), extend=False)`
- `select_face(index, extend=False)`
- `select_loop(edge)`
- `select_ring(edge)`
- `box_select(min_corner, max_corner, mode=None)`
- `circle_select(center, radius, mode="VERTEX")`
- `lasso_select(points, mode="VERTEX")`
- `select_similar(by="face_size", value=None, tolerance=0.1)`

### 3.4 Editing / Topology

- `extrude_face(face_index, distance=0.1)`
- `extrude(distance=0.1, face_indices=None)`
- `scale_face(face_index, scale=1.0)`
- `translate_face(face_index, delta)`
- `inset_faces(amount=0.05)`
- `bevel(width=0.05, segments=1)`
- `bridge_edge_loops(loop_a, loop_b)`
- `fill(vertices=None)`
- `grid_fill(boundary, rows=2, cols=2)`
- `subdivide(levels=1)`
- `loop_cut(cuts=1)`
- `knife(start, end)`
- `bisect(plane_point, plane_normal, clear_inner=False, clear_outer=False)`
- `spin(steps=8, angle=math.tau, axis="Y")`
- `screw(steps=16, angle=math.tau, height=1.0, axis="Y")`
- `solidify(thickness=0.05)`
- `wireframe(thickness=0.02)`
- `join(other, offset_x=0.0, offset_y=0.0, offset_z=0.0)`
- `join_fast(...)`
- `merge_duplicate_vertices(tolerance=1e-6)`

### 3.5 Deformation

- `bend(factor=0.5, axis="X")`
- `twist(angle=math.pi * 0.5, axis="Y")`
- `taper(factor=0.5, axis="Y")`
- `stretch(factor=1.1, axis="Y")`
- `shear(factor=0.2, axis="X", by="Y")`
- `warp(center=(0.0, 0.0, 0.0), strength=0.2, radius=1.0)`
- `symmetrize(axis="X", direction="POSITIVE")`

### 3.6 Sculpt / Remesh / UV / Retopo

- `brush(...)`, `pose_brush(...)`, `cloth_brush(...)`, `mask_brush(...)`
- `dyntopo(detail_size=0.05, subdivide_collapse=0.5)`
- `sculpt_filter(filter_type="smooth", strength=0.25, radius=None)`
- `voxel_remesh(voxel_size=0.1)`
- `quad_remesh(target_faces=2000)`
- `decimate(ratio=0.5)`
- `shade_smooth()`, `shade_flat()`, `auto_smooth(angle=...)`
- `mark_seam(edge)`
- `unwrap(method="angle_based", uv_layer=None)`
- `smart_uv_project(uv_layer=None)`
- `project_from_view(axis="Z", uv_layer=None)`
- `shrinkwrap(target, strength=1.0, max_samples=20000)`
- `poly_build(points, faces)`
- `relax_topology(iterations=1, strength=0.5)`
- `multires_subdivide(levels=1)`
- `face_set(face_indices, set_id)`
- `box_mask(min_corner, max_corner, value=1.0)`
- `lasso_mask(points, value=1.0)`
- `clear_mask()`

### 3.7 Modifier Stack on Mesh

- `add_modifier(modifier, **params)`
- `apply_modifiers()`
- `array(count=2, offset=(1.0, 0.0, 0.0))`
- `boolean(other, operation="UNION")`

## 4. Curves

- `td.BezierCurve(control_points)`
- `BezierCurve.evaluate(t)`
- `BezierCurve.sample(segments=32)`
- `BezierCurve.to_mesh(radius=0.05, radial_segments=12, segments=64)`
- `BezierCurve.extrude(distance=0.1)`
- `BezierCurve.bevel(radius=0.05)`
- `td.NURBSCurve(control_points, degree=3)`
- `NURBSCurve.sample(segments=32)`
- `NURBSCurve.to_mesh(...)`
- `td.lathe(profile, steps=32)`

## 5. Procedural Nodes

- Create graph with `td.NodeGraph()`
- Add nodes with `graph.node(type, **params)`
- Link with `graph.connect(a, b)`
- Evaluate with `graph.evaluate()`

Supported operations include primitive creation and mesh transforms/editing (`Subdivision`, `Extrude`, `Bevel`, `Boolean`, `Mirror`, `Solidify`, `Decimate`, `Brush`, etc.).

## 6. Viewer

Blocking preview:

```python
td.viewer(mesh)
```

Session style:

```python
with td.viewer() as session:
    session.update(mesh)
    session.run()
```
