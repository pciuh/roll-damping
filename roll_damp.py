#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

@date:   Fri, 03 Mar 2023, 17:32

@author: pciuh

This script estimates roll damping coefficient acc. to IKEDA
'''

import os
import sys
sys.path.append(os.getcwd()+'/modules/')
from ikeda import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iDir = 'input/'
cMap = 'PuRd'
rho,G = 1025.9,9.80665

fnam = 'ship'
df = pd.read_csv(fnam+'.csv',index_col=0)

df = df.fillna(0)
print(df)

lpp,brth,t,cb,cm,KG,tw,lbk,bbk = df['Value'].values
lbk,bbk = 0,0
VS = [4,8,12,16]
VS = np.arange(0,25,2)
phi = np.arange(1,20,2)

ogd = 1-KG/t
b44,b44d = [],[]
for vs in VS:

    u = vs*1852/3600

    bbkd = bilke(cb,cm,ogd,brth,bbk,lbk,lpp,t,phi,tw)
    bfd  = fric(lpp,brth,t,cb,ogd,phi,tw)
    bwd  = wave(cb,cm,ogd,brth,t,phi,tw,u)
    bed  = eddy(cb,cm,ogd,brth,t,phi,tw)
    bld  = lift(lpp,brth,t,cb,cm,ogd,u)

    b44t = bfd + bwd + bed + bld + bbkd
    b44d = np.append(b44d,b44t)

    b44  = np.append(b44,b44t*rho*cb*brth**3*t*lpp*np.sqrt(2*G/brth))


b44d = b44d.reshape(-1,len(phi))
b44 = b44.reshape(-1,len(phi))

phig,vg = np.meshgrid(phi,VS)

fig,ax = plt.subplots(figsize=(6,6))
cnt = ax.contourf(phig,vg,b44d,cmap=cMap,levels=11)
cbar = fig.colorbar(cnt,shrink=.75,orientation='horizontal',label=r'$\nu_{\varphi\varphi}$')
cbar.formatter.set_powerlimits((0, 0))
cbar.formatter.set_useMathText(True)
#ax.set_ylabel(r'$\nu_{\varphi\varphi}$')
ax.set_ylabel(r'$V_S$ (knots)')
ax.set_xlabel(r'$\varphi$ (deg)')
fig.tight_layout()
fig.savefig('plot.png',dpi=300)
plt.show()
