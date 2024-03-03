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

# Create an instance and call the method to collect sprint points
if __name__ == "__main__":
    sprint_velocity = SprintVelocity()
    sprint_velocity.collect_sprint_points()
