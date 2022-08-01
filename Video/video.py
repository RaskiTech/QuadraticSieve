from tkinter import font
from wsgiref.util import guess_scheme
from manim import *
from numpy import full
from pygments import highlight

# Background color defined in manim.cfg
TEXT_COLOR = GRAY_A
ACCENT_COLOR = BLUE
ACCENT2_COLOR = ORANGE

TEXT_ARGS =   {"font": "Futura Md BT", "font_size": 50, "color": TEXT_COLOR}
TEXT_ARGS_S = {"font": "Futura Md BT", "font_size": 40, "color": TEXT_COLOR}
MATH_ARGS = {"font_size": 60, "color": TEXT_COLOR}
MATH_ARGS_S = {"font_size": 50, "color": TEXT_COLOR}

def CreateTextbox(string: str, color) -> VGroup:
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=1.25, width=9, fill_color=color, 
        fill_opacity=0.1, stroke_color=color
    )
    text = Text(string, font="Futura Md BT", font_size=50).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result

def ShowTextbox(self, textbox) -> None:
    self.play(DrawBorderThenFill(textbox[0]), Create(textbox[1]))

def HideTextbox(self, textbox) -> None:
    self.play(FadeOut(textbox[0]), Uncreate(textbox[1]))


class CreateVideo(Scene):
    def construct(self):
        #StartExplanation(self)
        #FermatExplanation(self)
        #KratsKritsExplanation(self)
        #QuadraticSieveExplanation(self)
        OptimizeExplanation(self)


def StartExplanation(self):
    pass

def FermatExplanation(self):
    pass

def KratsKritsExplanation(self):
    pass

def QuadraticSieveExplanation(self):

    header = Text("Quadratic Sieve", font="Futura Md BT", font_size=100, color=ACCENT_COLOR)
    self.play(Create(header))
    self.wait(0)
    self.play(Uncreate(header))

    bText = Text("B = 13", font="Futura Md BT", font_size=40, color=TEXT_COLOR)
    self.play(FadeIn(bText))

    self.wait(0)
    self.play(bText.animate.to_edge(UP + LEFT))
    self.wait()

    example1first = Text("20")
    example1second = MathTex(r"5\cdot2\cdot2")
    example1first.shift(-DOWN * 0.5)
    self.play(FadeIn(example1first), example1first.animate.shift(DOWN * 0.5))
    self.play(Transform(example1first, example1second))
    self.wait(0)
    checkmark = MathTex(r"\checkmark", color=GREEN).next_to(example1first, RIGHT)
    self.play(FadeIn(checkmark))
    self.wait(0)
    self.play(FadeOut(example1first), FadeOut(checkmark))


    example2first = Text("34")
    example2second = MathTex(r"17\cdot2")
    example2first.shift(-DOWN * 0.5)
    self.play(FadeIn(example2first), example2first.animate.shift(DOWN * 0.5))
    self.play(Transform(example2first, example2second))
    self.wait(0)
    self.play(example2first.animate.set_color(RED))
    self.wait(0)
    self.play(FadeOut(example2first))

    algorithmPart1 = CreateTextbox("Finding B-smooth numbers", ACCENT_COLOR).shift(UP * 0.5)
    algorithmPart2 = CreateTextbox("Solve kernels of a matrix", ACCENT2_COLOR)
    algorithmPart2.next_to(algorithmPart1, DOWN, buff=1)

    ShowTextbox(algorithmPart1)
    ShowTextbox(algorithmPart2)

    self.play(
        algorithmPart1.animate.to_edge(UP),

        algorithmPart2.animate.shift(DOWN),
        FadeOut(algorithmPart2)
    )

    self.wait()
    self.play(FadeOut(algorithmPart1))

    algorithmPart2.shift(UP)

    ############### Part 1 #################

    text1 = MathTex("x^2\ mod\ N \\text{ is B-smooth}", **MATH_ARGS).shift(UP)
    self.play(FadeIn(text1))

    nText = Text("N = 1817", **TEXT_ARGS_S)
    self.play(Create(nText))
    self.play(nText.animate.to_edge(UP + LEFT).shift(DOWN * 0.75))

    guessText = Text("guess = 43", **TEXT_ARGS_S).to_edge(UP + LEFT).shift(DOWN * 1.5)
    self.play(FadeIn(guessText))

    part1example = MathTex("34^2\ mod\ 1817", **MATH_ARGS)
    self.play(Create(part1example))
    self.play(part1example.animate.shift(LEFT * 2))
    part1exampleResult = MathTex("= 32", **MATH_ARGS).next_to(part1example, RIGHT, buff=0.5)
    _temp = MathTex("=\ 2\cdot2\cdot2\cdot2\cdot2", **MATH_ARGS).next_to(part1example, RIGHT, buff=0.5)

    self.play(FadeIn(part1exampleResult))
    self.play(Transform(part1exampleResult, _temp))

    _newGuess = Text("guess = 44", **TEXT_ARGS_S).move_to(guessText)
    self.play(Transform(guessText, _newGuess))

    ############### Sieving ###############

    pauseEffect = Square(1000).set_fill(WHITE, 0.25)
    self.add(pauseEffect)

    self.wait(0.5)

    # Clear
    self.play(
        pauseEffect.animate.set_fill(WHITE, 0),
        bText.animate.shift(LEFT * 4),
        nText.animate.shift(LEFT * 4),
        guessText.animate.shift(LEFT * 4),
        FadeOut(text1),
        FadeOut(part1example),
        FadeOut(part1exampleResult)
    )

    primes = VGroup(
        Text("2 ", **TEXT_ARGS),
        Text("3 ", **TEXT_ARGS),
        Text("5 ", **TEXT_ARGS),
        Text("7 ", **TEXT_ARGS),
        Text("11", **TEXT_ARGS),
        Text("13", **TEXT_ARGS)
    )
    counts = VGroup(
        Text("_ ", **TEXT_ARGS),
        Text("_ ", **TEXT_ARGS),
        Text("_ ", **TEXT_ARGS),
        Text("_ ", **TEXT_ARGS),
        Text("_ ", **TEXT_ARGS),
        Text("_ ", **TEXT_ARGS)
    )

    toFactor = Text("4840", **TEXT_ARGS).shift(DOWN * 2)
    self.play(Create(toFactor))

    for i, num in enumerate(primes):
        num.shift(RIGHT * (i - len(primes)/2))
    primes.shift(UP * 3)
    for i, count in enumerate(counts):
        count.shift(RIGHT * (i - len(counts)/2))
    counts.shift(UP * 0.5)
    self.add(counts)

    self.play(FadeIn(primes))


    pointer = Arrow(start=DOWN, end=UP, color=RED).next_to(primes[0], DOWN)

    self.play(Create(pointer))

    temp = Text("2420", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("1 ").move_to(counts[0])))

    temp = Text("1210", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("2 ").move_to(counts[0])))

    temp = Text("605", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("3 ").move_to(counts[0])))

    self.play(pointer.animate.next_to(primes[1], DOWN))
    self.play(pointer.animate.next_to(primes[2], DOWN))

    temp = Text("121", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[2], Text("1 ").move_to(counts[2])))

    self.play(pointer.animate.next_to(primes[3], DOWN))
    self.play(pointer.animate.next_to(primes[4], DOWN))

    temp = Text("11", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[4], Text("1 ").move_to(counts[4])))

    temp = Text("1", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[4], Text("2 ").move_to(counts[4])))

    morePrimes = VGroup(
        Text("17", **TEXT_ARGS),
        Text("19", **TEXT_ARGS),
        Text("23", **TEXT_ARGS),
        Text("29", **TEXT_ARGS),
        Text("31", **TEXT_ARGS),
        Text("37", **TEXT_ARGS)
    )
    for i, num in enumerate(morePrimes):
        num.shift(RIGHT * (i - len(morePrimes)/2))
    morePrimes.next_to(primes, RIGHT, buff=0.4).set_fill(GRAY)
    self.play(FadeIn(morePrimes))
    arrow = Arrow(ORIGIN, 2 * RIGHT, color=RED).next_to(primes[-1], DOWN).shift(RIGHT * 0.5)
    self.play(Create(arrow))

    self.play(
        FadeOut(morePrimes),
        FadeOut(primes),
        FadeOut(counts),
        Uncreate(toFactor),
        Uncreate(pointer),
        Uncreate(arrow)
    )

    self.play(FadeIn(algorithmPart1))
    self.play(algorithmPart1.animate.move_to(UP), algorithmPart2.animate.shift(DOWN), FadeIn(algorithmPart2))

    self.play(FadeOut(algorithmPart1), algorithmPart2.animate.to_edge(UP))
    self.play(FadeOut(algorithmPart2))

    ######### Part 2 ##########

    self.play(
        bText.animate.shift(RIGHT * 4),
        nText.animate.shift(RIGHT * 4),
        #guessText.animate.shift(RIGHT * 4)
    )


    equations = VGroup(
        MathTex("34^2\\equiv","\\ 32","\\ mod\\ 1817", **MATH_ARGS).shift(UP * 1.5),
        MathTex("45^2\\equiv","208","\\ mod\\ 1817", **MATH_ARGS).shift(UP * 0.5),
        MathTex("47^2\\equiv","392","\\ mod\\ 1817", **MATH_ARGS).shift(UP * -0.5),
        MathTex("51^2\\equiv","784","\\ mod\\ 1817", **MATH_ARGS).shift(UP * -1.5),
    ).shift(UP * 1.5)
    factoredForms = VGroup(
        MathTex("2^5", **MATH_ARGS).next_to(ORIGIN, RIGHT).shift(UP * 1.5),
        MathTex("2^4","\cdot","13^1", **MATH_ARGS).next_to(ORIGIN, RIGHT).shift(UP * 0.5),
        MathTex("2^3","\cdot","7^2", **MATH_ARGS).next_to(ORIGIN, RIGHT).shift(UP * -0.5),
        MathTex("2^4","\cdot","7^2", **MATH_ARGS).next_to(ORIGIN, RIGHT).shift(UP * -1.5),
    ).next_to(equations, RIGHT, buff=1.0)
    for tex in factoredForms:
        tex.set_fill(GRAY)
    equations.z_index = 1
    

    self.play(Create(equations))

    highlightBox = Rectangle(GRAY_D, 3.6, 1.1).shift(UP * 1.4 + LEFT * 0.5).set_fill(GRAY_D, 1)
    highlightBox.z_index = 0
    self.play(FadeIn(highlightBox))
    self.play(FadeOut(highlightBox))

    self.play(FadeIn(factoredForms))
    self.play(FadeOut(factoredForms))

    goal = MathTex("a^2\\equiv b^2\\ mod\\ N", **MATH_ARGS_S).shift(DOWN * 2)
    self.play(Create(goal))

    self.play(FadeIn(highlightBox))
    self.play(FadeOut(highlightBox))

    squareExample1 = MathTex("47","^2","\cdot","51","^2", font_size=50, color=BLUE).shift(3*LEFT + DOWN)
    squareExample1_2 = MathTex("(","47","\cdot","51",")","^2", font_size=50, color=BLUE).move_to(squareExample1)

    self.play(FadeIn(squareExample1))
    self.play(TransformMatchingTex(squareExample1, squareExample1_2), run_time=2)
    self.play(FadeOut(squareExample1_2))

    self.play(FadeIn(highlightBox))
    self.play(FadeOut(highlightBox))

    numbers = VGroup(
        MathTex("\\ 32", **MATH_ARGS).shift(UP * 1.5),
        MathTex("208", **MATH_ARGS).shift(UP * 0.5),
        MathTex("392", **MATH_ARGS).shift(UP * -0.5),
        MathTex("784", **MATH_ARGS).shift(UP * -1.5),
    ).shift(LEFT * 1.5)

    self.play(
        TransformMatchingTex(equations[0], numbers[0]),
        TransformMatchingTex(equations[1], numbers[1]),
        TransformMatchingTex(equations[2], numbers[2]),
        TransformMatchingTex(equations[3], numbers[3]),
        FadeOut(goal)
    )
    factoredForms.move_to(numbers)
    factoredForms.color = TEXT_COLOR
    self.play(
        TransformMatchingTex(numbers[0], factoredForms[0]),
        TransformMatchingTex(numbers[1], factoredForms[1]),
        TransformMatchingTex(numbers[2], factoredForms[2]),
        TransformMatchingTex(numbers[3], factoredForms[3])
    )

    
    squareExample2 = VGroup(
        MathTex("(","x","^4","\cdot","y","^3",")","(","x","^2","\cdot","y","^1",")"),
        MathTex("(","x","^{","4","+","2","}","\cdot","y","^{","3","+","1","}",")"),
        MathTex("(","x","^6","\cdot","y","^4",")"),
        MathTex("(","x","^3","\cdot","y","^2",")","^2")
    )
    squareExample2.arrange(DOWN, buff=0.5).shift(RIGHT * 3)
    for tex in squareExample2:
        tex.color = BLUE

    self.play(FadeIn(squareExample2[0]))
    self.play(TransformMatchingTex(squareExample2[0].copy(), squareExample2[1]), run_time=2)
    self.play(TransformMatchingTex(squareExample2[1].copy(), squareExample2[2]), run_time=2)
    self.play(TransformMatchingTex(squareExample2[2].copy(), squareExample2[3]), run_time=2)

    self.play(FadeOut(squareExample2))

    fullFactoredForms = VGroup(
        MathTex("2^5","\cdot","3^0","\cdot","5^0","\cdot","7^0","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * 1.5),
        MathTex("2^4","\cdot","3^0","\cdot","5^0","\cdot","7^0","\cdot","11^0","\cdot","13^1", **MATH_ARGS).shift(UP * 0.5),
        MathTex("2^3","\cdot","3^0","\cdot","5^0","\cdot","7^2","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * -0.5),
        MathTex("2^4","\cdot","3^0","\cdot","5^0","\cdot","7^2","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * -1.5),
    ).move_to(factoredForms)
    for tex in fullFactoredForms:
        tex.set_color_by_tex("0", GRAY_D)

    self.play(TransformMatchingTex(factoredForms, fullFactoredForms), runTime=2)

    even = Text("Even", **TEXT_ARGS).shift(RIGHT * 4 + UP * 1.3)
    even.color = RED
    evenMod = MathTex("x\equiv0\ mod\ 2").next_to(even, DOWN, buff=0.5)
    self.play(Create(even))
    self.play(FadeIn(evenMod))

    odd = Text("Odd", **TEXT_ARGS).shift(RIGHT * 4 - UP * 1.3)
    odd.color = BLUE
    oddMod = MathTex("x\equiv1\ mod\ 2").next_to(odd, DOWN, buff=0.5)
    self.play(Create(odd))
    self.play(FadeIn(oddMod))


    self.play(FadeOut(odd), FadeOut(oddMod), FadeOut(even), FadeOut(evenMod))
    self.play(fullFactoredForms.animate.to_edge(UP + RIGHT))

    Xs = VGroup(
        MathTex("x_1", **MATH_ARGS).shift(UP * 1.5),
        MathTex("x_2", **MATH_ARGS).shift(UP * 0.5),
        MathTex("x_3", **MATH_ARGS).shift(UP * -0.5),
        MathTex("x_4", **MATH_ARGS).shift(UP * -1.5),
    ).next_to(fullFactoredForms, LEFT, buff=1.5)
    Xs.color = BLUE

    self.play(FadeIn(Xs))

    exponents2 = MathTex("2^5","\ ","2^4","\ ","2^3","\ ","2^4", **MATH_ARGS_S).shift(DOWN * 2)
    exponents2_add = MathTex("5","x_1+","4","x_2+","3","x_3+","4","x_4", **MATH_ARGS_S).move_to(exponents2)
    modulo2Equiv  = MathTex("5","x_1+","4","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(exponents2)
    self.play(TransformMatchingTex(fullFactoredForms.copy(), exponents2))
    self.play(TransformMatchingTex(exponents2, exponents2_add))
    self.play(TransformMatchingTex(exponents2_add, modulo2Equiv))

    modulo2Equiv_simple1  = MathTex("5","x_1+","0","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    modulo2Equiv_simple2  = MathTex("1","x_1+","0","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    modulo2Equiv_simple3  = MathTex("1","x_1+","0","x_2+","1","x_3+","0","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple1))
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple2))
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple3))

    linearEquations = VGroup(modulo2Equiv)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+1x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)

    self.play(FadeOut(fullFactoredForms), FadeOut(Xs), FadeOut(modulo2Equiv))
    linearEquations.arrange(DOWN).move_to(ORIGIN)
    self.play(Create(linearEquations))

    mat = Matrix([[1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])


    self.play(FadeOut(linearEquations))
    self.play(FadeIn(mat))

    self.play(mat.animate.shift(RIGHT + DOWN * 0.25))

    Xs.color = BLUE
    Xs.arrange(RIGHT, buff=0.8).next_to(mat, UP, buff=0.5)
    primes = VGroup(
        Text(" 2", **TEXT_ARGS_S),
        Text(" 3", **TEXT_ARGS_S),
        Text(" 5", **TEXT_ARGS_S),
        Text(" 7", **TEXT_ARGS_S),
        Text("11", **TEXT_ARGS_S),
        Text("13", **TEXT_ARGS_S)
    ).arrange(DOWN, buff=0.4).next_to(mat, LEFT, buff=0.5)
    primes.color = BLUE

    self.play(FadeIn(Xs), FadeIn(primes))

    highlight = SurroundingRectangle(mat.get_entries()[3 * 4 + 1])
    self.play(Create(highlight))
    self.play(Uncreate(highlight))

    solutionVec = VGroup(
        MathTex("1", **MATH_ARGS),
        MathTex("0", **MATH_ARGS),
        MathTex("1", **MATH_ARGS),
        MathTex("0", **MATH_ARGS)
    ).arrange(RIGHT, buff=1.0).move_to(Xs)
    solutionVec.color = BLUE

    self.play(Transform(Xs, solutionVec))

    self.play(FadeOut(Xs), FadeOut(primes), FadeOut(mat))
    numbers.move_to(ORIGIN)
    self.play(FadeIn(numbers))

    takenNums = VGroup( MathTex("\\ 32", **MATH_ARGS),MathTex("392", **MATH_ARGS)).arrange(DOWN, buff=0.5)
    self.play(TransformMatchingTex(numbers, takenNums))
    self.play(takenNums[0].animate.set_color(RED), takenNums[1].animate.set_color(ORANGE))

    self.play(takenNums.animate.shift(UP * 2))

    finalEq = MathTex("43^2","\cdot ","47^2","\equiv ","2^5","\cdot ","2^3\cdot 7^2","\ mod\ 1817", **MATH_ARGS)
    finalEq.set_color_by_tex_to_color_map({"2^5": RED, "43^2": RED, "2^3\cdot 7^2": ORANGE, "47^2": ORANGE})
    finalEq_2 = MathTex("(43\cdot 47)^2\equiv (2^4\cdot 7^1)^2\ mod\ 1817", **MATH_ARGS).next_to(finalEq, DOWN, buff=0.5)

    goal.next_to(finalEq_2, DOWN, buff=1)
    gdc = MathTex("gdc(N,\ a-b)", **MATH_ARGS_S).move_to(goal).shift(RIGHT * 2)
    goal.shift(LEFT * 2)

    goal.color = BLUE
    gdc.color = BLUE

    self.play(Create(finalEq))
    self.play(Create(finalEq_2))
    self.play(FadeIn(goal))
    self.play(FadeIn(gdc))

    self.play(FadeOut(takenNums))

    solution1 = Text(" X   Y = 1817 ", font="Futura Md BT").shift(UP * 2)
    solution2 = Text("  X   23 = 1817", font="Futura Md BT").move_to(solution1)
    solution3 = Text("79   23 = 1817", font="Futura Md BT").move_to(solution1)

    dot = Text("⋅").move_to(solution1).shift(LEFT * 1.3)

    self.play(FadeIn(solution1), FadeIn(dot))
    self.play(Transform(solution1, solution2), dot.animate.shift(LEFT *  0.2))
    self.play(Transform(solution1, solution3), dot.animate.shift(LEFT * -0.2))


    self.wait(2)
    self.play(Uncreate(solution1), FadeOut(gdc), FadeOut(goal), FadeOut(finalEq), FadeOut(finalEq_2))
    self.play(FadeOut(bText), FadeOut(nText))

def OptimizeExplanation(self):

    ########### Recap ##########

    buffer = 0.2
    scalar = 0.45

    tower = VGroup(
        CreateTextbox("Pick B", ORANGE),
        CreateTextbox("Decide data amount", ORANGE),
        CreateTextbox("Calculate first guess", ORANGE),

        VGroup(
            VGroup(
                CreateTextbox("Calculate possible number", GREEN),
                CreateTextbox("Sieve the number", GREEN),
                CreateTextbox("Increment guess", GREEN)
            ).arrange(DOWN, buff=buffer),
            CreateTextbox("Build matrix", YELLOW),
            VGroup(
               CreateTextbox("Solve one solution", RED),
               CreateTextbox("Check that solution", RED)
            ).arrange(DOWN, buff=buffer),
            CreateTextbox("Increase data requirement", BLUE)
        ).arrange(DOWN, buff=buffer)
    ).arrange(DOWN, buff=buffer).scale(scalar).to_edge(UP + LEFT)

    def CreateArrow(vgroup):
        self.play(vgroup.animate.shift(RIGHT * 0.5))
        arrow = Arrow(start=vgroup.get_bottom(), end=vgroup.get_top()).next_to(vgroup, LEFT)
        self.play(Create(arrow))
        vgroup += arrow

    mat = Matrix([[1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
    mat.shift(RIGHT * 2.5 + DOWN * 0.25)
    Xs = VGroup(
        MathTex("x_1", **MATH_ARGS).shift(UP * 1.5),
        MathTex("x_2", **MATH_ARGS).shift(UP * 0.5),
        MathTex("x_3", **MATH_ARGS).shift(UP * -0.5),
        MathTex("x_4", **MATH_ARGS).shift(UP * -1.5),
    ).arrange(RIGHT, buff=0.8).next_to(mat, UP, buff=0.5)
    Xs.color = BLUE
    primes = VGroup(
        Text(" 2", **TEXT_ARGS_S),
        Text(" 3", **TEXT_ARGS_S),
        Text(" 5", **TEXT_ARGS_S),
        Text(" 7", **TEXT_ARGS_S),
        Text("11", **TEXT_ARGS_S),
        Text("13", **TEXT_ARGS_S)
    ).arrange(DOWN, buff=0.4).next_to(mat, LEFT, buff=0.5)
    primes.color = BLUE
    matVisual = VGroup(mat, Xs, primes).scale(0.75)



    ShowTextbox(self, tower[0])
    ShowTextbox(self, tower[1])
    ShowTextbox(self, tower[2])

    ShowTextbox(self, tower[3][0][0])
    ShowTextbox(self, tower[3][0][1])
    ShowTextbox(self, tower[3][0][2])
    CreateArrow(tower[3][0])

    ShowTextbox(self, tower[3][1])
    self.play(FadeIn(matVisual))
    self.play(FadeOut(matVisual))

    ShowTextbox(self, tower[3][2][0])
    ShowTextbox(self, tower[3][2][1])
    gdc = MathTex("gdc(N,\ a-b)", **MATH_ARGS_S).shift(RIGHT * 2.5)
    gdc.color = BLUE
    self.play(FadeIn(gdc))
    CreateArrow(tower[3][2])
    ShowTextbox(self, tower[3][3])
    CreateArrow(tower[3])
    self.play(FadeOut(gdc))

    originalTower = tower.copy()


    ###########   The forbidden 3  ##########

    pickB = tower[0]
    pickData = tower[1]
    pickGuess = tower[2]

    tower -= pickB
    tower -= pickData
    tower -= pickGuess

    self.play(
        FadeOut(tower), 
        pickB.animate.to_edge(UP + LEFT),
        pickGuess.animate.move_to(ORIGIN).to_edge(UP),
        pickData.animate.to_edge(UP + RIGHT)
    )
    self.remove(tower)

    self.play( FadeOut(pickGuess), FadeOut(pickData), pickB.animate.move_to(ORIGIN).to_edge(UP))

    bFormula = MathTex("B=(e^{\sqrt{\ln(N)\ln(\ln N)}})^{\\frac{1}{\sqrt{2}}}", **MATH_ARGS)
    self.play(Create(bFormula))
    self.play(FadeOut(bFormula))

    self.play(FadeIn(pickGuess), FadeIn(pickData), pickB.animate.to_edge(UP + LEFT))
    self.play( FadeOut(pickData), pickGuess.animate.move_to(ORIGIN).to_edge(UP), FadeOut(pickB))

    guessFormula = MathTex("guess=\lceil \sqrt{N}\\rceil", **MATH_ARGS)
    guessCalc = MathTex("x=guess^2\ mod\ N", **MATH_ARGS).next_to(guessFormula, DOWN)

    self.play(FadeIn(guessCalc))
    self.play(Create(guessFormula))

    self.play(FadeOut(guessCalc), FadeOut(guessFormula))

    self.play(FadeIn(pickB), FadeIn(pickData), pickGuess.animate.move_to(ORIGIN).to_edge(UP))
    self.play( FadeOut(pickB), pickData.animate.move_to(ORIGIN).to_edge(UP), FadeOut(pickGuess))

    dataFormula = MathTex("\\text{amountTo}(B)+5")
    self.play(FadeIn(dataFormula))
    self.play(FadeOut(pickData), FadeOut(dataFormula))


    ########### Euler's criterion ###########

    critBox = CreateTextbox("Euler's criterion", PURPLE).scale(scalar).shift(10 * LEFT + UP * 1.15)

    # Could just add to index if there exists a function
    tmp = originalTower[3]
    originalTower -= tmp
    originalTower += critBox
    originalTower += tmp

    originalTower.shift(7 * LEFT)
    self.play(originalTower.animate.shift(RIGHT * 7))

    self.play(FadeIn(matVisual))
    self.play(FadeOut(matVisual))

    self.play(originalTower.animate.arrange(DOWN, buff=scalar * buffer).to_edge(UP + LEFT))
    self.play(originalTower[4].animate.shift(RIGHT * 0.5))

    eulerCheck = MathTex("N^{\\frac{p-1}{2}}mod\ p", **MATH_ARGS).shift(RIGHT * 2)
    self.play(Create(eulerCheck))
    self.play(FadeOut(eulerCheck))


    self.play(FadeIn(matVisual))

    highlight1 = Rectangle(GRAY_D, 1.15, 3.6).shift(RIGHT * 2.4 + UP * 0.45).set_fill(GRAY_D, 1)
    highlight2 = Rectangle(GRAY_D, 0.6, 3.6).shift(RIGHT * 2.4 + DOWN * 1.05).set_fill(GRAY_D, 1)
    matVisual.z_index = 1
    highlight1.z_index = 0
    highlight2.z_index = 0

    self.play(FadeIn(highlight1), FadeIn(highlight2))
    self.play(FadeOut(highlight1), FadeOut(highlight2))

    self.play(FadeOut(matVisual))
    self.play(originalTower.animate.move_to(ORIGIN))