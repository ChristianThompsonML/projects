## Data Manipulation
0. All Features

2. Features to transform
    a. wrestlerRecord - split into wins, losses, win_pct and totalMatches
    b. wrestlerSeed - convert to 1/wrestlerSeed
    c. wrestlerRank - convert to 1/wrestlerRank
    e. wrestlerClass - convert to numeric based on years of experience 1-Fr, 2-So, 3-Jr, 4-Sr

3. Final Dataset 
    Numerical
        a. wrestlerCap
        b. wrestlerRank
        c. wrestlerSeed
        d. wins
        e. losses
        f. win_pct
        g. teamRank
        h. teamPts
        i. totalMatches
    Categorical
        a. wrestlerClass
        b. wrestlerWeightClass
        c. tournamentYear

4. Features to ignore - for the purposes of this exercise we will ignore the post tournament features as they won't be known before the tournament.
    a. wrestlerAllAmerican
    b. wrestlerChampion