cmake_minimum_required(VERSION 3.15)

project(ThreeDimensionsCore LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

option(THREEDIMENSIONS_BUILD_PYBIND "Build the pybind11 C++ extension" ON)

# Find pybind11
find_package(pybind11 CONFIG QUIET)

if(NOT pybind11_FOUND)
    include(FetchContent)
    message(STATUS "pybind11 not found, downloading...")
    FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.13.6
    )
    FetchContent_MakeAvailable(pybind11)
endif()

# Core source files (ONLY stable ones)
set(CORE_SOURCES
    cpp_core/mesh/Mesh.cpp
    cpp_core/curves/BezierCurve.cpp
    cpp_core/curves/CurveMeshing.cpp
    cpp_core/geometry/Primitives.cpp
    cpp_core/modifiers/ModifierStack.cpp
    cpp_core/modifiers/Modifiers.cpp
    cpp_core/modifiers/SubdivisionModifier.cpp
    cpp_core/operations/EdgeLoop.cpp
    cpp_core/bindings.cpp
)

# Build Python module
if(THREEDIMENSIONS_BUILD_PYBIND)

    pybind11_add_module(_threedimensions_core ${CORE_SOURCES})

    target_include_directories(
        _threedimensions_core
        PRIVATE
            cpp_core
    )

    target_compile_features(_threedimensions_core PRIVATE cxx_std_20)

    install(
        TARGETS _threedimensions_core
        LIBRARY DESTINATION threedimensions
        ARCHIVE DESTINATION threedimensions
        RUNTIME DESTINATION threedimensions
    )

endif()
