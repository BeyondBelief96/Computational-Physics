import vpython as vp

def sodium_chloride_lattice(length_of_side):
    L = length_of_side
    R = 0.3
    count = 1
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                if count % 2 == 0:
                    vp.sphere(pos = vp.vector(i, j, k), radius=R, color = vp.color.cyan)
                else:
                    vp.sphere(pos = vp.vector(i, j, k), radius=R, color = vp.color.red)
                count+=1
                
sodium_chloride_lattice(5)

def fcc_lattice(length_of_side):
    L = length_of_side
    R = 0.3
    count = 1
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                vp.sphere(pos = vp.vector(i, j, k), radius=R, color = vp.color.cyan)
                vp.sphere(pos = vp.vector(i + 0.5, j + 0.5, k), radius=R, color = vp.color.cyan)
                vp.sphere(pos = vp.vector(i, j + 0.5, k + 0.5), radius=R, color = vp.color.cyan)
                vp.sphere(pos = vp.vector(i + 0.5, j, k + 0.5), radius=R, color = vp.color.cyan)



            