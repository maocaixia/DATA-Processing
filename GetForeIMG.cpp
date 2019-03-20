#include "opencv2/opencv.hpp"
#include "opencv2/video/background_segm.hpp"
 
using namespace cv;
using namespace std;
int main()
{
	VideoCapture capture;
	capture.open(0);
 
	int frameNum = 1;
	Mat frame, mask, thresholdImage, output;
	if (!capture.isOpened())
		cout << "fail to open!" << endl;
 
	capture >> frame;
	Ptr<BackgroundSubtractorMOG2> bgsubtractor = createBackgroundSubtractorMOG2();
	bgsubtractor->setVarThreshold(20);
 
	while (true) {
		capture >> frame;
		++frameNum;
		//bgSubtractor(frame, mask, 0.001);
		bgsubtractor->apply(frame, mask, -1);
		imshow("mask", mask);
		waitKey(10);
	}
 
	return 0;
}
