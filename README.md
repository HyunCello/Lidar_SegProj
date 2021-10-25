# Lidar Segmentation & Projection

## 사용된 데이터셋

[KITTI Object Detection Dataset](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark) training 7481장

## 작업 순서

- (ROS) 수정한 kitti_player를 켠다 

    `roslaunch kitti_player kitti_player.launch`

- (ROS) 수정한 depth_clustering을 켠다

    `rosrun depth_clustering show_objects_node --num_beams 64`

- 결과 파일을 각각 2_와 3_에 넣는다

    depth_clustering/src/visualization/0_result_seg.txt   ->   1_Projection/

    depth_clustering/src/clusters/0_seg_time.txt          ->   2_Time/

- 각각의 코드를 돌린다
