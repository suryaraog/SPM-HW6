import unittest
from features import SprintVelocity, TeamMember, TeamCapacity

class TestSprintVelocity(unittest.TestCase):
    def test_calculate_velocity(self):
        # Testing with a predefined list of sprint points
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [8, 10, 12, 9]  # Example sprint points
        self.assertEqual(sprint_velocity.calculate_velocity(), 9.75)

class TestTeamCapacity(unittest.TestCase):
    def test_calculate_individual_capacity(self):
        # Testing individual capacity calculation
        member = TeamMember(2, 5, (6, 8), 10)  # Example team member
        team_capacity = TeamCapacity()
        self.assertEqual(team_capacity.calculate_individual_capacity(member), 51)

    def test_calculate_team_capacity(self):
        # Testing total team capacity calculation with two members
        team_capacity = TeamCapacity()
        team_capacity.team_members.append(TeamMember(2, 5, (6, 8), 10))  # Member 1
        team_capacity.team_members.append(TeamMember(1, 4, (7, 9), 10))  # Member 2
        self.assertEqual(team_capacity.calculate_team_capacity(), 119)  # Expected total capacity

if __name__ == '__main__':
    unittest.main()
