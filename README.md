# pixelized_heatmap

# objective
Create a python program to take the input from all radio base stations (in this case 4G LTE network) in a country to estimate the traffic distribution.

# By Lim Kah Ming, 2016

# Input Details:
1. Site Name (Name of the radio base station)
2. Cell Name (or Sector Name)
3. Subcell Name (A cell being splitted to many subcell based on the bins of the Timing Advance Statistics or Propagation Delay Statistics in 3G WCDMA)
4. Data Users (Total data users during Busy Hour for the subcell, distributed from a cell based on weightage of total transactions in each subcell)
5. radius_s and radius_e (starting point and ending point of a subcell, eg 0-234m, 234-546m, etc)
6. Lat & Long (GPS coordinates of the Radio Base Station Site)
7. Beamwidth (beamwidth of the sector/cell. typically 65 degree)
8. Azimuth (direction of the sector/cell)

# Output
A list of GPS coordinates with respective data users count during busy hour and the top 3 contributing sectors/cells.

