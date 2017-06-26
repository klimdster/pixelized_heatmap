# please make sure you have populated the input file 'subcell_input_4G_201705_sample.csv' before run this
import pandas as pd
import math
import numpy as np
df=pd.read_csv('subcell_input_4G_201705_sample.csv')

print ("starting task 1 of 2: generating pixelized heatmap")

def SubSectorPoints (Origin_lat, Origin_long, Beamwidth, Azimuth, Length_s_m, Length_e_m):
    deg2km=111.3195
    Angle = 90-Azimuth
    BeamB_sin = math.sin(math.radians(90-(Azimuth-Beamwidth/2)))    
    BeamB_cos = math.cos(math.radians(90-(Azimuth-Beamwidth/2)))
    BeamB_lat = Length_s_m*BeamB_sin/1000/deg2km+Origin_lat
    BeamB_long = Length_s_m*BeamB_cos/1000/deg2km+Origin_long
    BeamC_sin = math.sin(math.radians(Angle))  
    BeamC_cos = math.cos(math.radians(Angle))
    BeamC_lat = Length_s_m*BeamC_sin/1000/deg2km+Origin_lat
    BeamC_long = Length_s_m*BeamC_cos/1000/deg2km+Origin_long
    BeamD_sin = math.sin(math.radians(90-(Azimuth+Beamwidth/2)))    
    BeamD_cos = math.cos(math.radians(90-(Azimuth+Beamwidth/2)))
    BeamD_lat = Length_s_m*BeamD_sin/1000/deg2km+Origin_lat
    BeamD_long = Length_s_m*BeamD_cos/1000/deg2km+Origin_long
    BeamE_sin = math.sin(math.radians(90-(Azimuth-Beamwidth/2)))    
    BeamE_cos = math.cos(math.radians(90-(Azimuth-Beamwidth/2)))
    BeamE_lat = Length_e_m*BeamE_sin/1000/deg2km+Origin_lat
    BeamE_long = Length_e_m*BeamE_cos/1000/deg2km+Origin_long
    BeamF_sin = math.sin(math.radians(Angle))  
    BeamF_cos = math.cos(math.radians(Angle))
    BeamF_lat = Length_e_m*BeamF_sin/1000/deg2km+Origin_lat
    BeamF_long = Length_e_m*BeamF_cos/1000/deg2km+Origin_long
    BeamG_sin = math.sin(math.radians(90-(Azimuth+Beamwidth/2)))    
    BeamG_cos = math.cos(math.radians(90-(Azimuth+Beamwidth/2)))
    BeamG_lat = Length_e_m*BeamG_sin/1000/deg2km+Origin_lat
    BeamG_long = Length_e_m*BeamG_cos/1000/deg2km+Origin_long
    return BeamB_lat,BeamB_long,BeamC_lat,BeamC_long, BeamD_lat, BeamD_long, BeamG_lat,BeamG_long,BeamF_lat,BeamF_long, BeamE_lat, BeamE_long


df['B_lat'] = df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[0], axis=1)
df['B_long']= df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[1], axis=1)
df['C_lat']= df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[2], axis=1)
df['C_long']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[3], axis=1)
df['D_lat']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[4], axis=1)
df['D_long']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[5], axis=1)
df['G_lat']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[6], axis=1)
df['G_long']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[7], axis=1)
df['F_lat']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[8], axis=1)
df['F_long']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[9], axis=1)
df['E_lat']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[10], axis=1)
df['E_long']=df.apply(lambda row: SubSectorPoints(row['lat'], row['long'],row['beamwidth'],row['azimuth'],row['radius_s'],row['radius_e'])[11], axis=1)

def FramePosition(B_lat,B_long,C_lat,C_long,D_lat,D_long,G_lat,G_long,F_lat,F_long,E_lat,E_long):
    BL_lat = min(B_lat,C_lat,D_lat,G_lat,F_lat,E_lat)
    BL_long = min(B_long,C_long,D_long,G_long,F_long,E_long)
    TR_lat = max(B_lat,C_lat,D_lat,G_lat,F_lat,E_lat)
    TR_long = max(B_long,C_long,D_long,G_long,F_long,E_long)    
    return BL_lat,BL_long,TR_lat,TR_long

df['BL_lat'] = df.apply(lambda row: FramePosition(row['B_lat'], row['B_long'],row['C_lat'],row['C_long'],row['D_lat'],row['D_long'],row['G_lat'], row['G_long'],row['F_lat'],row['F_long'],row['E_lat'],row['E_long'])[0], axis=1)
df['BL_long'] = df.apply(lambda row: FramePosition(row['B_lat'], row['B_long'],row['C_lat'],row['C_long'],row['D_lat'],row['D_long'],row['G_lat'], row['G_long'],row['F_lat'],row['F_long'],row['E_lat'],row['E_long'])[1], axis=1)
df['TR_lat'] = df.apply(lambda row: FramePosition(row['B_lat'], row['B_long'],row['C_lat'],row['C_long'],row['D_lat'],row['D_long'],row['G_lat'], row['G_long'],row['F_lat'],row['F_long'],row['E_lat'],row['E_long'])[2], axis=1)
df['TR_long'] = df.apply(lambda row: FramePosition(row['B_lat'], row['B_long'],row['C_lat'],row['C_long'],row['D_lat'],row['D_long'],row['G_lat'], row['G_long'],row['F_lat'],row['F_long'],row['E_lat'],row['E_long'])[3], axis=1) 
df.to_csv('df.csv')


df=pd.read_csv('df.csv')

def FramePoint(BL_lat,BL_long,TR_lat,TR_long):
    x=np.arange(round(BL_long/2,3)*2,round(TR_long/2,3)*2,0.002)
    y=np.arange(round(BL_lat/2,3)*2,round(TR_lat/2,3)*2,0.002)
    temp=np.array(np.meshgrid(x,y)).reshape(2,-1).T
    dftemp=pd.DataFrame(temp)
    dftemp.columns =['long','lat']
    return dftemp

def point_inside_polygon(x,y,poly):
    n = len(poly)
    inside =0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = 1
        p1x,p1y = p2x,p2y
    return inside


dfpix=pd.DataFrame(columns = ['long', 'lat','data_users','cell_subcell', 'point_data_users','cellname'])
dfpixfinal=pd.DataFrame(columns = ['long', 'lat', 'point_data_users','cellname'])

file_fraction = 0
for i in range(len(df)):
#for i in range(100):
    print ("processing " + str(i+1) + " of " + str(len(df))) 
    dfpixtemp = FramePoint(df.loc[i]['BL_lat'],df.loc[i]['BL_long'],df.loc[i]['TR_lat'],df.loc[i]['TR_long'])
    dfpixtemp['data_users'] =df.loc[i]['data_users']
    dfpixtemp['cell_subcell'] =df.loc[i]['cell_subcell'] 
    dfpixtemp['cellname'] =df.loc[i]['cellname'] 
    # check in polygon or not    
    polygon=[(df.loc[i]['B_long'],df.loc[i]['B_lat']),(df.loc[i]['C_long'],df.loc[i]['C_lat']),(df.loc[i]['D_long'],df.loc[i]['D_lat']),(df.loc[i]['G_long'],df.loc[i]['G_lat']),(df.loc[i]['F_long'],df.loc[i]['F_lat']),(df.loc[i]['E_long'],df.loc[i]['E_lat'])]
    in_coverage = []
    for j in range(len(dfpixtemp)):
         in_coverage.append(point_inside_polygon(dfpixtemp.loc[j]['long'],dfpixtemp.loc[j]['lat'],polygon))
    
    dfpixtemp['in_coverage']=in_coverage
    coverage_points = dfpixtemp['in_coverage'].sum(axis=0)
    point_data_users = []
    for j in range(len(dfpixtemp)):
        point_data_users.append(dfpixtemp.loc[j]['data_users']*dfpixtemp.loc[j]['in_coverage']/coverage_points)
    
    dfpixtemp['point_data_users']=point_data_users
    dfpixtemp = dfpixtemp[dfpixtemp['in_coverage'] == 1]
    dfpixtemp=dfpixtemp.drop('in_coverage',axis=1)
    dfpix = pd.concat([dfpix,dfpixtemp],ignore_index=True)
    if len(dfpix)>1000000:    #original 1000000
        file_fraction=file_fraction+1
        print ("file_fraction of " + str(file_fraction) + " with length of " + str(len(dfpix)))
        dfpix = dfpix.groupby(['long','lat','cellname']).sum().reset_index() 
        dfpix=dfpix.drop('data_users',axis=1)   
        dfpixfinal=pd.concat([dfpixfinal,dfpix],ignore_index=True)
        dfpix=pd.DataFrame(columns = ['long', 'lat','data_users','cell_subcell', 'point_data_users'])

dfpix=dfpix.drop(['data_users','cell_subcell'],axis=1)
dfpixfinal=pd.concat([dfpixfinal,dfpix],ignore_index=True)
dfpixfinal.to_csv('HeatPixelRaw.csv',index=False)

dfpixfinal['point_data_users']=dfpixfinal['point_data_users'].apply(lambda x:x*1000)
dfpixfinal['point_data_users']=dfpixfinal['point_data_users'].round(1)
dfpixfinal=dfpixfinal[dfpixfinal['point_data_users']>0]
dfpixfinal.sort_values(by=['long','lat'], ascending=[True,True])
dfpixfinal.to_csv('HeatPixelRawx1000.csv',index=False)

print ("completed task 1 of 2, pixelized-heatmap generated as HeatPixelRawx1000.csv")

#################################################################
#################################################################
print ("starting task 2 of 2, getting top 3 contributor for each pixel")
#import pandas as pd   #uncomment this to run if just want to run task 2
dfpixfinal=pd.read_csv('HeatPixelRawx1000.csv')
dfpixfinal['lat']=dfpixfinal['lat'].astype(str)
dfpixfinal['long']=dfpixfinal['long'].astype(str)
dfpixfinal1=dfpixfinal.groupby(['lat','long']).sum().reset_index()
dfpixfinal1.rename(columns={'point_data_users':'Total'}, inplace=True)

print ("dfpixfinal1 length is " + str(len(dfpixfinal1)) + ", sum is " + str(dfpixfinal1['Total'].sum()) )

dfpixfinal2=dfpixfinal.sort_values(by=['lat','long','point_data_users'],ascending=[True,True,False]).groupby(['lat','long']).head(3).reset_index(drop=True)
dfpixfinal2=dfpixfinal2.sort_values(by=['lat','long','point_data_users'],ascending=[True,True,False])
print ("dfpixfinal2 length is " + str(len(dfpixfinal2)) + ", sum is " + str(dfpixfinal2['point_data_users'].sum()) )

#dfpixfinal2['point_data_users']=dfpixfinal2['point_data_users'].round(1)
dfpixfinal2['cellname'] = dfpixfinal2['cellname'].str.cat(dfpixfinal2['point_data_users'].values.astype(str), sep=':')
dfpixfinal2['cellname'] = dfpixfinal2.groupby(['lat','long'])['cellname'].transform(lambda x: ', '.join(x))
dfpixfinal2=dfpixfinal2[['lat','long','cellname']].drop_duplicates().reset_index()

print ("new dfpixfinal2 length is " + str(len(dfpixfinal2)) )
dfpixfinal2=dfpixfinal2.drop('index', axis=1)
dfpixfinal2.rename(columns={'cellname':'source_sectors'}, inplace=True)


dfpixfinal3=pd.merge(dfpixfinal1, dfpixfinal2, how='left', left_on=['lat','long'], right_on=['lat','long'])

dfpixfinal3.rename(columns={'Total':'point_data_users'}, inplace=True)
dfpixfinal3.to_csv('HeatPixelx1000_top3src.csv',index=False)
dfpixfinal3_simp=dfpixfinal3.drop('source_sectors',axis=1)
dfpixfinal3_simp.to_csv('HeatPixelx1000_users.csv',index=False)
print ("new dfpixfinal3 length is " + str(len(dfpixfinal3)) + ", sum is " + str(dfpixfinal3['point_data_users'].sum()) )

print ("completed task 2 of 2, pixelized-heatmap with top 3 contributor generated as HeatPixelx1000_top3src.csv")
