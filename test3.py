e = "B0"
f = "B1"
g = "A6"
h = "E6"

def l2n(coord):
  return (ord(coord[0])-65,int(coord[1]))
def n2l(coord):
  return (chr(coord[0]+65),int(coord[1]))

def check_intersect(a, b, c, d):
  return(line_intersection((l2n(a),l2n(b)),(l2n(c),l2n(d))))
  

def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
    raise Exception('lines do not intersect')

  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  return x, y

print(check_intersect(e, f, g, h))