import haversine as hs

def distanceCheck(loc1, loc2):
    distance_between = hs.haversine(loc1,loc2)

    return distance_between
