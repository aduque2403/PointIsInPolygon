def is_point_in_path(x: int, y: int, poly) -> bool:
    # Determine if the point is in the polygon.
    #
    # Args:
    #   x -- The x coordinates of point.
    #   y -- The y coordinates of point.
    #   poly -- a list of tuples [(x, y), (x, y), ...]
    #
    # Returns:
    #   True if the point is in the path or is a corner or on the boundary
    #
    # Latitude corresponds to Y
    # Longitude corresponds to X
     
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i][0]) and (y == poly[i][1]):
                # point is a corner
                return True
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                slope = (x-poly[i][0])*(poly[j][1]-poly[i][1])-(poly[j][0]-poly[i][0])*(y-poly[i][1])
                if slope == 0:
                    # point is on boundary
                    return True
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    c = not c
            j = i
        return c

pointx = -14.5689
pointy = 23.789

polygon = [(12.45, 45.23), (14.23, 23.45), (12.45, 15.65), (0.5, 10.45)]

print (is_point_in_path(pointx, pointy, polygon))