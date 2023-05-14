
import cv2

from dlclive import DLCLive, Processor

LIVE_VIDEO = 0
PRE_RECORDED = 1

MODE = LIVE_VIDEO

MODEL_PATH = 'DLC_Msc_resnet_101_iteration-5_shuffle-1'
MP4_FILE = "I:/hs503/code/branches/video/Light_Normal/trial2/Trial2.mp4"

cap = None

dlc_proc = Processor()
dlc_live = DLCLive(MODEL_PATH, processor=dlc_proc)
image = cv2.imread('load.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dlc_live.init_inference(gray_image)
    
def Trail():
	if MODE == LIVE_VIDEO :
		cap = cv2.VideoCapture(0)
	else:
		cap = cv2.VideoCapture(MP4_FILE)

	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))

	# ret, frame = cap.read()
	# dlc_live.init_inference(frame)

	while(cap.isOpened()):
		ret, frame = cap.read()

		if ret == True:
			pose = dlc_live.get_pose(frame)
			for indx in pose:
				frame = cv2.circle(frame, (indx[0],indx[1]), radius=2, color=(0, 0, 255), thickness=-1)

			#out.write(frame)
			cv2.imshow('frame',frame)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

    
def SegmentFrames(frame):
	print("start_mode")
	pose = dlc_live.get_pose(frame)
	return pose

if __name__ == '__main__':
    Trail()