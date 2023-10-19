import numpy as np
import pandas as pd
import glob

def fit_velocity_file(df):
    # Get the site name from the file name
    # site = filename.split('/')[-1].split('_')[0]
    site = str(df['site'][0])
    coeffs_E = np.polyfit(df['yyyy.yyyy'], df['__east(m)'], 1)
    coeffs_N = np.polyfit(df['yyyy.yyyy'], df['_north(m)'], 1)
    coeffs_U = np.polyfit(df['yyyy.yyyy'], df['____up(m)'], 1)
    return site, coeffs_E[0], coeffs_N[0], coeffs_U[0]

def coordinates(df):
    lat = np.average(df['_latitude(deg)'])
    lon = np.average(df['_longitude(deg)'])
    elev = np.average(df['__height(m)'])
    return lat, lon, elev
    
def fit_velocity(tlist, ylist):
    coeffs_U = np.polyfit(tlist, ylist, 1)
    return coeffs_U 

# GPS28 = pd.read_csv('timeseries/P028.NA.tenv3',  delim_whitespace=True)
def fit_all_files(folder,pattern):
    P_files = glob.glob(folder+'/'+pattern)
    for i in P_files:
        GPS = pd.read_csv(i,  delim_whitespace=True)
        site, E, N, U =fit_velocity_file(GPS)
        lat,lon, elev =coordinates(GPS)
        print(lat, lon, elev)
        print(site, E, N, U)
        