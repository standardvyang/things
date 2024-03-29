# %%
import random
import statistics

# %%
# raw cardlist

raw_handlist = '''
Rank	Name	EV   	Win %	Tie %	Occur %	Cumulative %
1	AAo	0.70	84.93	0.54	0.45	0.45
2	KKo	0.64	82.11	0.55	0.45	0.90
3	QQo	0.59	79.63	0.58	0.45	1.35
4	JJo	0.54	77.15	0.63	0.45	1.80
5	TTo	0.50	74.66	0.70	0.45	2.26
6	99o	0.44	71.66	0.78	0.45	2.71
7	88o	0.38	68.71	0.89	0.45	3.16
8	AKs	0.34	66.21	1.65	0.30	3.46
9	77o	0.32	65.72	1.02	0.45	3.92
10	AQs	0.32	65.31	1.79	0.30	4.22
11	AJs	0.30	64.39	1.99	0.30	4.52
12	AKo	0.30	64.46	1.70	0.90	5.42
13	ATs	0.29	63.48	2.22	0.30	5.73
14	AQo	0.28	63.50	1.84	0.90	6.63
15	AJo	0.27	62.53	2.05	0.90	7.54
16	KQs	0.26	62.40	1.98	0.30	7.84
17	66o	0.26	62.70	1.16	0.45	8.29
18	A9s	0.25	61.50	2.54	0.30	8.59
19	ATo	0.25	61.56	2.30	0.90	9.50
20	KJs	0.25	61.47	2.18	0.30	9.80
21	A8s	0.23	60.50	2.87	0.30	10.10
22	KTs	0.23	60.58	2.40	0.30	10.40
23	KQo	0.22	60.43	2.04	0.90	11.31
24	A7s	0.21	59.38	3.19	0.30	11.61
25	A9o	0.21	59.44	2.64	0.90	12.51
26	KJo	0.21	59.44	2.25	0.90	13.42
27	55o	0.20	59.64	1.36	0.45	13.87
28	QJs	0.20	59.07	2.37	0.30	14.17
29	K9s	0.19	58.63	2.70	0.30	14.47
30	A5s	0.19	58.06	3.71	0.30	14.78
31	A6s	0.19	58.17	3.45	0.30	15.08
32	A8o	0.19	58.37	2.99	0.90	15.98
33	KTo	0.19	58.49	2.48	0.90	16.89
34	QTs	0.18	58.17	2.59	0.30	17.19
35	A4s	0.18	57.13	3.79	0.30	17.49
36	A7o	0.17	57.16	3.34	0.90	18.40
37	K8s	0.16	56.79	3.04	0.30	18.70
38	A3s	0.16	56.33	3.77	0.30	19.00
39	QJo	0.16	56.90	2.45	0.90	19.90
40	K9o	0.15	56.40	2.80	0.90	20.81
41	A5o	0.15	55.74	3.90	0.90	21.71
42	A6o	0.15	55.87	3.62	0.90	22.62
43	Q9s	0.15	56.22	2.88	0.30	22.92
44	K7s	0.15	55.84	3.38	0.30	23.22
45	JTs	0.15	56.15	2.74	0.30	23.52
46	A2s	0.14	55.50	3.74	0.30	23.83
47	QTo	0.14	55.94	2.68	0.90	24.73
48	44o	0.14	56.25	1.53	0.45	25.18
49	A4o	0.13	54.73	3.99	0.90	26.09
50	K6s	0.13	54.80	3.67	0.30	26.39
51	K8o	0.12	54.43	3.17	0.90	27.30
52	Q8s	0.12	54.41	3.20	0.30	27.60
53	A3o	0.11	53.85	3.97	0.90	28.50
54	K5s	0.11	53.83	3.91	0.30	28.80
55	J9s	0.11	54.11	3.10	0.30	29.11
56	Q9o	0.10	53.86	2.99	0.90	30.01
57	JTo	0.10	53.82	2.84	0.90	30.92
58	K7o	0.10	53.41	3.54	0.90	31.82
59	A2o	0.09	52.94	3.96	0.90	32.73
60	K4s	0.09	52.88	3.99	0.30	33.03
61	Q7s	0.08	52.52	3.55	0.30	33.33
62	K6o	0.08	52.29	3.85	0.90	34.23
63	K3s	0.08	52.07	3.96	0.30	34.53
64	T9s	0.08	52.37	3.30	0.30	34.84
65	J8s	0.08	52.31	3.40	0.30	35.14
66	33o	0.07	52.83	1.70	0.45	35.59
67	Q6s	0.07	51.67	3.86	0.30	35.89
68	Q8o	0.07	51.93	3.33	0.90	36.80
69	K5o	0.06	51.25	4.12	0.90	37.70
70	J9o	0.06	51.63	3.22	0.90	38.61
71	K2s	0.06	51.23	3.94	0.30	38.91
72	Q5s	0.05	50.71	4.11	0.30	39.21
73	T8s	0.04	50.50	3.65	0.30	39.51
74	K4o	0.04	50.22	4.20	0.90	40.42
75	J7s	0.04	50.45	3.74	0.30	40.72
76	Q4s	0.03	49.76	4.18	0.30	41.02
77	Q7o	0.03	49.90	3.72	0.90	41.93
78	T9o	0.03	49.81	3.43	0.90	42.83
79	J8o	0.02	49.71	3.55	0.90	43.74
80	K3o	0.02	49.33	4.18	0.90	44.64
81	Q6o	0.02	48.99	4.05	0.90	45.55
82	Q3s	0.02	48.93	4.16	0.30	45.85
83	98s	0.01	48.85	3.88	0.30	46.15
84	T7s	0.01	48.65	3.97	0.30	46.45
85	J6s	0.01	48.57	4.06	0.30	46.75
86	K2o	0.01	48.42	4.17	0.90	47.66
87	22o	0.00	49.38	1.89	0.45	48.11
88	Q2s	0.00	48.10	4.13	0.30	48.41
89	Q5o	0.00	47.95	4.32	0.90	49.32
90	J5s	0.00	47.82	4.33	0.30	49.62
91	T8o	0.00	47.81	3.80	0.90	50.52
92	J7o	0.00	47.72	3.91	0.90	51.43
93	Q4o	-0.01	46.92	4.40	0.90	52.33
94	97s	-0.01	46.99	4.25	0.30	52.63
95	J4s	-0.01	46.86	4.40	0.30	52.94
96	T6s	-0.02	46.80	4.28	0.30	53.24
97	J3s	-0.03	46.04	4.37	0.30	53.54
98	Q3o	-0.03	46.02	4.38	0.90	54.44
99	98o	-0.03	46.06	4.05	0.90	55.35
100	87s	-0.04	45.68	4.50	0.30	55.65
101	T7o	-0.04	45.82	4.15	0.90	56.56
102	J6o	-0.04	45.71	4.26	0.90	57.46
103	96s	-0.05	45.15	4.55	0.30	57.76
104	J2s	-0.05	45.20	4.35	0.30	58.06
105	Q2o	-0.05	45.10	4.37	0.90	58.97
106	T5s	-0.05	44.93	4.55	0.30	59.27
107	J5o	-0.05	44.90	4.55	0.90	60.18
108	T4s	-0.06	44.20	4.65	0.30	60.48
109	97o	-0.07	44.07	4.45	0.90	61.38
110	86s	-0.07	43.81	4.84	0.30	61.68
111	J4o	-0.07	43.86	4.63	0.90	62.59
112	T6o	-0.07	43.84	4.48	0.90	63.49
113	95s	-0.08	43.31	4.81	0.30	63.80
114	T3s	-0.08	43.37	4.62	0.30	64.10
115	76s	-0.09	42.82	5.08	0.30	64.40
116	J3o	-0.09	42.96	4.61	0.90	65.30
117	87o	-0.09	42.69	4.71	0.90	66.21
118	T2s	-0.10	42.54	4.59	0.30	66.51
119	85s	-0.10	41.99	5.10	0.30	66.81
120	96o	-0.11	42.10	4.77	0.90	67.72
121	J2o	-0.11	42.04	4.59	0.90	68.62
122	T5o	-0.11	41.85	4.78	0.90	69.53
123	94s	-0.12	41.40	4.90	0.30	69.83
124	75s	-0.12	40.97	5.39	0.30	70.13
125	T4o	-0.12	41.05	4.89	0.90	71.04
126	93s	-0.13	40.80	4.91	0.30	71.34
127	86o	-0.13	40.69	5.08	0.90	72.24
128	65s	-0.13	40.34	5.57	0.30	72.54
129	84s	-0.14	40.10	5.19	0.30	72.85
130	95o	-0.14	40.13	5.06	0.90	73.75
131	T3o	-0.14	40.15	4.87	0.90	74.66
132	92s	-0.15	39.97	4.88	0.30	74.96
133	76o	-0.15	39.65	5.33	0.90	75.86
134	74s	-0.16	39.10	5.48	0.30	76.16
135	T2o	-0.16	39.23	4.85	0.90	77.07
136	54s	-0.17	38.53	5.84	0.30	77.37
137	85o	-0.17	38.74	5.37	0.90	78.28
138	64s	-0.17	38.48	5.70	0.30	78.58
139	83s	-0.18	38.28	5.18	0.30	78.88
140	94o	-0.18	38.08	5.17	0.90	79.78
141	75o	-0.18	37.67	5.67	0.90	80.69
142	82s	-0.19	37.67	5.18	0.30	80.99
143	73s	-0.19	37.30	5.46	0.30	81.29
144	93o	-0.19	37.42	5.18	0.90	82.20
145	65o	-0.20	37.01	5.86	0.90	83.10
146	53s	-0.20	36.75	5.86	0.30	83.40
147	63s	-0.20	36.68	5.69	0.30	83.71
148	84o	-0.21	36.70	5.47	0.90	84.61
149	92o	-0.21	36.51	5.16	0.90	85.52
150	43s	-0.22	35.72	5.82	0.30	85.82
151	74o	-0.22	35.66	5.77	0.90	86.72
152	72s	-0.23	35.43	5.43	0.30	87.02
153	54o	-0.23	35.07	6.16	0.90	87.93
154	64o	-0.23	35.00	6.01	0.90	88.83
155	52s	-0.24	34.92	5.83	0.30	89.14
156	62s	-0.24	34.83	5.66	0.30	89.44
157	83o	-0.25	34.74	5.46	0.90	90.34
158	42s	-0.26	33.91	5.82	0.30	90.64
159	82o	-0.26	34.08	5.48	0.90	91.55
160	73o	-0.26	33.71	5.76	0.90	92.45
161	53o	-0.27	33.16	6.19	0.90	93.36
162	63o	-0.27	33.06	6.01	0.90	94.26
163	32s	-0.28	33.09	5.78	0.30	94.57
164	43o	-0.29	32.06	6.15	0.90	95.47
165	72o	-0.30	31.71	5.74	0.90	96.38
166	52o	-0.31	31.19	6.18	0.90	97.28
167	62o	-0.31	31.07	5.99	0.90	98.19
168	42o	-0.33	30.11	6.16	0.90	99.09
169	32o	-0.35	29.23	6.12	0.90	100.00
'''

# %%
def apply_chen_formulax(hand, data):
    score = 0
    '''
    Score your highest card only. Do not add any points for your lower card.
    A = 10 points.
    K = 8 points.
    Q = 7 points.
    J = 6 points.
    10 to 2 = 1/2 of card value. (e.g. a 6 would be worth 3 points)
    '''
    highest_card = hand[0]
    if highest_card == "A":
        score += 10
    elif highest_card == "K":
        score += 8
    elif highest_card == "Q":
        score += 7
    elif highest_card == "J":
        score += 6
    else:
        score += data["high_value"] / 2

    '''
    Multiply pairs by 2 of one card’s value. However, minimum score for a pair is 5.
    (e.g. KK = 16 points, 77 = 7 points, 22 = 5 points)
    '''
    if hand[0] == hand[1]:
        score = max(5, score * 2) 

    '''
    Add 2 points if cards are suited.
    '''
    if hand[2] == "s":
        score += 2

    '''
    Subtract points if there is a difference between the two cards.
    No difference = -0 points.
    1 card gap = -1 points.
    2 card gap = -2 points.
    3 card gap = -4 points.
    4 card gap or more = -5 points. (Aces are high this step, so hands like A2, A3 etc. have a 4+ gap.)
    '''
    difference = data["difference"]
    if difference <= 0:
        pass
    elif difference == 1:
        score -= 1
    elif difference == 2:
        score -= 2
    elif difference == 3:
        score -= 4
    else:
        score -= 5
    '''
    Add 1 point if there is a 0 or 1 card gap and both cards are lower than a Q. (e.g. JT, 75, 32 etc, this bonus point does not apply to pocket pairs)
    '''
    if difference <= 1 and hand[0] != hand[1]:
        if data["high_value"] < 12 and data["low_value"] < 12:
            score += 1

    '''
    Round half point scores up. (e.g. 7.5 rounds up to 8)
    '''
    score = round(score)
    return score




# %%
# cleaning data
handlist = raw_handlist.split('\n')[1:-1]
handlist = [x.split('\t') for x in handlist[1:]]

hands_dict = {card[1] : {"mrank" : int(card[0])} for card in handlist}
cards_value_transposition_values = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
}

for hand, data in hands_dict.items():
    data["high_value"] = cards_value_transposition_values[hand[0]]
    data["low_value"] = cards_value_transposition_values[hand[1]]
    data["sum_of_cards"] = data["high_value"] + data["low_value"]
    data["suited"] = hand[2] == "s"
    data["difference"] = abs(data["high_value"] - data["low_value"])
    data["gap"] = data["difference"] - 1
    data["chen_score"] = apply_chen_formulax(hand, data)

chen_scores = [data["chen_score"] for hand, data in hands_dict.items()]
chen_scores.sort(reverse=True)

chen_rank_differences = []
for hand, data in hands_dict.items():
    data["chen_rank"] = chen_scores.index(data["chen_score"]) + 1
    data["chen_rank_difference"] = abs(data["chen_rank"] - data["mrank"])
    chen_rank_differences.append(data["chen_rank_difference"])

print(sum(chen_rank_differences) / len(chen_rank_differences))
print(statistics.median(chen_rank_differences))


# %%
def get_custom_score(a,b,c,d,e=0):
    test_scores = []
    hand_data_sheet = {}

    for hand, data in hands_dict.items():
        
        # flush evaluation
        flush = 0
        if hand[2] == "s":
            flush = 1
        # straight evaluation
        straight = data["gap"]
        # pair evaluation
        pair = 0
        if hand[0] == hand[1]:
            pair = 1
        # high card evaluation
        high_card = data["high_value"] + data["low_value"]
        score = high_card*a + flush*b + straight*c + pair*d + data["chen_score"] * e

        test_scores.append(score)
        hand_data_sheet[hand] = {
            "cards": hand,
            "rank": data["mrank"],
            "score": score,
            "chen_rank" : data["chen_rank"],
            "chen_rank_difference" : data["chen_rank_difference"],
        }
    return (test_scores, hand_data_sheet)

def get_normalized_test_differences(test_scores, hand_data_sheet):
    differences = []
    test_scores.sort(reverse=True)

    for hand, data in hand_data_sheet.items():
        data["normalized test"] = test_scores.index(data["score"]) + 1
        data["difference"] = abs(data["normalized test"] - data["rank"])
        differences.append(data["difference"])

    return (differences, hand_data_sheet)


def test_custom_scoring_algorithm(a,b,c,d,e=0, to_print=False):
    (test_scores, hand_data_sheet) = get_custom_score(a,b,c,d,e)

    (differences, hand_data_sheet) = get_normalized_test_differences(test_scores, hand_data_sheet)

    scores = [round(data["score"]) for hand, data in hand_data_sheet.items()]
    if to_print == True:
        print(scores)
        print(len(scores))
        for hand, data in hand_data_sheet.items():
            pass
            # print(f"{hand}\t{data['rank']}\t{round(data['score'])}\t{data['normalized test']}\t{data['chen_rank_difference']}\t{data['difference']}")


    # biggest_difference = max(differences)
    mean_difference = sum(differences)/len(differences)
    # median_difference = statistics.median(differences)

    return mean_difference


# %%
bestscore = 6.25
weights = [2.9, 1.9, 1.1, 41.5, 1.7]


def upper(num):
    return num + 2.0
def lower(num):
    return num - 2.0



# %%
print(test_custom_scoring_algorithm(*weights, to_print=True))

# %%
a,b,c,d,e = [[int(upper(x)*10), int(lower(x)*10)] for x in weights]

for ia in range(a[1], a[0]):
    for ib in range(b[1], b[0]):
        for ic in range(c[1], c[0]):
            for id in range(d[1], d[0]):
                for ie in range(e[1], e[0]):
                    continue
                    score = test_custom_scoring_algorithm(ia*.1,ib*.1,ic*.1,id*.1,ie*.1)
                    if score < bestscore:
                        bestscore = score
                        bestweights = [ia*.1,ib*.1,ic*.1,id*.1,ie*.1]
                        print(f"New best score: {bestscore} with weights: {bestweights}")
                    else:
                        pass
                        # print(f"Score: {score} with weights: {i,j,k,l,m}")

# print(f"Best score: {bestscore} with weights: {bestweights}")



