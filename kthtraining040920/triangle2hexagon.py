def dist(x1, y1, x2, y2):
    return (abs(x2-x1)**2 + abs(y2-y1)**2)**0.5

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

def circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line=True, tangent_tol=1e-9):
    """ Find the points at which a circle intersects a line-segment.  This can happen at 0, 1, or 2 points.

    :param circle_center: The (x, y) location of the circle center
    :param circle_radius: The radius of the circle
    :param pt1: The (x, y) location of the first point of the segment
    :param pt2: The (x, y) location of the second point of the segment
    :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
    :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
    :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

    Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
    """

    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [intersections[0]]
        else:
            return intersections

bx, cx, cy = [float(x) for x in input().split()]
ax = float(0)
ay = float(0)
by = float(0)

c = dist(ax, ay, bx, by)
b = dist(ax, ay, cx, cy)
a = dist(bx, by, cx, cy)

ix = (a*ax + b*bx + c*cx)/(a + b + c)
iy = (a*ay + b*by + c*cy)/(a + b + c)

# d = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))

# ox = ((ax**2 + ay**2)*(by-cy) + (bx**2 + by**2)*(cy-ay) + (cx**2 + cy**2)*(ay-by))/d
# oy = ((ax**2 + ay**2)*(cx-bx) + (bx**2 + by**2)*(ax-cx) + (cx**2 + cy**2)*(bx-ax))/d

d = 2*(bx*cy - by*cx)

ox = (cy*(bx**2 + by**2) - by*(cx**2 + cy**2))/d
oy = (bx*(cx**2 + cy**2) - cx*(bx**2 + by**2))/d
circumrad = (ox**2 + oy**2)**0.5
# circumrad**2 = (x-ox)**2 + (y-oy)**2

mx, my = circle_line_segment_intersection((ox, oy), circumrad, (ax, ay), (ix, iy))[1]
nx, ny = circle_line_segment_intersection((ox, oy), circumrad, (bx, by), (ix, iy))[1]
px, py = circle_line_segment_intersection((ox, oy), circumrad, (cx, cy), (ix, iy))[1]

ab = line([ax, ay], [bx, by])
ac = line([ax, ay], [cx, cy])
bc = line([bx, by], [cx, cy])
np = line([nx, ny], [px, py])
nm = line([nx, ny], [mx, my])
mp = line([mx, my], [px, py])

ex, ey = intersection(ab, np)
fx, fy = intersection(ac, np)
gx, gy = intersection(ac, nm)
hx, hy = intersection(bc, nm)
jx, jy = intersection(bc, mp)
kx, ky = intersection(ab, mp)

ef = dist(ex, ey, fx, fy)
fg = dist(fx, fy, gx, gy)
gh = dist(gx, gy, hx, hy)
hj = dist(hx, hy, jx, jy)
jk = dist(jx, jy, kx, ky)
ke = dist(kx, ky, ex, ey)

print(ef, fg, gh, hj, jk, ke)