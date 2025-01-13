import numpy as np

red_line_adj = np.zeros((79,79),dtype=int)
def rcon(n1,n2):
    red_line_adj[n1,n2] = 1
    red_line_adj[n2,n1] = 1
def rdcon(n1,n2):
    red_line_adj[n1,n2] = 0
    red_line_adj[n2,n1] = 0

for n in range(1,65):
    rcon(n,n+1)
rcon(65,78)
rcon(78,66)
for n in range(67,71):
    rcon(n,n+1)
for n in range(72,75):
    rcon(n,n+1)
rcon(75, 76)
rcon(77, 76)
rcon(1,16)
rcon(27,77)
rcon(33,72)
rcon(38,71)
rcon(44,67)
rcon(52,66)
rcon(0, 9)

    
np.savetxt("Other/red_adj.txt",red_line_adj,fmt="%d")

# ================================================================

green_line_adj = np.zeros((153,153),dtype=int)
def gcon(n1,n2):
    green_line_adj[n1,n2] = 1
def gdcon(n1,n2):
    green_line_adj[n1,n2] = 0
    green_line_adj[n2,n1] = 0

gcon(1,13)                  # A to D
gcon(151,1)
gcon(2,151)
for n in range(1,13):       # ABC
    gcon(n+1,n)
gcon(13,12)                 # D to C
for n in range(13,29):      # DEF
    gcon(n,n+1)
    gcon(n+1,n)
for n in range(29,76):      # GHIJKLM
    gcon(n,n+1)
gcon(76,77)                 # M to N
gcon(77,101)                # N to R
for n in range(77,85):      # N
    gcon(n,n+1)
    gcon(n+1,n)
gcon(85,86)                 # N to O
for n in range(86,100):     # OPQ
    gcon(n,n+1)
gcon(100,85)                # Q to N
gcon(101,152)
gcon(152,102)
for n in range(101,150):    # RSTUVWXYZ
    gcon(n,n+1)
gcon(150,29)                # Z to G (? should be F)
gcon(0, 63)
gcon(57,0)
    
np.savetxt("Other/green_adj.txt",green_line_adj,fmt="%d")