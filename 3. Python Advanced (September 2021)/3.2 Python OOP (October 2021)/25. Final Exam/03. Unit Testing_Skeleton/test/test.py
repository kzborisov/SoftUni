import unittest

from project.team import Team


class TestTeam(unittest.TestCase):
    def test_team_initialization(self):
        team = Team("name")
        self.assertEqual("name", team.name)
        self.assertEqual({}, team.members)

    def test_team_initialization__when_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Team("name2")
        expected = "Team Name can contain only letters!"
        self.assertEqual(expected, str(context.exception))

    def test_add_member__when_name_not_in_team(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        member_name_2 = "name 2"
        member_age_2 = 20
        added_members_by_name = [member_name, member_name_2]
        members = {member_name: member_age, member_name_2: member_age_2}
        expected = f"Successfully added: {', '.join(added_members_by_name)}"
        actual = team.add_member(**members)
        self.assertTrue(member_name in team.members)
        self.assertEqual(members, team.members)
        self.assertEqual(expected, actual)

    def test_add_members__when_name_in_team(self):
        team = Team("name")
        expected = f"Successfully added: {', '.join([])}"
        team.add_member(**{"name": 10})
        actual = team.add_member(**{"name": 10})
        self.assertEqual(expected, actual)

    def test_remove_member__when_name_in_team(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        expected = f"Member {member_name} removed"
        team.add_member(**{member_name: member_age})
        actual = team.remove_member(member_name)
        self.assertTrue(member_name not in team.members)
        self.assertEqual({}, team.members)
        self.assertEqual(expected, actual)

    def test_remove_member__when_name_not_in_team(self):
        team = Team("name")
        member_name = "member name"
        expected = f"Member with name {member_name} does not exist"
        actual = team.remove_member(member_name)
        self.assertEqual(expected, actual)

    def test_team_gt__when_team_two_is_smaller(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        team.add_member(**{member_name: member_age})
        team2 = Team("new")
        actual = team > team2
        self.assertEqual(True, actual)

    def test_team_gt__when_equal(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        team.add_member(**{member_name: member_age})
        team2 = Team("new")
        team2.add_member(**{member_name: member_age})
        actual = team > team2
        self.assertEqual(False, actual)

    def test_team_gt__when_team_two_is_bigger(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        team.add_member(**{member_name: member_age})
        team2 = Team("new")
        members = {member_name: member_age, "new": 30}
        team2.add_member(**members)
        actual = team2 > team
        self.assertEqual(True, actual)

    def test_team_add(self):
        team = Team("name")
        team.add_member(**{"member 1": 20})
        team2 = Team("new")
        team2.add_member(**{"member 2": 30})
        team3 = team + team2
        new_name = f"{team.name}{team2.name}"
        new_members = team.members
        new_members.update(team2.members)
        self.assertEqual(new_name, team3.name)
        self.assertEqual(new_members, team3.members)

    def test_team_len(self):
        team = Team("name")
        member_name = "member name"
        member_age = 10
        team.add_member(**{member_name: member_age})
        self.assertEqual(1, len(team))

    def test_team_str(self):
        team_name = "name"
        team = Team(team_name)
        team.add_member(**{"member1": 20})
        team.add_member(**{"member2": 30})
        members = {"member1": 20, "member2": 30}
        result = [f"Team name: {team_name}"]
        members = list(sorted(members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected = "\n".join(result)
        self.assertEqual(expected, str(team))


if __name__ == "__main__":
    unittest.main()
