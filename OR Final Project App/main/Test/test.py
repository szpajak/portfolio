import unittest

import numpy as np

from algorythm import Team, Fixtures, Genetic, Match

def dodaj(a, b):
    return a + b

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("FcBarcelona", 1.0, 0.98, "barceona.png")
        self.team2 = Team("WisłaKraków", 0.08, 0.5, "wisla.png")

    def test_get_team_weight(self):
        result = self.team1.get_team_weight()
        self.assertEqual(result, 1.0)

    def test_get_stadion_weight(self):
        result = self.team1.get_stadium_weight()
        self.assertEqual(result, 0.98)

    def test_team_not_equal(self):
        self.assertNotEqual(self.team1, self.team2)

class TestFixtures(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("FcBarcelona", 1.0, 0.98, "barceona.png")
        self.team2 = Team("WisłaKraków", 0.08, 0.5, "wisla.png")
        self.fixtures = Fixtures()
        self.fixtures.set_team_list([Team("FcBarcelona", 1.0, 0.98, "barceona.png"),
                                     Team("WisłaKraków", 0.08, 0.5, "wisla.png")])

    def test_PL_fixtures(self):
        self.fixtures.PL_fixtures(False)
        self.assertEqual(self.fixtures.first_game, [[Match(team1=Team("FcBarcelona", 1.0, 0.98, "barceona.png"), team2=Team("WisłaKraków", 0.08, 0.5, "wisla.png"))]])
        self.assertEqual(self.fixtures.rematch, [[Match(team1=Team("WisłaKraków", 0.08, 0.5, "wisla.png"), team2=Team("FcBarcelona", 1.0, 0.98, "barceona.png"))]])


    def test_initiate_match_times(self):
        self.fixtures.PL_fixtures(False)
        self.fixtures.initiate_match_times()
        self.assertEqual(self.fixtures.team_list[0].games_f, ["H", None, None, None, None, None, None, None,
                                                              None, None, None, None, None, None, None, None,
                                                              None, None, None])
        self.assertEqual(self.fixtures.team_list[1].games_f, ["A", None, None, None, None, None, None, None,
                                                              None, None, None, None, None, None, None, None,
                                                              None, None, None])
        self.assertEqual(self.fixtures.team_list[0].games_r, ["A", None, None, None, None, None, None, None,
                                                              None, None, None, None, None, None, None, None,
                                                              None, None, None])
        self.assertEqual(self.fixtures.team_list[1].games_r, ["H", None, None, None, None, None, None, None,
                                                              None, None, None, None, None, None, None, None,
                                                              None, None, None])

    def test_objective_fun(self):
        self.fixtures = Fixtures(np.array([[0, Match(fCost=10)],
                                           [Match(fCost=5), 0]]))
        result = self.fixtures.objective_function()
        self.assertEqual(result, 15)

    def test_penalty_fun(self):
        self.fixtures.team_list[0].set_games_f(["H", "H", "H", "H", None, None, None, None,
                                None, None, None, None, None, None, None, None,
                                None, None, None])
        result = self.fixtures.penalty_fun()
        self.assertEqual(result, 10000)

    def test_objective_fun2(self):
        self.fixtures = Fixtures(np.array([[0, Match(fCost=10)],
                                           [Match(fCost=5), 0]]))
        self.fixtures.team_list[0].set_games_f(["H", "H", "H", "H", None, None, None, None,
                                                None, None, None, None, None, None, None, None,
                                                None, None, None])
        result = self.fixtures.objective_function()
        self.assertEqual(result, 15-10000)



if __name__ == '__test__':
    unittest.main()
