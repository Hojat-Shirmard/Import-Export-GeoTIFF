#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import gdal
import numpy

file = "G:/Python_Learning/TEST/LC81600392013183LGN00_B1.TIF"
ds = gdal.Open(file)
band = ds.GetRasterBand(1)
arr = band.ReadAsArray()
[cols, rows] = arr.shape
arr_min = arr.min()
arr_max = arr.max()
arr_mean = int(arr.mean())
arr_out = numpy.where((arr < arr_mean), 10000, arr)
driver = gdal.GetDriverByName("GTiff")
outdata = driver.Create("G:/Python_Learning/TEST/NB1.TIF", rows, cols, 1, gdal.GDT_UInt16)
outdata.SetGeoTransform(ds.GetGeoTransform())##sets same geotransform as input
outdata.SetProjection(ds.GetProjection())##sets same projection as input
outdata.GetRasterBand(1).WriteArray(arr_out)
outdata.GetRasterBand(1).SetNoDataValue(10000)##if you want these values transparent
outdata.FlushCache() ##saves to disk!!
outdata = None
band=None
ds=None


# In[ ]:




