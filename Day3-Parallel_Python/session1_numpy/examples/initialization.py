#################################################################
#   Example:  Numpy array initialization
#
#             There are various ways to initialize a Numpy array.
#             Several examples are shown below.

import numpy as np

#Array dimensions for use later
nx = 10
ny = 20


#1-D array, 4-byte real, using np.zeros
# means that values are initialized to zero
zarr = np.zeros(nx,dtype='float32')
print('zarr: ', zarr)
print(' ')

#1-D array, 8-byte real, using np.empty means that
# values are not initialized to anything
earr = np.empty(nx,dtype='float64')
print('earr: ', earr)
print(' ')

#2-d array, 4-byte integer, values set to zero
# Column major ordering (second index is fastest; like C/C++)
iarr2da = np.zeros((nx,ny),dtype='int32')
print('iarr2da: ', iarr2da)
print(' ')

#2-d array, 4-byte integer, values set to zero
#Row-major ordering (first index is fastest; like Fortran)
iarr2db = np.zeros((nx,ny),dtype='int32', order ='F')
print('iarr2db: ', iarr2db)
print(' ')


#1-d array, 4-byte real, values spaced  with integer spacing 
# in the range [istart,iend], with stepsize istep
# This is accomplished via np.arange
istart = 10
iend = 20
istep = 2
arrsp = np.arange(istart,iend,istep,dtype='float32')
print('arrsp: ', arrsp)
print(' ')

#1-d array, 8-byte real, values spaced with non-integer spacing
# in the range [istart,iend], with stepsize = (iend-istart)/nstep
istart = 100
iend = 200
nstep = 200
arrsp2 = np.linspace(istart,iend,nstep,dtype='float64')
print('arrsp2: ', arrsp2)
print(' ')

array_names = ['zarr', 'earr', 'iarr2da', 'iarr2db','arrsp', 'arrsp2']
arrays = [zarr,earr,iarr2da,iarr2db, arrsp, arrsp2]

for i,o in enumerate(arrays):
    ndim = o.ndim
    dtype = o.dtype
    isize = o.itemsize
    ssp = o.nbytes
    ne = o.size
    print('////////////////////////////////////////')
    print(' Information for ndarray '+array_names[i])
    print(' data type            : ', dtype)
    print(' number of elements   : ', ne)
    print(' element size (bytes) : ', isize)
    print(' dimensions           : ', ndim)
    for j in range(ndim):
        print('     dimension '+str(j)+' size :', o.shape[j])
    print(' storage space (bytes): ', ssp)
    if (ndim > 1):
        print(' Element spacing along dimension 1 (bytes): ', o.strides[0])
        print(' Element spacing along dimension 2 (bytes): ', o.strides[1])
    print('')
