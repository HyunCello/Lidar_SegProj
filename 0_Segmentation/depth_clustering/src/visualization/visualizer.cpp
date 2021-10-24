// Copyright (C) 2020  I. Bogoslavskyi, C. Stachniss
//
// GNU-GPL licence that follows one of libQGLViewer.

#include "./visualizer.h"

#include <algorithm>
#include <chrono>
#include <ctime>
#include <limits>
#include <string>
#include <vector>

#include <iostream>
#include <fstream>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "ros_bridge/cloud_odom_ros_subscriber.h" 


namespace depth_clustering {

using std::array;
using std::string;
using std::to_string;
using std::vector;

using std::lock_guard;
using std::map;
using std::mutex;
using std::string;
using std::thread;
using std::unordered_map;
using std::vector;
using std::ofstream;

static vector<array<int, 3>> COLORS;
int n = 0;
float cen_x, cen_y, cen_z, sca_x, sca_y, sca_z; 


Visualizer::Visualizer(QWidget* parent)
    : QGLViewer(parent), AbstractClient<Cloud>(), _updated{false} {
  _cloud_obj_storer.SetUpdateListener(this);
}

void Measure_save(uint64_t time_measure_1){                

    std::string str_n = std::to_string(time_measure_1);
    int seq = ReturnSeq();
    std::string str_seq = std::to_string(seq);

    std::string result = str_seq + " " + str_n;
    // std::string result = str_cen_x + " " + str_cen_y + " " + str_cen_z + " " + str_sca_x + " " + str_sca_y + " " + str_sca_z;

    // std::cout << result << std::endl;
    // std::cout << str_x << std::endl;    //지금은 읽은 문자열 바로 출력.
    std::ofstream out("/home/yh/catkin_ws/src/depth_clustering/clusaters/test.txt",std::ios::app);
    if (out.is_open()) {
      out << result << std::endl;
    }
    out.close(); 
     //파일 열기
                //1. istream의 getline.
                /*
                char tmp[256];
                readFile.getline(tmp, 256);
                cout << tmp << endl;    //지금은 읽은 문자열 바로 출력.
                */
                //2. std::getline.
                // fout << str_x << str_y << str_z << "\n";
                // getline(readFile, str);
                         //파일 닫아줍니다.

      
}

void Save(){                
    std::string str_cen_x = to_string(cen_x);
    std::string str_cen_y = to_string(cen_y);
    std::string str_cen_z = to_string(cen_z);
    std::string str_sca_x = to_string(sca_x);
    std::string str_sca_y = to_string(sca_y);
    std::string str_sca_z = to_string(sca_z);

    std::string str_n = to_string(n);
    int seq = ReturnSeq();
    std::string str_seq = to_string(seq);

    std::string result = str_seq + " " + str_cen_x + " " + str_cen_y + " " + str_cen_z + " " + str_sca_x + " " + str_sca_y + " " + str_sca_z;
    // std::string result = str_cen_x + " " + str_cen_y + " " + str_cen_z + " " + str_sca_x + " " + str_sca_y + " " + str_sca_z;

    // std::cout << result << std::endl;
    // std::cout << str_x << std::endl;    //지금은 읽은 문자열 바로 출력.
    std::ofstream out("/home/yh/catkin_ws/src/depth_clustering/src/visualization/test.txt",std::ios::app);
    if (out.is_open()) {
      out << result << std::endl;
    }
    out.close(); 
     //파일 열기
                //1. istream의 getline.
                /*
                char tmp[256];
                readFile.getline(tmp, 256);
                cout << tmp << endl;    //지금은 읽은 문자열 바로 출력.
                */
                //2. std::getline.
                // fout << str_x << str_y << str_z << "\n";
                // getline(readFile, str);
                         //파일 닫아줍니다.

      
}

void Visualizer::draw() {
  lock_guard<mutex> guard(_cloud_mutex);
  DrawCloud(_cloud);
  for (const auto& kv : _cloud_obj_storer.object_clouds()) {
    const auto& cluster = kv.second;
    Eigen::Vector3f center = Eigen::Vector3f::Zero();
    Eigen::Vector3f extent = Eigen::Vector3f::Zero();
    Eigen::Vector3f max_point(std::numeric_limits<float>::lowest(),
                              std::numeric_limits<float>::lowest(),
                              std::numeric_limits<float>::lowest());
    Eigen::Vector3f min_point(std::numeric_limits<float>::max(),
                              std::numeric_limits<float>::max(),
                              std::numeric_limits<float>::max());
    for (const auto& point : cluster.points()) {
      center = center + point.AsEigenVector();
      min_point << std::min(min_point.x(), point.x()),
          std::min(min_point.y(), point.y()),
          std::min(min_point.z(), point.z());
      max_point << std::max(max_point.x(), point.x()),
          std::max(max_point.y(), point.y()),
          std::max(max_point.z(), point.z());
    }
    center /= cluster.size();
    if (min_point.x() < max_point.x()) {
      extent = max_point - min_point;
    }
    if (center.x() > 0 && center.z() > -1.4 && center.y() < 6 && center.y() > -4){
      DrawCube(center, extent);
      cen_x = center.x();
      cen_y = center.y();
      cen_z = center.z();
      sca_x = extent.x();
      sca_y = extent.y();
      sca_z = extent.z();

      Save();
      // std::cout << center.x()<<", " << center.y()<<", " << center.z() << std::endl;              ////////////////////////////////////////////////
      // std::cout << extent.x()<<", " << extent.y()<<", " << extent.z() << std::endl << std::endl; ////////////////////////////////////////////////

    }
    // fout.close(); 
  }
}

void Visualizer::init() {
  setSceneRadius(100.0);
  camera()->showEntireScene();
  glDisable(GL_LIGHTING);
}

void Visualizer::DrawCloud(const Cloud& cloud) {
  glPushMatrix();
  glBegin(GL_POINTS);
  glColor3f(1.0f, 1.0f, 1.0f);
  for (const auto& point : cloud.points()) {
    glVertex3f(point.x(), point.y(), point.z());
  }
  glEnd();
  glPopMatrix();
}

void Visualizer::DrawCube(const Eigen::Vector3f& center,
                          const Eigen::Vector3f& scale) {
  glPushMatrix();
  glTranslatef(center.x(), center.y(), center.z());
  glScalef(scale.x(), scale.y(), scale.z());
  float volume = scale.x() * scale.y() * scale.z();
  if (volume < 30.0f && scale.x() < 6 && scale.y() < 6 && scale.z() < 6) {
    glColor3f(0.0f, 0.2f, 0.9f);
    glLineWidth(4.0f);
  } else {
    glColor3f(0.3f, 0.3f, 0.3f);
    glLineWidth(1.0f);
  }
  glBegin(GL_LINE_STRIP);

  // Bottom of Box
  glVertex3f(-0.5, -0.5, -0.5);
  glVertex3f(-0.5, -0.5, 0.5);
  glVertex3f(0.5, -0.5, 0.5);
  glVertex3f(0.5, -0.5, -0.5);
  glVertex3f(-0.5, -0.5, -0.5);

  // Top of Box
  glVertex3f(-0.5, 0.5, -0.5);
  glVertex3f(-0.5, 0.5, 0.5);
  glVertex3f(0.5, 0.5, 0.5);
  glVertex3f(0.5, 0.5, -0.5);
  glVertex3f(-0.5, 0.5, -0.5);

  glEnd();

  glBegin(GL_LINES);
  // For the Sides of the Box

  glVertex3f(-0.5, 0.5, -0.5);
  glVertex3f(-0.5, -0.5, -0.5);

  glVertex3f(-0.5, -0.5, 0.5);
  glVertex3f(-0.5, 0.5, 0.5);

  glVertex3f(0.5, -0.5, 0.5);
  glVertex3f(0.5, 0.5, 0.5);

  glVertex3f(0.5, -0.5, -0.5);
  glVertex3f(0.5, 0.5, -0.5);

  glEnd();
  glPopMatrix();
}

Visualizer::~Visualizer() {}

void Visualizer::OnNewObjectReceived(const Cloud& cloud, const int) {
  lock_guard<mutex> guard(_cloud_mutex);
  _cloud = cloud;
}

void Visualizer::onUpdate() { this->update(); }

unordered_map<uint16_t, Cloud> ObjectPtrStorer::object_clouds() const {
  lock_guard<mutex> guard(_cluster_mutex);
  return _obj_clouds;
}

void ObjectPtrStorer::OnNewObjectReceived(
    const unordered_map<uint16_t, Cloud>& clouds, const int) {
  lock_guard<mutex> guard(_cluster_mutex);
  _obj_clouds = clouds;

  if (_update_listener) {
    _update_listener->onUpdate();
  }
}

}  // namespace depth_clustering
