class SprintVelocity:
    """
    A class to calculate and display the sprint velocity of a team based on entered sprint points.

    Attributes:
        sprint_points (list): A list to store the points completed in each sprint.
    """

    def __init__(self):
        """
        Initializes the SprintVelocity class with an empty list for sprint points.
        """
        self.sprint_points = []

    def collect_sprint_points(self):
        """
        Collects sprint points from the user via command-line input.

        Continuously prompts the user to enter the points completed in each sprint,
        accepting only integer values. The user can type 'done' to finish entering points.
        """
        print("Enter sprint points (type 'done' to finish): ")
        while True:
            entry = input("> ")
            if entry.lower() == 'done':
                break
            try:
                point = int(entry)
                self.sprint_points.append(point)
            except ValueError:
                print("Please enter a valid integer or 'done' to finish.")

    def calculate_velocity(self):
        """
        Calculates the average sprint velocity based on the entered sprint points.

        Returns:
            float: The average sprint velocity. Returns 0 if no sprint points were entered.
        """
        if not self.sprint_points:
            print("No sprint points entered.")
            return 0
        return sum(self.sprint_points) / len(self.sprint_points)
    
    def display_velocity(self):
        """
        Calculates and displays the sprint velocity.

        Prints the calculated sprint velocity to the console in a user-friendly format.
        """
        velocity = self.calculate_velocity()
        print(f"\nCalculated Sprint Velocity: {velocity} points per sprint")


class TeamMember:
    def __init__(self, days_off, ceremony_hours, hours_per_day, sprint_days):
        self.days_off = days_off
        self.ceremony_hours = ceremony_hours
        self.hours_per_day = hours_per_day
        self.sprint_days = sprint_days

class TeamCapacity:
    def __init__(self):
        self.team_members = []

    def collect_team_members(self):
        print("\nEnter team member details (type 'done' when finished):")
        while True:
            days_off_input = input("Days off (or type 'done' to finish): ")
            if days_off_input.lower() == 'done':
                break
            ceremony_hours = int(input("Ceremony hours: "))
            hours_per_day_min = int(input("Minimum hours per day: "))
            hours_per_day_max = int(input("Maximum hours per day: "))
            sprint_days = int(input("Sprint days: "))
            
            member = TeamMember(
                days_off=int(days_off_input),
                ceremony_hours=ceremony_hours,
                hours_per_day=(hours_per_day_min, hours_per_day_max),
                sprint_days=sprint_days
            )
            self.team_members.append(member)
            
    def calculate_individual_capacity(self, member):
        avg_hours_per_day = sum(member.hours_per_day) / 2
        available_hours = (member.sprint_days - member.days_off) * avg_hours_per_day - member.ceremony_hours
        return available_hours


# Main program execution
if __name__ == "__main__":    
    print("Select feature to test:\n1. Sprint Velocity\n2. Team Capacity")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        # Create an instance of the SprintVelocity class
        sprint_velocity = SprintVelocity()
        # Collect sprint points from the user
        sprint_velocity.collect_sprint_points()
        # Display the calculated sprint velocity
        sprint_velocity.display_velocity()
    elif choice == '2':
        team_capacity = TeamCapacity()
        team_capacity.collect_team_members()
    else:
        print("Invalid choice.")