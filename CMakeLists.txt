cmake_minimum_required(VERSION 3.24)
project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

# Force release build.
if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

find_package(Python COMPONENTS Interpreter Development.Module Development.SABIModule REQUIRED)
message(STATUS "Python interpreter: ${Python_EXECUTABLE}")

# Detect the installed dspsim package and import it into CMake
execute_process(
  COMMAND "${Python_EXECUTABLE}" -m dspsim.framework --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE dspsim_ROOT)
find_package(dspsim REQUIRED)

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

# Set the installation directory for the dspsim library.
set(DSPSIM_LIBRARY_INSTALL_DIR dspsim/library)
# Generate and build the library module.
dspsim_add_module(_library ${CMAKE_SOURCE_DIR}/pyproject.toml ${DSPSIM_LIBRARY_INSTALL_DIR})
