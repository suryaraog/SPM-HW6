class SprintVelocity:
    def __init__(self):
        self.sprint_points = []

    def collect_sprint_points(self):
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
        if not self.sprint_points:
            print("No sprint points entered.")
            return 0
        return sum(self.sprint_points) / len(self.sprint_points)

# Assuming the collection method is already called
if __name__ == "__main__":
    sprint_velocity = SprintVelocity()
    sprint_velocity.collect_sprint_points()
    print(f"Average Velocity: {sprint_velocity.calculate_velocity()}")