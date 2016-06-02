import cPickle
import gzip
import os
import numpy as np
pwd = os.path.join(os.path.dirname(__file__))

def load_disfa():
    dat = cPickle.load(gzip.open(pwd+'/data/disfa.pklz','rb'))
    X = np.vstack(dat['X'])
    y = np.vstack(dat['y'])
    S = np.hstack([[ii]*jj.shape[0] for ii,jj in zip(dat['S'],dat['y'])])
    return X,y,S

def load_fera():pass
def load_pain():pass