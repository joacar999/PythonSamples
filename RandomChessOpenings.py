###########################################################################
# Chess openings when I play white - give random suggestion
###########################################################################
# Author: Jocke C
# Copyright: No copyright. Similar programs can be found all over internet
# Email: joakim.carlsson@conciliodesign.se
###########################################################################
import random

# List of chess openings with their weights # The more common the opening, the higher the weight
# The rare/odd ones shall be presented less often
openings = [
    "e4 Opening - Ruy Lopez (Spanish Game)",
    "e4 Opening - Italian Game",
    "e4 Opening - King's Gambit",
    "e4 Opening - Vienna Game",
    "d4 Opening - Queen's Gambit",
    "d4 Opening - London System",
    "d4 Opening - Reti Opening",
    "English Opening",
    "Bird's Opening",
    "a rare one - Alapin Variation",
    "a rare one - Catalan Opening",
    "a rare one - Four Knights Game"
]
# Weights for each opening. The rare/odd ones shall be presented less often
weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 2]

random_opening = random.choices(openings, weights=weights, k=1)
if random_opening:
    print(f"==============================================================")
    print(f"For next Chessgame as white, choose opening : {random_opening}")
    print(f"==============================================================")
else:
    print("N/A")
