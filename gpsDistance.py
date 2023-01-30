from math import sin, cos, sqrt, atan2, radians

tl=[-33.968508, 151.1083948]

# approximate radius of earth in km
R = 6373.0

# vehicles={}

def distancetoLight(vehLat1,vehLon1):
    lat1 = radians(tl[0])
    lon1 = radians(tl[1])
    lat2 = radians(vehLat1)
    lon2 = radians(vehLon1)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancetoLight=round(R*c*1000,2)
    print(distancetoLight)
    return distancetoLight













