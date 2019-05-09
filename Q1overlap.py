def overlap_check(x1,x2,x3,x4):

    # assume two lines have non-zero legth: ie. x1<x2 and x3<x4 always.
    return (x1<x3 and x3<x2) or (x3<x1 and x1<x4)

print( overlap_test(1,3,7,9) )
print( overlap_test(7,9,1,3) )
print( overlap_test(1,7,3,9) )
print( overlap_test(3,9,1,7) )
print( overlap_test(3,7,1,9) )
print( overlap_test(1,9,3,7) )
print( overlap_test(-3,-1,-9,-7) )
print( overlap_test(-9,-7,-3,-1) )
print( overlap_test(-7,-1,-9,-3) )
print( overlap_test(-9,-3,-7,-1) )
print( overlap_test(-7,-3,-9,-1) )
print( overlap_test(-9,-1,-7,-3) )
print( overlap_test(-3,1,-9,7) )
print( overlap_test(-9,7,-3,1) )
print( overlap_test(-7,1,-9,3) )
print( overlap_test(-9,3,-7,1) )
print( overlap_test(-7,3,-9,1) )
print( overlap_test(-9,1,-7,3) )