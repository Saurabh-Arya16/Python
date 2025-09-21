def can_visit_all_waypoints(battery_percentage, waypoints):
    # Check if the drone has enough battery to start the journey
    if battery_percentage < 30:
        print("Drone cannot start the journey, battery below 30%")
        return

    # Calculate battery consumption per waypoint
    battery_required_per_waypoint = 10

    # Loop through each waypoint
    for i in range(waypoints):
        # Check if there is enough battery for the next waypoint
        if battery_percentage >= battery_required_per_waypoint:
            battery_percentage -= battery_required_per_waypoint
        else:
            print("Drone cannot visit all waypoints")
            return

    # If the loop completes, the drone can visit all waypoints
    print("Drone can visit all waypoints")

# Example usage:
current_battery = int(input("Enter the current battery percentage: "))
num_waypoints = int(input("Enter the number of waypoints: "))

can_visit_all_waypoints(current_battery, num_waypoints)
