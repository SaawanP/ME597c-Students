from math import exp
# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    def trajectory_planner(self):
        TYPE = "parabola"
        # TYPE = "sigmoid"

        trajectory = []
        if TYPE == 'parabola':
            trajectory = [[x/10, (x/10)**2] for x in range(15)]
        elif TYPE == 'sigmoid':
            trajectory = [[x/10, 2 / (1+exp(-2*x/10)) + 1] for x in range(25)]
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        return trajectory

