# NOTE: This script can be modified for different pair styles
# See in.elastic for more info.

### Choose potential ###
pair_style      smatb
#pair_coeff  id1 id2 atomDiameter p q A Xi cut_start cut_end
pair_coeff 1 1 2.814 10.7960 3.1976 0.1993 2.2318 4.8745 5.6286
pair_coeff 1 2 2.779 9.7190 2.7488 0.2750 2.4880 4.8745 5.0912
pair_coeff 2 2 2.545 8.6420 2.3000 0.1582 1.8443 4.4091 5.0912



# Setup neighbor style
#neighbor 1.0 nsq
#neigh_modify once no every 1 delay 0 check yes

# Setup minimization style
min_style            cg
min_modify           dmax ${dmax} line quadratic

# Setup output
thermo          1
thermo_style custom step temp pe press pxx pyy pzz pxy pxz pyz lx ly lz vol
thermo_modify norm no
