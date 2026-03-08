cmake_minimum_required(VERSION 3.15)

project(ThreeDimensionsCore LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

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

# Collect all C++ sources
file(GLOB_RECURSE CORE_SOURCES
    cpp_core/*.cpp
)

# Build Python module
if(THREEDIMENSIONS_BUILD_PYBIND)

  pybind11_add_module(_threedimensions_core ${CORE_SOURCES})

  target_include_directories(
    _threedimensions_core
    PRIVATE
      cpp_core
  )

  install(
    TARGETS _threedimensions_core
    LIBRARY DESTINATION threedimensions
    ARCHIVE DESTINATION threedimensions
    RUNTIME DESTINATION threedimensions
  )

endif()
