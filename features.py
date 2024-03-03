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

# Main program execution
if __name__ == "__main__":
    # Create an instance of the SprintVelocity class
    sprint_velocity = SprintVelocity()

    # Collect sprint points from the user
    sprint_velocity.collect_sprint_points()

    # Display the calculated sprint velocity
    sprint_velocity.display_velocity()
