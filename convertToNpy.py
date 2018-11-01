import numpy as np
import scipy.io
import os

PATH = 'matFeatures'


# Process sober dataset
files = [];
filenames = [];
outPath = "LBPTOP_npy/Sober"

for i in os.listdir(PATH+'/Sober'):
    print (i);
    ff = PATH+'/Sober'+'/'+i;
    
    x = scipy.io.loadmat(ff);

    x = x.items()[0][1];
    x = x.ravel()
    np.save(outPath+'/'+i[:-4]+'.npy', x)



# Process drunk dataset
files = [];
filenames = [];
outPath = "LBPTOP_npy/Drunk"

for i in os.listdir(PATH+'/Drunk'):
    print (i);
    ff = PATH+'/Drunk'+'/'+i;
    
    x = scipy.io.loadmat(ff);

    x = x.items()[0][1];
    x = x.ravel()
    np.save(outPath+'/'+i[:-4]+'.npy', x)
