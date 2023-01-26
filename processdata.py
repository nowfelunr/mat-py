import pandas as pd
import numpy as np

# Read input CSV and conside first row as value as well.
rawdata = pd.read_csv('input.txt', header=None)

# Convert pandas df to numpy array
rawdata = rawdata.values

# Slicing values
x = rawdata[:,1]
y = rawdata[:,2]
xcos = rawdata[:,4]
ycos = rawdata[:,5]
E = rawdata[:,6]

xround = np.round(x)
yround = np.round(y)

xcosround = np.round(xcos*100)/100
ycosround = np.round(ycos*100)/100

xidx = np.unique(xround)
yidx = np.unique(yround)

xcosidx = np.unique(xcosround)
ycosidx = np.unique(ycosround)


xarray = np.arange(-1, 2)
yarray = np.arange(-1, 2)
xcosarray = np.arange(-1, 1.01, 0.01)
xcosarray = np.round(xcosarray*100)/100
ycosarray = np.arange(-1, 1.01, 0.01)
ycosarray = np.round(ycosarray*100)/100

# Initializing 4-d array

Egrid = np.empty(shape=(len(xarray), len(yarray), len(xcosarray), len(ycosarray)))

# Convert values to NaN (Matlab Way)

Egrid.fill(np.nan)


for xid in range(len(xarray)):
    for yid in range(len(yarray)):
        for xcosid in range(len(xcosarray)):
            for ycosid in range(len(ycosarray)):
                # Comparison of values
                comp_axis_vals = np.logical_and(xround==xarray[xid], yround==yarray[yid]) 
                comp_cos_vals = np.logical_and(xcosround==xcosarray[xcosid], ycosround==ycosarray[ycosid])
                oneid = np.logical_and(comp_axis_vals, comp_cos_vals)
                oneid = np.delete(oneid, np.where(oneid == False))
                if oneid.size != 0:
                    Egrid[xid, yid, xcosid, ycosid] = E[0]
               


nF = np.nanmax(Egrid)

# Normalize
Egrid = Egrid/nF

# Transposing the size of matrix
Egrid = np.transpose(Egrid, (3,2,1,0))
# Convert all nan to number values
Egrid = np.nan_to_num(Egrid, -1)

# Write the binary
Egrid.astype('float').tofile('Egrid.bin')

