cmake_minimum_required(VERSION 4.0)
project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find dspsim package
find_package(dspsim REQUIRED)
message(STATUS "Found dspsim: ${dspsim_DIR}")

# Generate and build the library module.
dspsim_add_module(_library ${CMAKE_SOURCE_DIR}/pyproject.toml ${SKBUILD_PROJECT_NAME})
