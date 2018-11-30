import os
import subprocess

'''
This stage extract features of video using OpenFace library
videoFeatures takes directories of video folder and output folder
'''
# def videofeatures(input_folder_video, output_folder):
#     OPENFACE_LOCATION = '/home/lasii/OpenFace/build/bin/FeatureExtraction'
#     files = []
#     for f in os.listdir(input_folder_video):
#         files.append(input_folder_video+'/'+f)
#
#     c1 = '"{OPENFACE_LOCATION}" {videos} -out_dir ' + output_folder + ' -2Dfp -3Dfp -pose -aus -gaze'
#     videopaths = ""
#     for f in range(0, len(files)):
#         videopaths += '-f "' + files[f] + '" '
#
#     com1 = c1.format(OPENFACE_LOCATION=OPENFACE_LOCATION, videos=videopaths)
#     subprocess.call(com1, shell=True)



def videofeatures(input_folder_video, output_folder):
    OPENFACE_LOCATION = '/home/lasii/OpenFace/build/bin/FeatureExtraction'
    for f in os.listdir(input_folder_video):
        # files.append(input_folder_video+'/'+f)

        c1 = '"'+OPENFACE_LOCATION+'"'+' -f '+ '"'+input_folder_video+'/'+f+'"' +' -out_dir "' + output_folder + '" -2Dfp -pdmparams -3Dfp -pose -aus -gaze'
        print (c1)
        subprocess.call(c1, shell=True)
    # videopaths = ""
    # for f in range(0, len(files)):
        # videopaths += '-f "' + files[f] + '" '

    # com1 = c1.format(OPENFACE_LOCATION=OPENFACE_LOCATION, videos=videopaths)

# Sample run
input_folder_video = './10sec/Drunk'
output_folder = './Features/10sec/Drunk'
videofeatures(input_folder_video,output_folder)

input_folder_video = './10sec/Sober'
output_folder = './Features/10sec/Drunk'
videofeatures(input_folder_video,output_folder)

input_folder_video = './15sec/Drunk'
output_folder = './Features/15sec/Drunk'
videofeatures(input_folder_video,output_folder)

input_folder_video = './15sec/Sober'
output_folder = './Features/15sec/Drunk'
videofeatures(input_folder_video,output_folder)
