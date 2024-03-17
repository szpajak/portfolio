import copy
import random
from random import shuffle
from typing import List, Tuple, TypeVar
import numpy as np
from itertools import combinations


#klasa druzyna opisuje jedna druzyne
class Team:
    def __init__(self, name: str, team_weight: float, stadium_weight: float, path: str):
        self.name = name
        self.games_f = [None for _ in range(19)]
        self.games_r = [None for _ in range(19)]
        self.t_w = team_weight
        self.s_w = stadium_weight
        self.path = path

    def set_games_f(self, game):
        self.games_f = game

    def get_team_weight(self) -> float:
        return self.t_w

    def get_stadium_weight(self) -> float:
        return self.s_w

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, Team):
            return self.name < other.name
        return NotImplemented

    def __hash__(self):
        return hash(self.name)

TeamType = TypeVar("TeamType", bound=Team)

#klasa Mecz opisuje parametry danego meczu
class Match:
    def __init__(self, fCost: int = 0, team1: TeamType = None, team2: TeamType = None,  time: str = None, rnd: int = None, stadion: float = None):
        # self.id = id
        self.fCost = fCost
        self.team1 = team1
        self.team2 = team2
        self.time = time
        self.rnd = rnd
        self.stadion = stadion

    def __repr__(self):
        return f"{self.team1}: {self.team2}: {self.rnd}: {self.fCost}: {self.time};"

    def __eq__(self, other):
        if isinstance(other, Match):
            return self.fCost == other.fCost
        return False


    def __lt__(self, other):
        if isinstance(other, Match):
            return self.fCost < other.fCost
        return NotImplemented

    def __hash__(self):
        return hash(self.fCost)

    def __add__(self, other):
        if isinstance(other, Match):
            return Match(self.fCost + other.fCost)
        elif isinstance(other, (int, float)):
            return Match(self.fCost + other)

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)


MatchType = TypeVar("MatchType", bound=Match)


# klasa Terminarza
class Fixtures:

    def __init__(self, Pl_fixtures_mat = None):
        self.first_game = None
        self.rematch = None
        self.team_list = [
        Team("Arsenal", 2.82, 0.60704, "arsenal.png"),                          # 0
        Team("Aston Villa", 0.35, 0.42530, "aston_villa.png"),                  # 1
        Team("Bournemouth", 0.08, 0.11307, "bournemouth.png"),                  # 2
        Team("Brentford", 0.05, 0.17250, "brentford.png"),                      # 3
        Team("Brighton", 0.18, 0.31876, "brighton.png"),                        # 4
        Team("Burnley", 0.07, 0.21744, "burnley.png"),                          # 5
        Team("Chelsea", 4.14, 0.40173, "chelsea.png"),                          # 6
        Team("CrystalPalace", 0.18, 0.25486, "crystal_palace.png"),             # 7
        Team("Everton", 0.3, 0.39414, "everton.png"),                           # 8
        Team("Fulham", 0.1, 0.24500, "fulham.png"),                             # 9
        Team("Liverpool", 4.36, 0.61276, "liverpool.png"),                      # 10
        Team("Luton", 0.04, 0.11500, "luton.png"),                              # 11
        Team("ManchesterCity", 4.94, 0.53400, "manchester_city.png"),           # 12
        Team("ManchesterUnited", 6.31, 0.74031, "manchester_united.png"),       # 13
        Team("NewcastleUnited", 0.25, 0.52257, "newcastle.png"),                # 14
        Team("Nottingham", 0.1, 0.30404, "nottingham.png"),                     # 15
        Team("Sheffield", 0.07, 0.32050, "sheffield.png"),                      # 16
        Team("TottenhamHotspur", 1.65, 0.62850, "tottenham.png"),               # 17
        Team("WestHamUnited", 0.41, 0.62500, "west_ham.png"),                   # 18
        Team("WolverhamptonWanderers", 0.26, 0.31750, "wolves.png"),            # 19
    ]
        if Pl_fixtures_mat is None:
            self.Pl_fixtures_mat = np.zeros((len(self.team_list), len(self.team_list)), dtype=object)
        else:
            self.Pl_fixtures_mat = Pl_fixtures_mat

    def set_team_list(self, team_list):
        self.team_list = team_list

    def PL_fixtures(self, exist): #-> Tuple[List[List[MatchType]], List[List[MatchType]]]:
        if exist is False:
            n = len(self.team_list)
            matches = []
            fixtures = []
            return_matches = []
            for fixture in range(1, n):
                for i in range(n // 2):
                    #tutaj doajemy mecze zamiast samych par drużyn
                    m1 = Match(team1=self.team_list[i], team2=self.team_list[n - 1 - i])
                    m2 = Match(team1=self.team_list[n - 1 - i], team2=self.team_list[i])
                    matches.append(m1)
                    return_matches.append(m2)
                self.team_list.insert(1, self.team_list.pop())
                fixtures.insert(len(fixtures) // 2, matches)
                fixtures.append(return_matches)
                matches = []
                return_matches = []

            self.first_game = fixtures[slice(0, n * 2 - 1, 2)]
            self.rematch = fixtures[slice(1, n * 2, 2)]
            shuffle(self.first_game)
            shuffle(self.rematch)
        else:
            # w parametrze teams podajemy macierz i dzieli na first_game i rematch
            for idx1, idx2 in self.copy_idx:
                f_game = self.Pl_fixtures_mat[idx1][idx2].rnd
                r_game = self.Pl_fixtures_mat[idx2][idx1].rnd
                if f_game <= 19 < r_game:
                    self.team_list[idx1].games_f[f_game - 1], self.team_list[idx2].games_f[f_game - 1] = \
                    self.team_list[idx2].games_f[f_game - 1], self.team_list[idx1].games_f[f_game - 1]
                    self.team_list[idx1].games_r[r_game - 20], self.team_list[idx2].games_r[r_game - 20] = \
                    self.team_list[idx2].games_r[r_game - 20], self.team_list[idx1].games_r[r_game - 20]
                elif r_game <= 19 < f_game:
                    self.team_list[idx1].games_f[f_game - 20], self.team_list[idx2].games_f[f_game - 20] = \
                        self.team_list[idx2].games_f[f_game - 20], self.team_list[idx1].games_f[f_game - 20]
                    self.team_list[idx1].games_r[r_game - 1], self.team_list[idx2].games_r[r_game - 1] = \
                        self.team_list[idx2].games_r[r_game - 1], self.team_list[idx1].games_r[r_game - 1]

                elif r_game <= 19 and f_game <= 19:
                    self.team_list[idx1].games_f[f_game - 1], self.team_list[idx2].games_f[f_game - 1] = \
                        self.team_list[idx2].games_f[f_game - 1], self.team_list[idx1].games_f[f_game - 1]
                    self.team_list[idx1].games_r[r_game - 1], self.team_list[idx2].games_r[r_game - 1] = \
                        self.team_list[idx2].games_r[r_game - 1], self.team_list[idx1].games_r[r_game - 1]

                elif r_game > 19 and f_game > 19:
                    self.team_list[idx1].games_f[f_game - 20], self.team_list[idx2].games_f[f_game - 20] = \
                        self.team_list[idx2].games_f[f_game - 20], self.team_list[idx1].games_f[f_game - 20]
                    self.team_list[idx1].games_r[r_game - 20], self.team_list[idx2].games_r[r_game - 20] = \
                        self.team_list[idx2].games_r[r_game - 20], self.team_list[idx1].games_r[r_game - 20]

    # Funkcje zrobione pod mutacje -> do krzyżowania inna funkcja
    # do mutate1 - zmiana gospodarza
    def match_times_update(self, changes):
        self.idx = list(combinations(list(range(20)), 2))
        self.idx_pairs = random.sample(self.idx, int(changes*len(self.idx)))
        self.copy_idx = self.idx_pairs.copy()
        for i1, j1 in self.idx_pairs:

            # zamiana gosc-gospodarz
            self.Pl_fixtures_mat[i1][j1].time, self.Pl_fixtures_mat[j1][i1].time = self.Pl_fixtures_mat[j1][i1].time, self.Pl_fixtures_mat[i1][j1].time
            self.Pl_fixtures_mat[i1][j1].rnd, self.Pl_fixtures_mat[j1][i1].rnd = self.Pl_fixtures_mat[j1][i1].rnd, self.Pl_fixtures_mat[i1][j1].rnd
            self.Pl_fixtures_mat[i1][j1].stadion, self.Pl_fixtures_mat[j1][i1].stadion = self.Pl_fixtures_mat[j1][i1].stadion, self.Pl_fixtures_mat[i1][j1].stadion

        self.PL_fixtures(exist=True)
        self.complete_the_cost_matrix(exist=True)

    # do mutate2 - zmiana godzin w 1. części sezonu
    def match_times_update2(self, changes):
        i = 0
        f_m = lambda wi, wj, si, hk, rl: wi * wj * si * hk * rl

        self.weight_time2 = {"0SOB_13:30": 50, "1SOB1_16:00": 5, "2SOB2_16:00": 5, "3SOB3_16:00": 5, "4SOB4_16:00": 5,
                             "5SOB5_16:00": 5, "6SOB_18:30": 80, "7NIE_15:00": 20, "8NIE_17:30": 60, "9PON_21:00": 10}

        weights = [(15, 5), (12, 5), (10, 5), (7, 5), (10, 5), (15, 5), (25, 5), (20, 3)]

        rw_list = [weight for weight, count in weights for _ in range(count)]
        self.round_weight = {index: value for index, value in enumerate(rw_list)}

        while changes > i:
            time_to_change = np.random.choice(self.first_game[i], 2, replace=False)

            time_to_change[0].time, time_to_change[1].time = time_to_change[1].time, time_to_change[0].time
            time_to_change[0].fCost = f_m(time_to_change[0].team1.t_w, time_to_change[0].team2.t_w, time_to_change[0].stadion, self.weight_time2[time_to_change[0].time], self.round_weight[time_to_change[0].rnd-1])
            time_to_change[1].fCost = f_m(time_to_change[1].team1.t_w, time_to_change[1].team2.t_w,
                                          time_to_change[1].stadion, self.weight_time2[time_to_change[1].time],
                                          self.round_weight[time_to_change[1].rnd - 1])

            i += 1
            if i > 19:
                changes -= 19
                i = 0

    # do mutate3 - zmiana godzin w 2. części sezonu
    def match_times_update3(self, changes):
        i = 0

        f_m = lambda wi, wj, si, hk, rl: wi * wj * si * hk * rl

        self.weight_time2 = {"0SOB_13:30": 50, "1SOB1_16:00": 5, "2SOB2_16:00": 5, "3SOB3_16:00": 5, "4SOB4_16:00": 5,
                             "5SOB5_16:00": 5, "6SOB_18:30": 80, "7NIE_15:00": 20, "8NIE_17:30": 60, "9PON_21:00": 10}

        weights = [(15, 5), (12, 5), (10, 5), (7, 5), (10, 5), (15, 5), (25, 5), (20, 3)]

        rw_list = [weight for weight, count in weights for _ in range(count)]
        self.round_weight = {index: value for index, value in enumerate(rw_list)}

        while changes > i:
            time_to_change = np.random.choice(self.rematch[i], 2, replace=False)
            time_to_change[0].time, time_to_change[1].time = time_to_change[1].time, time_to_change[0].time
            time_to_change[0].fCost = f_m(time_to_change[0].team1.t_w, time_to_change[0].team2.t_w,
                                          time_to_change[0].stadion, self.weight_time2[time_to_change[0].time],
                                          self.round_weight[time_to_change[0].rnd - 1])
            time_to_change[1].fCost = f_m(time_to_change[1].team1.t_w, time_to_change[1].team2.t_w,
                                          time_to_change[1].stadion, self.weight_time2[time_to_change[1].time],
                                          self.round_weight[time_to_change[1].rnd - 1])
            i += 1
            if i > 19:
                changes -= 19
                i = 0

    # do mutate4 - zmiana kolejki
    def match_times_update4(self):
        f_m = lambda wi, wj, si, hk, rl: wi * wj * si * hk * rl

        self.weight_time2 = {"0SOB_13:30": 50, "1SOB1_16:00": 5, "2SOB2_16:00": 5, "3SOB3_16:00": 5, "4SOB4_16:00": 5,
                             "5SOB5_16:00": 5, "6SOB_18:30": 80, "7NIE_15:00": 20, "8NIE_17:30": 60, "9PON_21:00": 10}

        weights = [(15, 5), (12, 5), (10, 5), (7, 5), (10, 5), (15, 5), (25, 5), (20, 3)]

        rw_list = [weight for weight, count in weights for _ in range(count)]
        self.round_weight = {index: value for index, value in enumerate(rw_list)}

        random_rnd_indices = random.sample(range(len(self.first_game)), 2)
        self.first_game[random_rnd_indices[0]], self.first_game[random_rnd_indices[1]] = self.first_game[random_rnd_indices[1]], self.first_game[random_rnd_indices[0]]

        for game in self.first_game[random_rnd_indices[1]]:

            game.rnd = random_rnd_indices[1] + 1
            game.fCost = f_m(game.team1.t_w, game.team2.t_w, game.stadion, self.weight_time2[game.time], self.round_weight[random_rnd_indices[1]])
            game.team1.games_f[random_rnd_indices[1]] = "H"
            game.team2.games_f[random_rnd_indices[1]] = "A"

        for game in self.first_game[random_rnd_indices[0]]:
            game.rnd = random_rnd_indices[0] + 1
            game.fCost = f_m(game.team1.t_w, game.team2.t_w, game.stadion, self.weight_time2[game.time],
                             self.round_weight[random_rnd_indices[0]])
            game.team1.games_f[random_rnd_indices[0]] = "H"
            game.team2.games_f[random_rnd_indices[0]] = "A"

        random_rnd_indices2 = random.sample(range(len(self.rematch)), 2)

        self.rematch[random_rnd_indices2[0]], self.rematch[random_rnd_indices2[1]] = self.rematch[
                                                                                             random_rnd_indices2[1]], \
                                                                                         self.rematch[
                                                                                             random_rnd_indices2[0]]

        for game in self.rematch[random_rnd_indices2[1]]:
            game.rnd = random_rnd_indices2[1] + 20
            game.fCost = f_m(game.team1.t_w, game.team2.t_w, game.stadion, self.weight_time2[game.time],
                             self.round_weight[random_rnd_indices2[1]])
            game.team1.games_r[random_rnd_indices[1]] = "H"
            game.team2.games_r[random_rnd_indices[1]] = "A"

        for game in self.rematch[random_rnd_indices2[0]]:
            game.rnd =random_rnd_indices2[0] + 20
            game.fCost = f_m(game.team1.t_w, game.team2.t_w, game.stadion, self.weight_time2[game.time],
                             self.round_weight[random_rnd_indices2[0]])
            game.team1.games_r[random_rnd_indices[0]] = "H"
            game.team2.games_r[random_rnd_indices[0]] = "A"

    def get_first_rematch(self):
        return self.first_game, self.rematch

    def set_first(self, f_game):
        self.first_game = f_game

    def set_rematch(self, r_game):
        self.rematch = r_game

    def child_game_update(self):
        for i, r in enumerate(self.first_game):
            for j, match in enumerate(r):
                match.team1.games_f[i] = "H"
                match.team2.games_f[i] = "A"
                match.time = self.first_game[i][j].time
                match.stadion = match.team1.s_w
                match.rnd = self.first_game[i][j].rnd
                match.fCost = self.first_game[i][j].fCost
                self.Pl_fixtures_mat[self.team_list.index(match.team1)][self.team_list.index(match.team2)] = match

        for i, r in enumerate(self.rematch):
            for j, match in enumerate(r):
                match.team1.games_r[i] = "H"
                match.team2.games_r[i] = "A"
                match.time = self.rematch[i][j].time
                match.stadion = match.team1.s_w
                match.rnd = self.rematch[i][j].rnd
                match.fCost = self.rematch[i][j].fCost
                self.Pl_fixtures_mat[self.team_list.index(match.team1)][self.team_list.index(match.team2)] = match

    def initiate_match_times(self): #-> Tuple[List[List[MatchType]], List[List[MatchType]]]:

        self.weight_time = {0: ("0SOB_13:30", 50), 1: ("1SOB1_16:00", 5), 2: ("2SOB2_16:00", 5), 3: ("3SOB3_16:00", 5), 4: ("4SOB4_16:00", 5),
                  5: ("5SOB5_16:00", 5), 6: ("6SOB_18:30", 80), 7: ("7NIE_15:00", 20), 8: ("8NIE_17:30", 60), 9: ("9PON_21:00", 10)}

        self.weight_time2 = {"0SOB_13:30": 50, "1SOB1_16:00": 5, "2SOB2_16:00": 5, "3SOB3_16:00": 5, "4SOB4_16:00": 5,
                             "5SOB5_16:00": 5, "6SOB_18:30": 80, "7NIE_15:00" : 20, "8NIE_17:30": 60, "9PON_21:00": 10}

        self.weight_time_lst = [i for i in range(10)]

        for i, r in enumerate(self.first_game):
            shuffle(self.weight_time_lst)
            for j, match in enumerate(r):
                match.team1.games_f[i] = "H"
                match.team2.games_f[i] = "A"
                match.time = self.weight_time[self.weight_time_lst[j]][0]
                match.stadion = match.team1.s_w

        for j, r in enumerate(self.rematch):
            shuffle(self.weight_time_lst)
            for k, match in enumerate(r):
                match.team1.games_r[j] = "H"
                match.team2.games_r[j] = "A"
                match.time = self.weight_time[self.weight_time_lst[k]][0]
                match.stadion = match.team1.s_w

        #return self.first_game, self.rematch

    def complete_the_cost_matrix(self, exist):
        # funkcja liczaca wage jednego spotkania
        f_m = lambda wi, wj, si, hk, rl: wi * wj * si * hk * rl

        # wymieramy co 5 kolejek i zmienamy ich wagi
        weights = [(15, 5), (12, 5), (10, 5), (7, 5), (10, 5), (15, 5), (25, 5), (20, 3)]

        rw_list = [weight for weight, count in weights for _ in range(count)]
        self.round_weight = {index: value for index, value in enumerate(rw_list)}

        self.weight_time2 = {"0SOB_13:30": 50, "1SOB1_16:00": 5, "2SOB2_16:00": 5, "3SOB3_16:00": 5, "4SOB4_16:00": 5,
                             "5SOB5_16:00": 5, "6SOB_18:30": 80, "7NIE_15:00": 20, "8NIE_17:30": 60, "9PON_21:00": 10}

        if not exist:
            for i, r in enumerate(self.first_game):
                for j, match in enumerate(r):
                    match.rnd = i+1 #można pomyśleć czy nie i+1???
                    match.fCost = f_m(match.team1.t_w, match.team2.t_w, match.stadion, self.weight_time2[match.time], self.round_weight[i])
                    self.Pl_fixtures_mat[self.team_list.index(match.team1)][self.team_list.index(match.team2)] = match


            for i, r in enumerate(self.rematch):
                for j, match in enumerate(r):
                    match.rnd = i+20  # można pomyśleć czy nie i+1???
                    match.fCost = f_m(match.team1.t_w, match.team2.t_w, match.stadion, self.weight_time2[match.time], self.round_weight[i])
                    self.Pl_fixtures_mat[self.team_list.index(match.team1)][self.team_list.index(match.team2)] = match

        else:
            for i, j in self.copy_idx:
                self.Pl_fixtures_mat[i][j].fCost = f_m(self.team_list[i].t_w, self.team_list[j].t_w, self.Pl_fixtures_mat[i][j].stadion, self.weight_time2[self.Pl_fixtures_mat[i][j].time],
                                     self.round_weight[self.Pl_fixtures_mat[i][j].rnd-1])
                self.Pl_fixtures_mat[j][i].fCost = f_m(self.team_list[i].t_w, self.team_list[j].t_w, self.Pl_fixtures_mat[j][i].stadion,
                                                           self.weight_time2[self.Pl_fixtures_mat[j][i].time],
                                                           self.round_weight[self.Pl_fixtures_mat[j][i].rnd-1])

    def penalty_fun(self):
        three_home_game_in_row = 0
        for match in self.first_game[0]:
            for i in range(len(match.team1.games_f) - 3):
                if match.team1.games_f[i] == match.team1.games_f[i + 1] == match.team1.games_f[i + 2] == match.team1.games_f[i + 3] == "H":
                    three_home_game_in_row += 1
                if match.team1.games_r[i] == match.team1.games_r[i + 1] == match.team1.games_r[i + 2] == match.team1.games_r[i + 3] == "H":
                    three_home_game_in_row += 1
                if match.team2.games_f[i] == match.team2.games_f[i + 1] == match.team2.games_f[i + 2] == match.team2.games_f[i + 3] == "H":
                    three_home_game_in_row += 1
                if match.team2.games_r[i] == match.team2.games_r[i + 1] == match.team2.games_r[i + 2] == match.team2.games_r[i + 3] == "H":
                    three_home_game_in_row += 1
        return three_home_game_in_row * 1000

    def objective_function(self):
        sum = np.sum(self.Pl_fixtures_mat)
        return sum.fCost - self.penalty_fun()

    def __getitem__(self, item):
        return self.Pl_fixtures_mat[item]

    def __eq__(self, other):
        if isinstance(other, Fixtures):
            return np.where(self.Pl_fixtures_mat == other.Pl_fixtures_mat, self.Pl_fixtures_mat, np.nan) #można by też porównywać id, ale chyba bez sensu
        return False

    def __lt__(self, other):
        if isinstance(other, Fixtures):
            return self.objective_function() < other.objective_function()
        return NotImplemented

    def __repr__(self):
        return f"{self.objective_function()}"


class Genetic:
    def __init__(self, population_size: int, generation_size: int):
        self.population = [None for _ in range(population_size)]
        self.parents = [None for _ in range(population_size//5)]
        self.population_size = population_size
        self.parents_size = population_size//5
        self.generation_size = generation_size

    def create_population(self):
        for i in range(len(self.population)):
            fixtures = Fixtures()
            fixtures.PL_fixtures(False)
            fixtures.initiate_match_times()
            fixtures.complete_the_cost_matrix(0)
            self.population[i] = fixtures

    def tournament_selection(self, tournament_size, elite_percent):
        if self.parents[0] is None:
            self.parents = random.sample(self.population, self.parents_size)
        else:
            new_parents = []

            for _ in range(len(self.parents)):
                winner = max(random.sample(self.population, tournament_size))
                new_parents.append(winner)

            elite = sorted(self.parents, reverse=True)[:int(elite_percent*len(self.parents))]
            new_parents = elite + new_parents
            new_parents = sorted(new_parents, reverse=True)[:len(self.parents)]
            shuffle(new_parents)
            self.parents = new_parents.copy()

            self.population = self.parents + self.population

    def ranking_selection(self, ranking_size, elite_percent):
        if self.parents[0] is None:
            self.parents = random.sample(self.population, self.parents_size)
        else:
            new_parents = []
            sorted_parents = sorted(self.parents, reverse=True)

            for i in range(len(self.parents)):
                new_parents.append(sorted_parents[i])
            elite = sorted(self.parents, reverse=True)[:int(elite_percent * len(self.parents))]
            new_parents = elite + new_parents
            new_parents = sorted(new_parents, reverse=True)[:len(self.parents)]
            shuffle(new_parents)
            self.parents = new_parents.copy()

            self.population = self.parents + self.population

    def cross(self):
        possible_parents = list(combinations(self.parents, 2))
        possible_parents = random.sample(possible_parents, self.parents_size) #daje ci listę z tyloma kombinacjami ile ma być potomków

        self.child_lst = [None for _ in range(len(possible_parents)*2)]
        i = 0
        for parent1, parent2 in possible_parents:
            parent1_first, parent1_rematch = parent1.get_first_rematch()
            parent2_first, parent2_rematch = parent2.get_first_rematch()
            new_child1 = Fixtures()
            new_child2 = Fixtures()

            new_child1.set_first(parent1_first)
            new_child1.set_rematch(parent2_rematch)
            new_child1.child_game_update()
            # print(new_child1.team_list[0].games_f)
            # new_child1.initiate_match_times()
            # new_child1.complete_the_cost_matrix(0)
            new_child2.set_first(parent2_first)
            new_child2.set_rematch(parent1_rematch)
            new_child2.child_game_update()
            # new_child2.initiate_match_times()
            # new_child2.complete_the_cost_matrix(0)
            self.child_lst[i] = new_child1
            self.child_lst[i+1] = new_child2
            i += 2
        self.population += self.child_lst
        self.population = sorted(self.population, reverse=True)
        self.population = self.population[:self.population_size]

    def remove_from_array(self, base_array, test_array):
        for index in range(len(base_array)):
            if np.array_equal(base_array[index].Pl_fixtures_mat, test_array.Pl_fixtures_mat):
                base_array.pop(index)
                break
        return base_array

    # DO WSZYSTKICH MUTACJI
    # percent_muted -> jaką część populacji chcemy mutować;
    # mute_rate -> jak bardzo mutujemy osobnika

    # zamiana gospodarza
    def mutate1(self, percent_muted, mut_rate):

        temp_population = self.population.copy()
        percent_muted = self.population_size * percent_muted #do funkcji podajemy w procentach: 0.5, 0.25 itp.
        to_be_mutated = random.sample(temp_population, int(percent_muted))


        for mat in to_be_mutated:
            temp_population = self.remove_from_array(temp_population, mat)
            mat.match_times_update(mut_rate)
            temp_population.append(mat)

        self.population = temp_population

    #zamiana godziny meczow w pierwszej czesci sezonu
    def mutate2(self, percent_muted, mut_rate):
        temp_population = self.population.copy()
        percent_muted = self.population_size * percent_muted  # do funkcji podajemy w procentach: 0.5, 0.25 itp.
        to_be_mutated = random.sample(temp_population, int(percent_muted))

        for mat in to_be_mutated:
            temp_population = self.remove_from_array(temp_population, mat)
            mat.match_times_update2(mut_rate*38)
            temp_population.append(mat)

        self.population = temp_population

    # zamiana godziny meczow w drugiej czesci sezonu
    def mutate3(self, percent_muted, mut_rate):
        temp_population = self.population.copy()
        percent_muted = self.population_size * percent_muted  # do funkcji podajemy w procentach: 0.5, 0.25 itp.
        to_be_mutated = random.sample(temp_population, int(percent_muted))

        for mat in to_be_mutated:
            temp_population = self.remove_from_array(temp_population, mat)
            mat.match_times_update3(mut_rate*38)
            temp_population.append(mat)

        self.population = temp_population

    # zamiana kolejki
    def mutate4(self, percent_muted):
        temp_population = self.population.copy()
        percent_muted = self.population_size * percent_muted  # do funkcji podajemy w procentach: 0.5, 0.25 itp.
        to_be_mutated = random.sample(temp_population, int(percent_muted))

        for mat in to_be_mutated:
            temp_population = self.remove_from_array(temp_population, mat)
            mat.match_times_update4()
            temp_population.append(mat)

        self.population = temp_population

    def __iter__(self):
        return iter(self.population)

    def __repr__(self):
        return f"{self.parents}"


class Population:
    def finish(self, population_size, generation_size, tournament_size, tournament_type, elite_percent, mut_type, percent_muted, mut_rate):
        try:
            Genn = Genetic(population_size, generation_size)
            Genn.create_population()
            best_result = [None for _ in range(Genn.generation_size)]
            best_result[0] = max(Genn.population)
            # print(best_result)
            if tournament_type == "Tournament":
                Genn.tournament_selection(tournament_size, elite_percent)
            elif tournament_type == "Ranking":
                Genn.ranking_selection(tournament_size, elite_percent)
            Genn.cross()
            for i in range(1, Genn.generation_size):
                new_gen = copy.deepcopy(Genn)
                if tournament_type == "Tournament":
                    new_gen.tournament_selection(tournament_size, elite_percent)
                elif tournament_type == "Ranking":
                    new_gen.ranking_selection(tournament_size, elite_percent)
                new_gen.cross()
                if "Host" in mut_type:
                    new_gen.mutate1(percent_muted, mut_rate)
                if "Round" in mut_type:
                    new_gen.mutate4(percent_muted)
                if "Hour1" in mut_type:
                    new_gen.mutate2(percent_muted, mut_rate)
                if "Hour2" in mut_type:
                    new_gen.mutate3(percent_muted, mut_rate)
                best_result[i] = max(new_gen.population)
                # print(best_result)
                Genn = new_gen
                print(best_result)
                del new_gen

            self.each_iter_best = best_result
            self.best_fix = max(best_result) # do gui
            self.best = round(self.best_fix.objective_function(),2)
            self.all_generation = best_result

            return True

        except:
            return False


if __name__ == "__main__":
    # Lista drużyn w Premier League

    a = Fixtures()

    a.PL_fixtures(False)
    a.initiate_match_times()
    a.complete_the_cost_matrix(0)
    a.penalty_fun()
    a.objective_function()
    pp = Population()
    pp.finish(population_size=20, generation_size=30, tournament_size=5, tournament_type="Ranking",
              elite_percent=0.1, mut_type=["Round"], percent_muted=0.2, mut_rate=0.3)

    posortowana_lista = sorted(pp.best_fix.first_game[0], key=lambda x: x.time)
    # G.cross()

