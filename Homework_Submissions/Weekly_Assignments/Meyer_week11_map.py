#%%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point, Polygon
import contextily as ctx
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


# %%
# Identifying file pathways and where to find them

# Class files
gages_shapefile = os.path.join('../../data/gagesii_shapefile', 'gagesII_9322_sept30_2011.shp')
arizona_watershed =  os.path.join('../../data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
# Data retrieved from https://www.sciencebase.gov/catalog/item/5eaa545982cefae35a22231f
national_boundaries =  os.path.join('../../data/GovernmentUnits_National_GDB', 'GovernmentUnits_National_GDB.gdb')

# Listing the layers within each file
fiona.listlayers(gages_shapefile)
fiona.listlayers(arizona_watershed)
fiona.listlayers(national_boundaries)

# Reading in geodataframes using geopandas (gpd.read_file)
gages = gpd.read_file(gages_shapefile)
HUC8 = gpd.read_file(arizona_watershed, layer='WBDHU8')
states = gpd.read_file(national_boundaries, layer='GU_StateOrTerritory')
native_land = gpd.read_file(national_boundaries, layer='GU_NativeAmericanArea')

#%%
# Checking the column names
gages.columns
HUC8.columns
states.columns
native_land.columns

# Checking the shapes
gages.shape
HUC8.shape
states.shape
native_land.shape

# Checking the Coordinate Reference System (.crs)
gages.crs
HUC8.crs
states.crs
native_land.crs

# %%
# Checking the geometry type
gages.geom_type
HUC8.geom_type
states.geom_type
native_land.geom_type

# Checking the total bounds (lat/lon)
gages.total_bounds
HUC8.total_bounds
states.total_bounds
native_land.total_bounds

#%%
# Subsetting the gages only in arizona
gages_arizona = gages[gages['STATE']=='AZ']
gages_arizona.shape


#%%
# Calculating native population density
population = (native_land['POPULATION'])
area = (native_land['AREASQKM'])
density = population / area

native_land.insert(3, 'density', pd.Series(density))

# native population density greater than 100 individuals/sqkm
native_land_10 = native_land[native_land['density']<10]
native_land_0 = native_land[native_land['density']<1]
#%%
# Checking the type
type(gages)
type(HUC8)
type(states)
type(native_land)

#%%
# Creating an array of gages coordinates within Arizona
gage_coordinates = np.array(gages_arizona[['LNG_GAGE','LAT_GAGE']]).astype(float)

# Converting these locations into point spatial features
gage_point_geometries = [Point(xy) for xy in gage_coordinates]

# Creating a geopandas dataframe of the gage points
point_gages_df = gpd.GeoDataFrame(gage_point_geometries, 
                                  columns=['geometry'], 
                                  crs=HUC8.crs)

fig, ax = plt.subplots(figsize=(5,5))
HUC8.plot(ax=ax)
point_gages_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
plt.show()

#%%
points_gages_projection = point_gages_df.to_crs(gages_arizona.crs)

gages_arizona.plot(column='DRAIN_SQKM', categorical=False,
                   legend=True, markersize=45, cmap='Set2',
                   ax=ax)

points_gages_projection.plot(ax=ax, color='black', marker='*')

#%%
HUC8_projection = HUC8.to_crs(gages_arizona.crs)

fig, ax = plt.subplots(figsize=(5, 5))

gages_arizona.plot(column='DRAIN_SQKM', categorical=False,
                   legend=True, markersize=25, cmap='Set2',
                   ax=ax)
points_gages_projection.plot(ax=ax, color='black', marker='*')

HUC8_projection.boundary.plot(ax=ax, color=None,
                              edgecolor='black', linewidth=1)

#%%
HUC8_projection = HUC8.to_crs(gages_arizona.crs)
native_land_projection = native_land.to_crs(gages_arizona.crs)

fig, ax = plt.subplots(figsize=(5,5))

HUC8.plot(ax=ax, cmap='viridis')

gages_arizona.plot(column='DRAIN_SQKM', categorical=False,
                   legend=True, cmap='magma',
                   ax=ax)
points_gages_projection.plot(ax=ax, color='black', 
                             marker='*', markersize=15)
HUC8_projection.boundary.plot(ax=ax, color=None,
                              edgecolor='black', linewidth=1)


#%%
# The gages points are within a different projection, thus,
            # they need to be fixed to the same projection.
            # This (.to_crs) function only works if the
            # original spatial object (gages_arizona) has a
            # coordinate reference systems assigned to it, and
            # if that coordinate reference system is the 
            # correct coordinate reference system.
points_gages_projection = point_gages_df.to_crs(gages_arizona.crs)
native_land_projection = native_land.to_crs(gages_arizona.crs)
native_land_10_proj = native_land_10.to_crs(gages_arizona.crs)
native_land_0_proj = native_land_0.to_crs(gages_arizona.crs)
states_projection = states.to_crs(gages_arizona.crs)


# ------------------ARIZONA--------------------------------

HUC8_projection = HUC8.to_crs(gages_arizona.crs)

fig, ax = plt.subplots(figsize=(10,10))
HUC8.plot(ax=ax, cmap='YlOrRd')

# plotting gages in arizona
gages_arizona.plot(column='DRAIN_SQKM', categorical=False,
                   legend=False, markersize=30, cmap = 'YlOrRd', 
                   ax=ax)

# plotting the native land projection
native_land_10_proj.plot(ax=ax)
native_land_0_proj.plot(ax=ax)

# plotting the native land area boundaries
native_land.boundary.plot(color=None, 
                          edgecolor='white', ax=ax)
native_land_0.boundary.plot(color=None, 
                            edgecolor='white', ax=ax, 
                            hatch = '/////')
native_land_10.boundary.plot(color=None, 
                             edgecolor='white', ax=ax)

# plotting the point projection
points_gages_projection.plot(ax=ax, color = 'black', 
                             marker='.', markersize=10)

# plotting the HUC8 (watershed) projection
HUC8_projection.boundary.plot(color=None, linewidth = 2, 
                              ax=ax)

point_gages_df.plot(ax=ax, color='black', marker='*', 
                    markersize=10)

#plotting state boundaries
states.boundary.plot(color=None, edgecolor='black', 
                     linewidth=1, ax=ax, alpha = 0.5)

# Making legend
lessthan10 = mpatches.Patch(color='white', fill=False, 
                            hatch=' ',label = '<10 People/km$^2$')
morethan0 = mpatches.Patch(color='white', fill=False, 
                           hatch='/////', label = '>0 People/km$^2$')
black_star = mlines.Line2D([], [], color='black', marker='*', 
                           linestyle='None',
                          markersize=5, label='Streamgage')
gagepoints =mpatches.Patch(color='black',fill=False, edgecolor='none', 
                           hatch='*',label='Streamgage')
fig.legend(bbox_to_anchor=(0.18, 0.05), framealpha=0, edgecolor='white', 
           facecolor='none',handles=[lessthan10, morethan0, black_star], 
           loc='lower left', ncols=3)

# Formatting
ax.set_facecolor('lightgray')
fig.set_facecolor('darkgray')
ax.set_title("HUC8 Boundaries and Native American Reservation Population Density", fontsize=12)
ax.grid(alpha=0.5)
plt.xlim(-116,-107.5)
plt.ylim(29.5,39.5)
plt.xlabel('Latitude')
plt.ylabel('Longitude')

im = ax.imshow([gages_arizona.DRAIN_SQKM], cmap='YlOrRd', vmin=0, vmax=35000)
fig.colorbar(im,ax=ax, label='Watershed Basin Drainage Area (km$^2$)', cmap='YlOrRd')
plt.show()

fig.savefig('Meyer_HW11_fig.png', dpi=300)
# %%
