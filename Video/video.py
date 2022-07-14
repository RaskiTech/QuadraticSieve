from tkinter import font
from manim import *

# Background color defined in manim.cfg
TEXT_COLOR = GRAY_A
ACCENT_COLOR = BLUE
ACCENT2_COLOR = ORANGE

TEXT_ARGS =   {"font": "Futura Md BT", "font_size": 50, "color": TEXT_COLOR}
TEXT_ARGS_S = {"font": "Futura Md BT", "font_size": 40, "color": TEXT_COLOR}
MATH_ARGS = {"font_size": 60, "color": TEXT_COLOR}

def CreateTextbox(string: str, color) -> VGroup:
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=1.25, width=9, fill_color=color, 
        fill_opacity=0.1, stroke_color=color
    )
    text = Text(string, font="Futura Md BT", font_size=50).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result


class CreateVideo(Scene):
    def construct(self):
        #StartExplanation(self)
        #FermatExplanation(self)
        #KratsKritsExplanation(self)
        QuadraticSieveExplanation(self)
        #OptimizeExplanation(self)


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

    self.play(DrawBorderThenFill(algorithmPart1))
    self.play(DrawBorderThenFill(algorithmPart2))

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
    part1exampleResult = Text("= 32", **TEXT_ARGS_S).next_to(part1example, RIGHT, buff=0.5)
    _temp = MathTex("=\ 2\cdot2\cdot2\cdot2\cdot2", **MATH_ARGS).next_to(part1example, RIGHT, buff=0.5)

    self.play(FadeIn(part1exampleResult))
    self.play(Transform(part1exampleResult, _temp))

    _newGuess = Text("guess = 44", **TEXT_ARGS_S).move_to(guessText)
    self.play(Transform(guessText, _newGuess))

    ############### Video pause and sieving ###############

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

    self.play(
        FadeOut(morePrimes),
        FadeOut(primes),
        FadeOut(counts),
        Uncreate(toFactor),
        Uncreate(pointer)
    )

    self.play(FadeIn(algorithmPart1))
    self.play(algorithmPart1.animate.move_to(UP), algorithmPart2.animate.shift(DOWN), FadeIn(algorithmPart2))

    self.play(FadeOut(algorithmPart1), algorithmPart2.animate.to_edge(UP))
    self.play(FadeOut(algorithmPart2))

    self.wait(2)

    

def OptimizeExplanation(self):
    pass