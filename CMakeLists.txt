cmake_minimum_required(VERSION 3.17)

project(Game)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/3rd)

# project
include_directories(${CMAKE_CURRENT_LIST_DIR}/include)
aux_source_directory(${CMAKE_CURRENT_LIST_DIR}/src PROJECT_SRC)

if (ANDROID)
    set(ANDROID_STL c++_shared)

    include_directories(${ANDROID_NDK}/sources/android/native_app_glue)

    add_library(
        ${PROJECT_NAME}Android
        SHARED
        ${PROJECT_SRC}
        platforms/android.cpp
        ${ANDROID_NDK}/sources/android/native_app_glue/android_native_app_glue.c
    )

    set(CMAKE_SHARED_LINKER_FLAGS
        "${CMAKE_SHARED_LINKER_FLAGS} -u ANativeActivity_onCreate"
    )
  
    target_link_libraries(${PROJECT_NAME}Android PRIVATE
        android
        EGL
        GLESv3
        log
        3rdparty
    )
else()
    add_executable(
        ${PROJECT_NAME}
        ${PROJECT_SRC}
        platforms/standalone.cpp
    )

    target_link_libraries(
        ${PROJECT_NAME}
        3rdparty
    )

    # Checks if OSX and links appropriate frameworks (Only required on MacOS)
    if (APPLE)
        target_link_libraries(${PROJECT_NAME} "-framework IOKit")
        target_link_libraries(${PROJECT_NAME} "-framework Cocoa")
        target_link_libraries(${PROJECT_NAME} "-framework OpenGL")
    elseif(EMSCRIPTEN)
        # -fexceptions is required by pocketpy
        set(EMCC_LINKER_FLAGS "-s USE_GLFW=3 --preload-file=workdir -fexceptions --allow-memory-growth -s TOTAL_MEMORY=512MB -sASYNCIFY -sASSERTIONS")
        set(CMAKE_EXECUTABLE_SUFFIX ".html")
        set_target_properties(${PROJECT_NAME} PROPERTIES LINK_FLAGS ${EMCC_LINKER_FLAGS})
    elseif(WIN32)
        if(CMAKE_BUILD_TYPE STREQUAL "Release")
            set_target_properties(${PROJECT_NAME} PROPERTIES LINK_FLAGS "/SUBSYSTEM:WINDOWS /ENTRY:mainCRTStartup")
        endif()
    endif()
endif()