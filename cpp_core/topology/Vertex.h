#pragma once
#include "../math/Vector3.h"

struct Vertex {
    Vector3 position;

    Vertex(const Vector3& pos) : position(pos) {}
};
