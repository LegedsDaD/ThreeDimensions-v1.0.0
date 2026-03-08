#include "Bevel.h"
#include "../math/Vector3.h"

using ThreeDimensions::Math::Vector3;

void Bevel::apply(HalfEdge* he, float width)
{
    HalfEdge* twin = he->twin;

    Vector3 dir = he->vertex->position - twin->vertex->position;
    Vector3 offset = dir * (width * 0.5f);

    he->vertex->position += offset;
    twin->vertex->position -= offset;
}
