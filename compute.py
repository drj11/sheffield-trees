#!/usr/bin/env python3

import csv

with open("cleanup.csv") as f:
    responses = 0
    households = 0
    agree = 0
    disagree = 0
    for i,row in enumerate(csv.reader(f), start=1):
        if i == 1:
            continue
        if 'Totals' in row:
            continue
        scores = list(map(int, row[2:6]))
        if scores[2] + scores[3] > scores[0]:
            print("REJECT Row {}: agree + disagree exceeds responses".format(i))
            print(",".join(row))
            continue
        responses += scores[0]
        households += scores[1]
        agree += scores[2]
        disagree += scores[3]
        if scores[1] <= 2:
            print(i, row)

    print("responses", responses)
    print("households", households)
    print("agree", agree)
    print("disagree", disagree)
