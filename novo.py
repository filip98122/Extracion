import math
def Vector_Normalization(x,y):
    # Calculate dx and dy with direction
    vector_length=math.sqrt(x*x+y*y)#Pitagorina teorema
    x=x/vector_length
    y=y/vector_length
    return x,y
for i in range(5):
    def vector_to_angle(x1,y1):
        x,y=Vector_Normalization(x1,y1)
        radians=math.acos(x)
        anglenotnormal = int(round(math.degrees(radians)))
        anglenotnormal-=90
        anglenotnormal*=-1
        anglenotnormal+=360
        anglenotnormal%=360
        if y<0:
            if anglenotnormal>=180:
                anglenotnormal-=2*(abs(270-anglenotnormal))
            else:
                anglenotnormal-=2*(abs(90-anglenotnormal))
        anglenotnormal+=360
        anglenotnormal%=360
        return anglenotnormal
    print(vector_to_angle(int(input()),int(input())))
