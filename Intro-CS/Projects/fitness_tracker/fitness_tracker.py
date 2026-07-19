from dateutil import parser
from gps import gpsDistance


class Workout(object):
    """
    A class that keeps track of
    your fitness
    """

    cal_per_hr = 200

    def __init__(self, start, end, calories=None):
        """
        creates a workout class; start and 
        end are strings,
        calories is an optional float
        """
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = "😓"
        self.kind = "Workout"
    
    def get_start(self):
        """return the start time of the workout"""   
        return self.start
    
    def get_end(self):
        """return the end time of the workout"""
        return self.end
    
    def get_calories(self):
        """return the total calories burned during the workout"""
        if (self.calories is None):
             # calc the calories based on the length of the workout and cal_per_hr
            return self.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories
    
    def get_kind(self):
        """return the kind of workout; i.e. swim, run.."""
        return self.kind
    
    def set_start(self, start):
        """set the start time of the workout"""
        self.start = parser.parse(start)
    
    def set_end(self, end):
        """set the end time of your workout"""
        self.end = parser.parse(end)
    
    def set_calories(self, other):
        """set the total calories burnt"""
        self.calories = other
    
    def get_duration(self):
        """
        returns the time duration you've been 
        training for.
        """
        return self.end - self.start
    
    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr =  f"|{'–'*width}|\n"
        retstr += f"|{' ' *width}|\n"
        retstr += f"| {self.icon}{' '*(width-3)}|\n"  #assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"|{' ' *width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"{round(self.get_calories(),1)}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"

        retstr += f"|{' ' *width}|\n"
        retstr +=  f"|{'_'*width}|\n"

        return retstr
    
    def __eq__(self, other):
        """
        returns True if this workout is the same as the other, 
        False o.w
        """
        return type(self) == type(other) and \
        self.start == other.start and \
        self.end == other.end and \
        self.kind == other.kind and \
        self.get_calories() == other.get_calories()
        

class RunWorkout(Workout):
    """Create a new instance of a running workout, where start and
        end are strings representing the start and end time of the workout,
        and elev is the total elevaation gain in the workout in feet,
        calories is an optional number representing the calories 
        burned in the run, and route_gps_points is an optional array 
        of (lat,lon) pairs representing the route of the run"""
    
    # redefine class variable cal_per_hr
    cals_per_km = 100 

    def __init__(self, start, end, elev=0, calories=None, route_gps_points=None):
        super().__init__(start, end, calories)
        self.elev = elev
        self.icon = "🏃🏽"
        self.kind = "Running"
        self.route_gps_points = route_gps_points
    
    def get_elev(self):
        """Return the elevation gain of the workout in feet"""
        return self.elev

    def set_elev(self, other):
        """Sets the elevation gain of the workout in feet, to other"""
        self.elev = other

    def get_calories(self):
        """Return the total calories consumed by the workout, derived
        using 1) the GPS points if supplied, 2) calories, if supplied,
        or 3) an estimate of the calories based on the duration"""
        if (self.route_gps_points is not None):
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1:]:
                dist += gpsDistance(lastP,p)
                lastP = p
            return dist * RunWorkout.cals_per_km
        else:
            return super().get_calories()
        
    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false o.w."""
        return super().__eq__(other) and self.elev == other.elev
    

class SwimWorkout(Workout):
    """subclass of Workout representing swimming"""

    # redefine class variable cal_per_hr
    cal_per_hr = 400
    
    def __init__(self, start, end, pace, calories=None):
        """a new instance of a swimming workout, where start and
        end are strings represent the start and end time of the workout,
        and pace is the pace of the workout in min/100yd, and calories
        is an optional parameter specifying the calories burned in the workout
        """
        super().__init__(start, end, calories)
        self.pace = pace
        self.kind = "swimming"
        self.icon = "🏊🏽"
    
    def get_pace(self):
         """returns the pace of the workout"""
         return self.pace
    
    def get_calories(self):
        if (self.calories is None):
             # calc the calories based on the length of the workout and cal_per_hr
            return SwimWorkout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:       
            return self.calories


# =============================================================================
# EXAMPLE:  Show how RunWorkout and SwimWorkout can reuse __str__ from Workout
# =============================================================================

w = Workout('9/30/2021 1:35 PM','9/30/2021 1:57 PM') # uses 200 cal_per_hr
r = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:57 PM', 100) # uses 200 cal_per_hr
sw = SwimWorkout('9/30/2021 1:35 PM','9/30/2021 1:57 PM', 100) # uses 400 cal_per_hr

# print(w)
# print(r)
# print(sw)

# =============================================================================
# EXAMPLE:  Subclasses can be used in place of workouts
# =============================================================================
def total_calories(workouts):
	cals = 0
	for w in workouts:
		cals += w.get_calories()
	return cals

def total_elevation(run_workouts):
	elev = 0
	for w in run_workouts:
		elev += w.get_elev()
	return elev

w1 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM') # 30 min workout
w2 = Workout('9/30/2021 4:35 PM','9/30/2021 5:05 PM') # 30 min workout
rw1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:35 PM', 100) # 2 hr workout
rw2 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:35 PM', 200) # 2 hr workout

print(total_calories([w1,w2,rw1,rw2]))  # (1) # cal = 100+100+400+400
print(total_elevation([rw1,rw2]))       # (2) # elev = 100+200