cmake_minimum_required(VERSION 3.1)
project(SharedResouceLibrary)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED 11)

add_subdirectory(static/DynRes)

add_subdirectory(tests/DynRes)
add_subdirectory(tests/DynResDLL)

enable_testing()

add_test(NAME test1 
	 COMMAND Test_DynRes ${CMAKE_BINARY_DIR}/tests/DynResDLL/libCRes.so)