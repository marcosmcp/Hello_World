import glob
import os
import h5py
import numpy as np

"""
Convert eye tracker hdf5 files to csv format
"""
def convertHdf5(path, sep = ","):
    for inputfile in glob.glob(os.path.join(path, '*.hdf5')):
        filename = os.path.basename(inputfile)
        print("Loading file {0}".format(filename))
        name = os.path.splitext(filename)[0]
        inputfile = "{0:s}{1:s}.hdf5".format(path, name)
        csvfile = "{0:s}{1:s}.csv".format(path, name)
        # to csv format
        np.savetxt(csvfile, h5py.File(inputfile)['data_collection']['condition_variables']['EXP_CV_1'], '%s', delimiter = sep)
        print("{0} file created".format(filename))

def main():
    ASL_PATH = "./ASL/hdf5/"
    SMIETG_PATH = "./smietg/HDF5/"
    SMIHED_PATH = "./smihed/HDF5/"
    TOBIIGLASSES_PATH = "./tobiiglasses/HDF5/"
    PATHS = [ASL_PATH, SMIETG_PATH, SMIHED_PATH, TOBIIGLASSES_PATH]
    for p in PATHS:
        print("-----converting files in {0} directory-----".format(p))
        convertHdf5(p)

if __name__ == '__main__':
    main()
