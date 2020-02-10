# 6.867-Final-Project

We present HoopNet - a new method to count the number of shots made in a clip of a basketball game. We present a model that first detects and draws a bounding box around the basketball hoop in a particular frame of a video clip by applying the Tiny-YOLOv3 architecture. We then feed the bounded box into a simple CNN that we built and experimented from scratch to classify whether or not a basketball shot is being made. We manually labeled our dataset, which was comprised of frames from 2019 NBA Finals Games 1 and 2, both taking place on the Toronto Raptors home court. Both hoop detection and shot classification perform with high accuracy on testing data from other Finals Games taking place on the Raptors home court. However, the combined pipeline does not generalize well to non-Finals games or to games that do not take place on the Raptors home court due to the lack of variety in our training data.

Please refer to HoopNet_Paper.pdf for more information on the project.
Yolov3 architecture: https://github.com/ultralytics/yolov3/wiki/Train-Custom-Data
