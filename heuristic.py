PIECE_SCORES = [0,0,900,-900,500,-500,330,-330,320,-320,100,-100,0]

heuristic=lambda b: sum(PIECE_SCORES[p]for r in b for p in r)
