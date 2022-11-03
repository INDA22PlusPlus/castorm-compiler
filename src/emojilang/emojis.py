# DIGITS IN BASE 12
ZERO = "🕛"                     # THE DIGIT ZERO (0)
ONE = "🕐"                      # THE DIGIT ONE (1)
TWO = "🕑"                      # THE DIGIT TWO (2)
THREE = "🕒"                    # THE DIGIT THREE (3)          
FOUR = "🕓"                     # THE DIGIT FOUR (4)
FIVE = "🕔"                     # THE DIGIT FIVE (5)
SIX = "🕕"                      # THE DIGIT SIX (6)
SEVEN = "🕖"                    # THE DIGIT SEVEN (7)
EIGHT = "🕗"                    # THE DIGIT EIGHT (8)
NINE = "🕘"                     # THE DIGIT NINE (9)
TEN = "🕙"                      # THE DIGIT "TEN" (A) base 12
ELEVEN = "🕚"                   # THE DIGIT "ELEVEN" (B) base 12
DIGITS = { ZERO: 0, ONE: 1, TWO: 2, THREE: 3, FOUR: 4, FIVE: 5, SIX: 6, SEVEN: 7, EIGHT: 8, NINE: 9, TEN: 10, ELEVEN: 11 }
DIGITS_REVERSED = { 0: ZERO, 1: ONE, 2: TWO, 3: THREE, 4: FOUR, 5: FIVE, 6: SIX, 7: SEVEN, 8: EIGHT, 9: NINE, 10: TEN, 11: ELEVEN }
def emoint_to_pyint(string: str) -> str:
    idx = 0
    tot = 0
    for c in string[::-1]:
        if c not in DIGITS.keys(): 
            return None
        tot += DIGITS[c] * 12**idx
        idx += 1
    return str(tot)

def pyint_to_emoint(string: str) -> str:
    try:
        i = int(string)
        idx = 0
        res = ""
        while i != 0:
            res = DIGITS_REVERSED[i % 12] + res
            i //= 12
        return res
    except:
        return None


#ALPHABET
A = "😡"                    
B = "🥵"
C = "🥶"
D = "😨"
E = "🥱"
F = "😈"
G = "👿"
H = "🤢"
I = "🤡"
J = "💩"
K = "💀"
ALPHABET = { A: "A", B: "B", C: "C", D: "D", E: "E", F: "F", G: "G", H: "H", I: "I", J: "J", K: "K" }
#ALPHABET_REVERSED = { "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K }


# ARITHMETIC
ADDITION = "🙂"                         # ADDITION (+)
MULTIPLICATION = "😂"                   # MULTIPLICATION (*)
SUBTRACTION = "🙃"                      # SUBTRACTION (-)
DIVISION = "😭"                         # (INTEGER)DIVISION (/)
ARITHMETIC = { ADDITION: "+", SUBTRACTION: "-", MULTIPLICATION: "*", DIVISION: "//"}



# COMPARISONS
GT = "👆"                       # GREATER THAN (>)
LT = "👇"                       # LESS THAN (<)
EQ = "👍"                       # EQUALS (==)
NE = "👎"                       # NOT EQUAL (!=)
COMPARISONS = { GT: ">", LT: "<", EQ: "==", NE: "!=" }

# BOOLEAN LOGIC
OR = "✌️"                       # LOGICAL OR (||)
AND = "🤞"                      # LOGICAL AND (&&)
NOT = "❌"                      # LOGICAL NOT (!)
TRUE = "✅"
FALSE = "❎"
LOGIC = { OR: "or", AND: "and", NOT: "not" }
BOOLS = { TRUE: "True", FALSE: "False"}

# FLOW CONTROL
IF = "👉"                   # IF ([CONDITION] 👉 [BLOCK OF CODE])
ELSE = "👈"                 # ELSE ([CONDITION] 👉 [BLOCK OF CODE] 👈 [BLOCK OF CODE])
LOOP = "👌"                 # WHILE (👌 [BLOCK OF CODE])
FLOW = { IF: "if", ELSE: "else", LOOP: "while True:"}

# IO
OUTPUT = "👄"                     # OUTPUT (print())
INPUT = "👂"
IO = {OUTPUT: "print", INPUT: "input()"}


# OTHER
NEWLINE = "🚩"
ASSIGNMENT = "👏"                       # VARIABLE ASSIGNMENT (=)

LP = "🤛"
RP = "🤜"

LB = "👐"
RB = "🙌"

DEFINITIONS = set([NEWLINE, ASSIGNMENT, LP, RP, LB, RB] + list(IO.keys()) + list(FLOW.keys()) + list(LOGIC.keys()) + list(COMPARISONS.keys()) + list(ARITHMETIC.keys()) + list(ALPHABET.keys()) + list(DIGITS.keys()))

