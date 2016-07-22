import numpy as na
import matplotlib.pyplot as plt;plt.ion()

star_rads = na.logspace(-1,1,5)
rp0 = 10.
plan_rads = star_rads*rp0


specs = 10.**na.array([-0.9,-0.5,-0.13,0.,0.08,0.24,0.58,0.92])
spec_labs = ['M8V','M5V','K5V','G2V','F5V','A5V','B5V','O9V']


depths = na.logspace(-2,1,4)
depths = na.array([.01,0.1,1.,1.5])

plan_rads = []
for i in range(len(depths)):
    plan_rads.append(star_rads*na.sqrt(depths[i]/100.)*109.)
plan_rads = na.array(plan_rads)

for i in range(len(depths)):    plt.loglog(star_rads,plan_rads[i],label='%.2f%% Depth'%depths[i])
for i in range(len(specs)):     plt.text(specs[i],0.2,spec_labs[i],horizontalalignment='center',size='large',rotation=90)
plt.loglog(1.14,15.3,marker='*',color='r',ms=20)
plt.xlabel(r"Stellar Radius [R$_\odot$]",size='large')
plt.ylabel(r"Planet Radius [R$_\oplus$]",size='large')
plt.legend(loc='upper left')
plt.ylim(top=1.e2)
plt.savefig('/Users/anthonyharness/Desktop/star_vs_planet.png')

plan_rads = na.logspace(-2,1,4)
plan_rads = na.array([1.,2.,4.,10.])
new_dep = []
for i in range(len(plan_rads)):
    new_dep.append( (plan_rads[i]/109./star_rads)**2.*100.)
new_dep = na.array(new_dep)

plt.figure()
for i in range(len(new_dep)):    plt.loglog(star_rads,new_dep[i],label=r"%.2f R$_\oplus$"%plan_rads[i])
for i in range(len(specs)): plt.text(specs[i],3.e-4,spec_labs[i],horizontalalignment='center',size='large',rotation=90)
plt.loglog(1.14,1.5,marker='*',color='r',ms=20)
plt.xlabel(r"Stellar Radius [R$_\odot$]",size='large')
plt.ylabel('% Transit Depth',size='large')
plt.legend(loc='upper right')
plt.ylim([1.e-4,10.])
plt.savefig('/Users/anthonyharness/Desktop/star_vs_depth.png')


import pdb;pdb.set_trace()