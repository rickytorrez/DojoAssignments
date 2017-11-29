a=[2,4,10,16]

def draw_stars (a,var):
    b=[]
    for i in a:
        i=i*var
        b.append(i)
    return b

for i in draw_stars(a,'*'):
    print i