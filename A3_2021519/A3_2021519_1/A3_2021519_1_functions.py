import math
def matmul(A,B):
    col_B = len(B[0])
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(col_B):
            sum = 0
            for k in range(len(A[i])):
                sum += B[k][j] * A[i][k]
            res[i].append(sum)
    return res


def scaling(x,y,z,sx,sy,sz):
        for k in range(len(x)):
            x[k] = (x[k]*sx)
        for k in range(len(y)):
            y[k] = (y[k]*sy)
        for k in range(len(z)):
            z[k] = (z[k]*sz)

def translation(x,y,z,tx,ty,tz):
    for k in range(len(x)):
        x[k] = (x[k]+tx)
    for k in range(len(y)):
        y[k] = (y[k]+ty)
    for k in range(len(z)):
        z[k] = (z[k]+tz)

def rotation(x,y,z,axis,phi):
    if axis == 'x':
        for k in range(len(y)):
            y[k] = round(((y[k]*math.cos(phi))-(z[k]*math.sin(phi))),2)
        for k in range(len(z)):
            z[k] = round(((y[k]*math.sin(phi))+(z[k]*math.cos(phi))),2)
    elif axis == 'y':
        for k in range(len(x)):
            x[k] = round((x[k]*math.cos(phi))+(z[k]*math.sin(phi)),2)
        for k in range(len(z)):
            z[k] = round((z[k]*math.cos(phi))-(x[k]*math.sin(phi)),2)
    elif axis == 'z':
        for k in range(len(x)):
            x[k] = round(((x[k]*math.cos(phi))-(y[k]*math.sin(phi))),2)
        for k in range(len(x)):
            x[k] = round(((y[k]*math.cos(phi))+(x[k]*math.sin(phi))),2)  
    else:
        return False
