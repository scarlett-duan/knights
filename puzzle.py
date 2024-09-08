'''
puzzle.py contains various 4 puzzles made by claims from three knights and three knaves. 
Their associated knowledge basesare ran through the model in logic.py to return Which is 
a knight and which is a knave. 

Below there are three knights and three knaves which will be making claims.

'''

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Or(Not(AKnight), And(AKnight, AKnave))
)   

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(Not(AKnight), And(AKnave, BKnave)),
    Or(Not(AKnight), Not(Or(AKnight, BKnight))),
    Or(Not(AKnave), Or(AKnight, BKnight))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(Not(AKnight), And(AKnight, BKnight)),
    Or(Not(AKnave), Or(AKnight, BKnight)),
    Or(Not(BKnight), AKnave),
    Or(Not(BKnave), AKnave)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave), 
    Or(CKnight, CKnave), 
    Or(Not(BKnight), Not(AKnave)),
    Or(Not(BKnave), Not(AKnave)), 
    Or(Not(BKnight), CKnave), 
    Or(Not(BKnave), Not(CKnave)), 
    Or(Not(CKnight), AKnight), 
    Or(Not(CKnave), Not(AKnight))


)

#runs each knowledge base through our model_check in logic.py
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    # A list containing all puzzles and their associated knowledge bases
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print(f"    Not yet implemented. Could not find knowledge base for {puzzle}. Missing 'conjuncts'.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol} is true")
                else:
                    print(f"    {symbol} is false or unknown")


if __name__ == "__main__":
    main()
