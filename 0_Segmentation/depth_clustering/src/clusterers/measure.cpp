#include <algorithm>
#include <chrono>
#include <ctime>
#include <limits>
#include <string>
#include <vector>

#include "ros/ros.h"
#include "ros_bridge/cloud_odom_ros_subscriber.h"
#include "std_msgs/String.h"
#include <fstream>
#include <iostream>
#include <sstream>

void Measure_save(uint64_t time_measure_1) {
  std::string str_n = to_string(time_measure_1);
  int seq = ReturnSeq();
  std::string str_seq = to_string(seq);

  std::string result = str_seq + " " + str_n;
  // std::string result = str_cen_x + " " + str_cen_y + " " + str_cen_z + " " +
  // str_sca_x + " " + str_sca_y + " " + str_sca_z;

  // std::cout << result << std::endl;
  // std::cout << str_x << std::endl;    //지금은 읽은 문자열 바로 출력.
  std::ofstream out(
      "/home/yh/catkin_ws/src/depth_clustering/clusaters/test.txt",
      std::ios::app);
  if (out.is_open()) {
    out << result << std::endl;
  }
  out.close();
  //파일 열기
  // 1. istream의 getline.
  /*
  char tmp[256];
  readFile.getline(tmp, 256);
  cout << tmp << endl;    //지금은 읽은 문자열 바로 출력.
  */
  // 2. std::getline.
  // fout << str_x << str_y << str_z << "\n";
  // getline(readFile, str);
  //파일 닫아줍니다.
}

// YH