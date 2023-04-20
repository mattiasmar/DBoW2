cmake_minimum_required(VERSION 3.15)
project(dbow2 CXX)

find_package(OpenCV REQUIRED)

set(HDRS
  include/DBoW2/BowVector.h
  include/DBoW2/FBrief.h 
  include/DBoW2/QueryResults.h  
  include/DBoW2/TemplatedDatabase.h  
  include/DBoW2/FORB.h 
  include/DBoW2/DBoW2.h             
  include/DBoW2/FClass.h         
  include/DBoW2/FeatureVector.h 
  include/DBoW2/ScoringObject.h      
  include/DBoW2/TemplatedVocabulary.h)
  
set(SRCS 
  src/BowVector.cpp     src/FBrief.cpp        src/FORB.cpp
  src/FeatureVector.cpp src/QueryResults.cpp  src/ScoringObject.cpp)

  
add_library(dbow2 ${SRCS})

target_include_directories(dbow2 PUBLIC include)


target_link_libraries(dbow2 opencv::opencv)

set_target_properties(dbow2 PROPERTIES    PUBLIC_HEADER "${HDRS}")
install(TARGETS dbow2)