# Write a program that takes as input the speed of a car e.g 80.
# If the speed is less than 70, it should print “Ok”.
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: 
# “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.


def speed_limit(speed):
    maxpoint = 12
    increment = 5
    limit = 70
    
    if  speed <=limit:
        print("Okay")
    
    else:
        demerit_points = (speed - limit)
        actual_point = demerit_points/increment
        
        print(f"Demerit points:{actual_point}")
        
        if actual_point >= 12:
            print(f"Suspended license cause of {actual_point} points"  )

driving_speed = int(input("Enter speed: "))

speed_limit(driving_speed)
