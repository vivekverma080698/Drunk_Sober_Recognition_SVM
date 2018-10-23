import csv
import numpy
import pandas
import os
import subprocess

#input_folder = '5_face_alignment/Drunk_NewDataset_Output_5_full'

# def processCSV_file(input_folder):
# 	for f in os.listdir(input_folder):
# 		filePath = os.path.join(input_folder, f)
# 		if (f[-4:] == '.csv'):
# 			print(filePath)
# 			do_further_processing(filePath);
# 			break
# def do_further_processing(filePath):
# 	try:
# 		with open(filePath) as csvfile:
# 			reader = pandas.read_csv(csvfile)
# 			landmarkX = ' eye_lmk_x_'
# 			landmarkY = ' eye_lmk_y_'
# 			frame = []
# 			for index, row in reader.iterrows():
# 				listx = []
# 				listy = []
# 				for i in range(56):
# 					landmarkx = landmarkX + str(i) 
# 					landmarky = landmarkY + str(i) 
# 					valuex = row[landmarkx].tolist();
# 					listx.append(valuex)
# 					valuey = row[landmarky].tolist();
# 					listy.append(valuey)
# 				listx = listx + listy
# 				frame.append(listx)
# 			print(frame)
# 	except:
# 		print('File not Found ',filePath)
# processCSV_file(input_folder)

OPENFACE_LOCATION = '/home/black/OpenFace-master/build/bin/FeatureExtraction'

input_folder = '/home/black/pipeline_4_July/5secin'
output_folder = '/home/black/pipeline_4_July/5secout'
files = []
for f in os.listdir('5secin'):
 	files.append(input_folder+'/'+f)

c1 = '"{OPENFACE_LOCATION}" {videos} -out_dir '+ output_folder +' -2Dfp -3Dfp -pose -aus -gaze';
videoPaths = "";
for f in range(0,len(files)):
    videoPaths+='-f "'+files[f]+'" ';

com1 = c1.format(OPENFACE_LOCATION = OPENFACE_LOCATION , videos= videoPaths);
print(com1)
subprocess.call(com1, shell=True)
