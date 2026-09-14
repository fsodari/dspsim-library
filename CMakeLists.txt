cmake_minimum_required(VERSION 3.24)
project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

# Force release build.
if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Simplest way of exporting symbols for windows.
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

# Set warning level
if (MSVC)
    # warning level 4
    add_compile_options(/W2)
else()
    # additional warnings
    add_compile_options(-Wall -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-maybe-uninitialized)
endif()

# Find dspsim package
find_package(dspsim REQUIRED HINTS ${CMAKE_PREFIX_PATH}/dspsim/framework/cmake)

# # RPath
# # Set the RPATH to where dspsim/framework will be installed relative to this module.
# list(APPEND CMAKE_INSTALL_RPATH "$ORIGIN/../framework")
# set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

# Set project paths.
# set(DSPSIM_LIBRARY_PKG_DIR ${CMAKE_SOURCE_DIR}/src/dspsim/library)
# set(DSPSIM_LIBRARY_HDL_DIR ${CMAKE_SOURCE_DIR}/src/dspsim/library/hdl)
set(DSPSIM_LIBRARY_INSTALL_DIR dspsim/library)

# Generate and build the library module.
dspsim_add_module(_library ${CMAKE_SOURCE_DIR}/pyproject.toml ${DSPSIM_LIBRARY_INSTALL_DIR})
