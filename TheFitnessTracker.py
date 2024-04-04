activities = ['dancing', 'swimming', 'biking' ]
duration = [10, 20, 15]

def fitness_log_tracker (activities, duration):
    
    fitness_log = {}
    for i in range(len(activities)):
        fitness_log[activities[i]] = duration[i]
    
    return fitness_log

def calories (duration):
    burn  = [i *3.5 for i in duration]
    return burn

fitness = fitness_log_tracker(activities, duration)
burn = calories(duration)

print(f"The activities and Time for completion are as follows: {fitness}")
print(f"the calories burned per activie are: {burn}")