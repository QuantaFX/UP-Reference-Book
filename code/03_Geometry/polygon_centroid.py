def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def centroid(points):
    n = len(points)
    ans_x, ans_y = 0.0, 0.0
    z = 0.0

    for i in range(n):
        j = (i - 1) % n
        cp = cross(points[j], points[i])

        ans_x += (points[j][0] + points[i][0]) * cp
        ans_y += (points[j][1] + points[i][1]) * cp
        z += cp

    return (ans_x / (3 * z), ans_y / (3 * z))