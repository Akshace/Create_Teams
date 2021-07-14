#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: Akshat Arvind (aarvind), Aniket Kale (ankale), Rahul Shamdasani (rshamdas)
#
# Based on skeleton code by R. Shah and D. Crandall, January 2021

import time
import pandas as pd
import numpy as np
import sys
import random
import heapq


def calculate_complains(team_members, pref, dontwant):
    # Complains is initialized to 0
    size_complains = 0
    pref_complains = 0
    dontwant_complains = 0

    # team_members=team.split('-')

    for names in team_members:
        # print("****")
        # print("current team in consideration is")
        # print(names)

        requested = pref[names]
        current_pref = pref[names]

        # print(names, "requeste teams to be", requested)
        # print(names, "requeste teams to be", requested)

        # Checking the team size and incrementing complains
        if (len(requested) != len(team_members)):
            # print("team complain incrementef for", requested, names)
            size_complains += 1

        # Calculating complains based on pref
        for curr_names in requested:
            if (curr_names not in team_members and curr_names != "zzz"):
                # print("incrementingfor" , curr_names)
                pref_complains += 1

        # Calculating complains for dont want to work with
        current_dontwant = dontwant[names]
        for cur_names_dontwant in current_dontwant:
            if (cur_names_dontwant in team_members):
                dontwant_complains += 2

    # print("complains for team size are ", size_complains)
    # print("complains for pref is ", pref_complains)
    # print("complains for dont want is ", dontwant_complains)
    return size_complains + pref_complains + dontwant_complains


## This function executes after the while loop and pops the least complain group allotment
def solve(ent):
    latest = heapq.heappop(ent)
    groups = []
    optimal = {}
    for group in latest[1]:
        strng = '-'.join(group)
        groups.append(strng)
    optimal['assigned-groups'] = groups
    optimal['total-cost'] = latest[0]
    print(optimal)
    return [optimal]
    # yield ({"assigned-groups": ["vibvats-djcran-zkachwal", "shah12", "vrmath"],
    #         "total-cost": 12})
    #
    # # Then we think a while and return another solution:
    # time.sleep(10)
    # yield ({"assigned-groups": ["vibvats-djcran-zkachwal", "shah12-vrmath"],
    #         "total-cost": 10})
    # while True:
    #     print("here")
    #     yield ({"assigned-groups": ["vibvats-djcran", "zkachwal-shah12-vrmath"],
    #             "total-cost": 9})


def solver(inpfile):
    ent = []
    t_end = time.time() + 20
    while time.time() < t_end:  # Timed While loop set to 20 seconds
        file = open(inpfile, "r")
        data = []

        for entry in file:
            s = entry.split()
            data.append(s)
        # print(data)

        pref = {}
        dontwant = {}
        "Step1: Reading input file"
        "converting it to a python dictionary"
        "key=>user (who is filling the preference)"

        with open(inpfile, 'r') as file:
            for line in file:
                row = line.split()
                pref[row[0]] = row[1].split('-')
                dontwant[row[0]] = row[2].split(',')

        users = []
        for i in data:
            users.append(i[0])
        # print(users)

        map = {}  # Creating a map to store point allotment for users corresponding to concerned user.
        for i in range(0, len(users)):
            score = []
            for j in range(0, len(users)):
                if users[j] in data[i][1] and len(list(data[i][1].split("-"))) == 1:  # User wants to work alone.
                    #         map[users[i]] = random.randint(9,10)
                    score.append(random.randint(9, 10))
                elif users[j] in data[i][1] and len(list(data[i][1].split("-"))) in [2,
                                                                                     3]:  # User wanted in a team of 2 or 3
                    score.append(random.randint(6, 8))
                elif users[j] in data[i][2]:  # If in the 2nd column, the user is not wanted so low score
                    score.append(random.randint(0, 2))
                else:
                    score.append(random.randint(3, 5))
            map[users[i]] = score
        # print(map)

        df = pd.DataFrame.from_dict(map, orient='index').T
        A = df.corr()  # Creating a correlation matrix using pandas datarame
        l1 = []
        visited = []
        for k in users[0:len(users)]:
            l2 = []
            for i in users:
                if A[k].get(i) > np.average(A[k]) and i not in visited and len(l2) < 3:
                    visited.append(i)
                    l2.append(i)
            if len(l2) > 0:
                l1.append(l2)
        # print(l1)
        complains = 0
        for curr_team in l1:
            complains += calculate_complains(curr_team, pref, dontwant)
        # print("Total complains", complains)
        heapq.heappush(ent, (complains, l1))
        heapq.heapify(ent)
        # print(ent)
    ret = solve(ent)
    return ret


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        raise (Exception("Error: expected an input filename"))

    for result in solver(sys.argv[1]):
        print(type(result))
        print("----- Latest solution:\n" + "\n".join(result['assigned-groups']))
        print("\nAssignment cost: %d \n" % result['total-cost'])
