import numpy as np


A = np.loadtxt('Octa_118.in', usecols = (2,3,4), skiprows = 9)
atom_type = np.loadtxt('Octa_118.in', usecols = (1), skiprows = 9)
index = np.loadtxt('Octa_118.in', usecols = (0), skiprows = 9)


dist = 1.960000
z_max = np.amax(A[:,2]) + dist/2
z_min = np.amax(A[:,2]) - dist/2
Co = True
number = len(atom_type)

print(z_min,z_max,-np.amax(A[:,2]))
while z_max > -np.amax(A[:,2]):

    for i in range(0, number-1):
        # print(z_min,z_max,A[i,2])
        if (z_min<A[i,2]<z_max):
            atom_type[i] = atom_type[i] + Co
            # print(i)
    Co = not Co

    z_max = z_min
    z_min = z_min - dist



data =np.stack((index,atom_type,A[:,0],A[:,1],A[:,2]),axis =-1)


string = "# babbuccia \n {} atoms \n 2 atom types \n \n-400.00000 400.000 xlo xhi \n-400.00000 400.000 ylo yhi \n-400.00000 400.000 zlo zhi \n \n Atoms \n".format(int(number))
name = "TEST.in"
np.savetxt(name,data,fmt = ['%3d', '%3d','%3f','%3f','%3f'],delimiter = '    ', header=string,comments = '')
