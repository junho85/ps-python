# 1p 가 이겨야 된다.
python judge.py ./dodo.py ./dodo_punch_kick_punch_kick.py
python judge.py ./dodo.py ./dodo_simple_punch.py

# 2p 가 이겨야 된다.
# fail
python judge.py ./dodo_punch_kick_punch_kick.py ./dodo.py
python judge.py ./dodo_kick_punch_kick_punch.py ./dodo.py

# success
python judge.py ./dodo_simple_punch.py ./dodo.py

# kick punch vs kick punch (P1 almost win)
python judge.py ./dodo_kick_punch_kick_punch.py ./dodo_kick_punch_kick_punch.py

# kick punch vs punch kick (P1 got advantage)
python judge.py ./dodo_kick_punch_kick_punch.py ./dodo_punch_kick_punch_kick.py

# punch kick vs kick punch (random. P1 got little advantage)
python judge.py ./dodo_punch_kick_punch_kick.py ./dodo_kick_punch_kick_punch.py