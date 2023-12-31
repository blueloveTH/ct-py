cmake_minimum_required(VERSION 3.10)

project(3rdparty)

set(CMAKE_CXX_STANDARD 17)

aux_source_directory(imgui IMGUI_SRC)
aux_source_directory(rlImGui RLIMGUI_SRC)

option(CUSTOMIZE_BUILD "Customize build" ON)
option(SUPPORT_MODULE_RMODELS "" OFF)
option(SUPPORT_SSH_KEYBOARD_RPI "" OFF)
option(SUPPORT_GIF_RECORDING "" OFF)

option(SUPPORT_FILEFORMAT_DDS "" OFF)
option(SUPPORT_FILEFORMAT_HDR "" OFF)
option(SUPPORT_FILEFORMAT_QOI "" OFF)
option(SUPPORT_FILEFORMAT_FNT "" OFF)

option(SUPPORT_FILEFORMAT_OBJ "" OFF)
option(SUPPORT_FILEFORMAT_MTL "" OFF)
option(SUPPORT_FILEFORMAT_IQM "" OFF)
option(SUPPORT_FILEFORMAT_GLTF "" OFF)
option(SUPPORT_FILEFORMAT_VOX "" OFF)
option(SUPPORT_FILEFORMAT_M3D "" OFF)
option(SUPPORT_MESH_GENERATION "" OFF)

option(SUPPORT_FILEFORMAT_XM "" OFF)
option(SUPPORT_FILEFORMAT_MOD "" OFF)
option(SUPPORT_FILEFORMAT_QOA "" OFF)

option(SUPPORT_STANDARD_FILEIO "" OFF)
add_subdirectory(raylib)

# pocketpy
option(PK_USE_BOX2D "Use Box2D" ON)
option(PK_USE_CJSON "Use cJSON" OFF)
add_subdirectory(pocketpy)

add_library(
    ${PROJECT_NAME}
    STATIC
    ${IMGUI_SRC}
    ${RLIMGUI_SRC}
)

target_link_libraries(
    ${PROJECT_NAME}
    raylib
    pocketpy
)

target_include_directories(
    ${PROJECT_NAME}
    PUBLIC
    imgui
    rlImGui
    raylib/src
    pocketpy/include
)