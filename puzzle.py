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
    #  note : it can't be night and knave at the same time and there is a way to do it  its better but not required 
    # Not(And(AKnight, AKnave)),  # cannot be k
    Or( AKnight , AKnave ),         # one of them is true -will be Knight or Knave 
    Implication( AKnight, And( AKnight , AKnave) )# call implication from logic
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
        
    #  note : it can't be night and knave at the same time and there is a way to do it  its better but not required 
    #Not ( And(AKnight, AKnave) ) , Not( And(BKnight, BKnave) )
    Or(AKnight, AKnave),        # will be Knight or Knave 
    Or(BKnight, BKnave),        # will be Knight or Knave

    Implication( AKnave, Not(And( AKnave, BKnave )) ),
    Implication( AKnight, And( AKnave, BKnave ) )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
   # in this part i used the not to  make sure that is not knight and hanave at the same time
    Not( And( BKnight, BKnave ) ),
    Not(And(AKnight, AKnave)),
    Or( BKnight, BKnave ) , #one of the ways is or so it has to be one of them ture 
    Or(AKnight, AKnave), #one of the ways is or so it has to be one of them ture 

    # Or(And(AKnight, BKnave), And(AKnave, BKnight)), # A and B can't be the same figure

    Implication(AKnight, And(AKnight, BKnight)),
    Implication(AKnave, Not(And(AKnave, BKnave))),

    Implication(BKnight, And(BKnight, AKnave)),
    Implication(BKnave, Not(And(BKnave, AKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
   #Not( And( CKnight,CKnave ) ) like A and B 
   # now we no that can't not be knight and knave at the same time and i will not add it in here same before (for A and B and C)
   
    Or( AKnight,AKnave ),# call class Or from logic and, so A is a Knight or Knave and seend sybols
    Or( BKnight,BKnave ) ,#call class Or from logic and B will be Knight or Knave and seend sybols
    Or( CKnight,CKnave ) ,# call class Or from logic and C to the same and seend sybols

    # then A says " i am a knight"or"i am a knave"  so we will which one next .
    Or(
        And(
            Implication( AKnight,AKnight ) ,# call the class implication from logic and seend sybols
            Implication( AKnave,Not( AKnight ) )# call the class implication from logic and seend sybols
        ) 
        ,
        
        And(# if he says "i am a knave"
            Implication( AKnight,AKnave ) , # call the class implication from logic and seend sybols
            Implication( AKnave,Not( AKnave ) )) # call the class implication from logic and seend sybols
    ) # close or 
    ,
    Not( And(       
        And( # if says " i am knight "
            Implication( AKnight, AKnight ), # call the class implication from logic and seend sybols
            Implication( AKnave, Not( AKnight) )) # call the class implication from logic and seend sybols
        ,
        And( # "I am a knave."
            Implication( AKnight,AKnave ), # call the class implication from logic and seend sybols
            Implication( AKnave,Not( AKnave ) ) ) # call the class implication from logic and seend sybols
    )) #close Not 
    ,
    # B says "A said 'I am a knave'."
    # call the class implication from logic and seend sybols and nested call class implication 
    Implication( BKnight,And(
        Implication( AKnight,AKnave ),
        Implication(AKnave, Not( AKnave ) ))
        )# close first implication
        ,
    # call the class implication from logic and seend sybols and nested call class implication 

    Implication(BKnave,Not( And
    (
        Implication( AKnight,AKnave ) ,# call the class implication from logic and seend sybols
        Implication( AKnave,Not( AKnave ) )# call the class implication from logic and seend sybols
    ))) # close first implication
    ,
    Implication( BKnight,CKnave ) ,# call the class implication from logic and seend sybols
    Implication( BKnave,Not( CKnave ) ),# call the class implication from logic and seend sybols

    # C says "A is a knight."
    Implication( CKnight,AKnight ) ,# call the class implication from logic and seend sybols
    Implication( CKnave,Not( AKnight ))# call the class implication from logic and seend sybols
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
