project(Test_DynRes)

set(exec_src
    src/main.cpp)

set(libs
	LIB_DynRes
    dl)

include_directories(${CMAKE_SOURCE_DIR}/static/DynRes
    ${CMAKE_SOURCE_DIR}/tests/DynResDLL/src)

add_executable(${PROJECT_NAME} ${exec_src})
set_target_properties(${PROJECT_NAME}
	PROPERTIES OUTPUT_NAME testDynRes)
target_link_libraries(${PROJECT_NAME} ${libs})
