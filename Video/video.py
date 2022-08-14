from math import ceil, sqrt
import string
from tkinter import font
from tokenize import String
from venv import create
from wsgiref.util import guess_scheme
from manim import *
from numpy import full, place
from pygments import highlight

# Background color defined in manim.cfg
TEXT_COLOR = GRAY_A
ACCENT_COLOR = BLUE
ACCENT2_COLOR = RED
TIME = 0 # wait time in each self.wait

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
        #FermatExplanationExample(self)
        #KratsKritsExplanation(self)
        #QuadraticSieveExplanation(self)
        #OptimizeExplanation(self)
        pass


def StartExplanation(self):

    # Nowadays big prime numbers are used a lot in cryptography.

    lock_image = SVGMobject('lock.svg', height=4)
    key_image = SVGMobject('key.svg', height=4)

    self.play(Create(lock_image))
    self.wait(TIME)

    # These numbers are used to create big semiprimes often used as keys

    self.play(Transform(lock_image, key_image))
    self.wait(TIME)
    
    # But when I said big primes you might wonder how big

    text_1 = Text('?', font="Futura Md BT", font_size=100)

    self.play(Uncreate(lock_image), Create(text_1))
    self.wait(TIME)

    self.play(Uncreate(text_1))

    number_1 = Text('2', font="Futura Md BT", font_size=100)
    number_2 = Text('61', font="Futura Md BT", font_size=100)
    number_3 = Text('8256536257', font="Futura Md BT", font_size=100)
    number_4 = Paragraph('''

    -----BEGIN PUBLIC KEY-----

        MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQB6kft8xpg60bjBp0pNsKlx
        FWkSRl3kf0CCSAo2zfPaLoVzfJL8LpzjfK59AnAVeM+n2z1mY3WBfTSVDDcq6NNk
        bSIH4Ov/0/MSSZpjRp4Z5roQwZVihhSoNN2aPREDngylXHBb5+WZ9n+PsY9yu0H6
        15Y+NWDIlUI9KCg+MKmp7h7+Pos8lIESVu/tIoNIL1ICuBYSusAK0wGoNfJjOiit
        cCkSd7g/kFXaXtF0Wz/KEaJ+dlksXZRq95y60EY5xN3CKamQuMEfHWc3sa/5qEsm
        6q3+QkW2oNYHEHK+F/bhco4SK0nXM4kvHy5HUvF0Nv9vlOog2KuY8F5w6XpqmvLN
        AgMBAAE=

    -----END PUBLIC KEY-----

    ''', font="Futura Md BT", font_size=20)

    number_5 = MathTex(r'10^{300}', font_size=100)

    # Well the primes of which theese keys consist arent normal primes like 2

    self.play(Create(number_1))
    self.wait(TIME)
    self.play(Transform(number_1, number_2))
    self.wait(TIME)
    # or like 61
    self.play(Transform(number_1, number_3))
    self.wait(TIME)
    # or even like this behemoth
    # In reality the keys look like this:
    self.play(Transform(number_1, number_4))
    self.wait(TIME)

    # AND the primes that make them up are on the scale of
    self.play(Transform(number_1, number_5))
    self.wait(TIME)
    # 10^600

    # well that got big really fast

    self.play(Uncreate(number_1))

    # Alkutekstit

    OpeningCredits(self)

    # When I first saw these big prime numbers I thought to myself: “huh, that seems a bit extreme” and just after that “wait a minute! how on earth could anyone verify that!”. These primes are like over 600 digits long. If they had two factors of the same length they would both be 300 digits long. And you may say: “300 digits phew that doesn’t sound like much”, but think about it in this way: the universe 436,117,077,000,000,000 seconds old – that’s only a at the scale of 10^18, 18 digits, and those potential factors would be on a scale waaay bigger.

    TrialDivisionExplanation(self)

    self.wait(TIME)
    # Now, If you started checking factors for these primes at the beginning of the universe with a rate of about quintillion numbers a second, you’d still have to check about a billion times more digits until you would have found these potential factors. That is great if you are some sort of an eternal being since you’ve got the answer, but to us mere mortals time is a problem. The amount of possible factors grows about the same rate as the square root of the number if we aren’t using any techniques, and with that we would have to say goodbye to ever factoring these giant numbers. But that got me thinking, what other ways there are to factor these big integers?

    # That brings us to the topic of this video, Quadratic Sieve. It is the second best factorization method currently known. The best method, General number sieve, is far more complex and out of the scope of this video, but Quadratic sieve doesn’t fall far behind: It is still the best algorithm for factoring numbers less than 100 digits, which is good enough for us. We hope to give you an in-depth understanding of this algorithm, so that in the end of this video you could, for example, program your own implementation of Quadratic Sieve.


def OpeningCredits(self):
    header = Text("Quadratic Sieve", font="Futura Md BT", font_size=100, color=ACCENT_COLOR).move_to(UP*0.5)
    header_1 = Text("or", font="Futura Md BT", font_size=40, color=ACCENT_COLOR).move_to(DOWN*1.25 + LEFT*20)
    header_2 = Text("How to factor REALLY fast", font="Futura Md BT", font_size=40, color=ACCENT_COLOR).move_to(DOWN*1.75+LEFT*50)
    sub_header = Text("Rasse & Kimmo", font="Futura Md BT", font_size=30, color=WHITE).move_to(DOWN*3)

    self.play(Write(header))
    self.wait(1)
    self.play(header_1.animate.move_to(DOWN*1.5), header_2.animate.move_to(DOWN*2))

    self.play(Write(sub_header))
    self.wait(3)

    self.play(FadeOut(header), FadeOut(header_1), FadeOut(header_2), FadeOut(sub_header))

def TrialDivisionExplanation(self):

    header = Text("Trial Division", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)
    self.play(Create(header))
    self.wait(TIME)
    self.play(FadeOut(header))

    example_header = Text("Example", font="Futura Md BT", font_size=40).move_to(UP*3.4)
    text_1 = Text("N = 5063", **TEXT_ARGS_S)

    self.play(Create(example_header))
    self.wait(TIME)
    self.play(Create(text_1))
    self.wait(TIME)

    self.play(text_1.animate.to_edge(UP + LEFT))

    STEP = UP*0.7

    value_1 = MathTex(r'5063/2=2531.5').move_to(UP)
    value_2 = MathTex(r'5063/3=1687.\dot{6}').move_to(UP-STEP)
    value_3 = MathTex(r'5063/5=1265.75').move_to(UP-2*STEP)
    dots = MathTex(r'\dots').move_to(UP-3*STEP)
    value_4 = MathTex(r'5063/61=83').move_to(UP-4*STEP)
    value_4_2 = MathTex(r'5063/61=83', font_size=80)
    value_4_3 = MathTex(r'5063=83\cdot 61', font_size=80)

    self.play(Create(value_1))
    self.wait(TIME)
    self.play(Create(value_2))
    self.wait(TIME)
    self.play(Create(value_3))
    self.wait(TIME)
    self.play(Create(dots))
    self.wait(TIME)
    self.play(Create(value_4))
    self.wait(TIME)

    self.play(FadeOut(VGroup(value_1, value_2, value_3, dots, example_header, text_1)), Transform(value_4, value_4_2))
    self.play(Transform(value_4, value_4_3))
    self.wait(TIME)

    self.play(Uncreate(value_4))

    header_2 = Text("When to stop?", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)
    text_2 = MathTex(r'\sqrt{N}', font_size=80).next_to(header_2, DOWN, 0.5)

    self.play(Create(header_2))
    self.wait(TIME)
    self.play(Create(text_2))
    self.wait(TIME)

    self.play(FadeOut(text_2), FadeOut(header_2))


def SieveOfEratosthenesExplanation(self):

    header = Text("Sieve of Eratosthenes", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)

    self.play(Create(header))
    self.wait(TIME)
    self.play(FadeOut(header))



    grid = []

    for y in range(10):
        row = []
        for x in range(10):
            cell_size = 0.7
            box = Square(cell_size).move_to(UP*cell_size*(4.5-y)+LEFT*cell_size*(4.5-x))
            text = Text(str(y*10+x + 1), font="Futura Md BT", font_size=16).move_to(box.get_center())
            cell = VGroup(*[box,text])
            row.append(cell)
        grid.append(row)
    
    grid_group = VGroup()

    for row in grid:
        grid_group += VGroup(*row)

    self.play(Create(grid_group))
    self.wait(TIME)

    all_crosses = VGroup()

    def cross_out_multiples(n_list):
        crosses = VGroup()
        for n in n_list:
            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    number = y*10+x + 1
                    if number % n == 0 and number != n :
                        cross = Cross(cell)
                        crosses += cross
        self.play(Create(crosses))
        return crosses
    
    all_crosses += cross_out_multiples([2])
    all_crosses += cross_out_multiples([3])
    all_crosses += cross_out_multiples([5])

    def is_prime(n):
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True

    def get_primes_in_range(start, stop):
        ans = []
        for n in range(start, stop):
            if is_prime(n) :
                ans.append(n)
        return ans


    all_crosses += cross_out_multiples(get_primes_in_range(7, 100 + 1))           

    prime_cells = VGroup()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            number = y*10+x + 1
            if is_prime(number):
                prime_cells += cell
    
    self.bring_to_front(prime_cells)
    self.play(prime_cells.animate.set_color(ACCENT_COLOR))
    self.wait(TIME)

    self.play(FadeOut(grid_group), FadeOut(all_crosses))

    text_1 = MathTex(r'N', font_size=60, color=ACCENT_COLOR)
    text_2 = MathTex(r'\sqrt{N}', font_size=60, color=ACCENT_COLOR).next_to(text_1, DOWN, buff=0.5)

    self.play(Create(text_1))
    self.wait(TIME)
    self.play(Create(text_2))
    self.wait(TIME)

    self.play( *[FadeOut(mob)for mob in self.mobjects] )


def FermatExplanation(self):

    # When building up to the superior factorization algorithms, we have to look at Fermat's Factorization.

    header = Text("Fermat's Factorization", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)

    self.play(Create(header))
    self.wait(TIME)
    self.play(FadeOut(header))

    # Have you ever tried factoring even integers and didn't find any factors? – No?

    number_1 = MathTex(r'6', font_size=60, color=ACCENT_COLOR).move_to(3*LEFT)
    number_2 = MathTex(r'26', font_size=60, color=ACCENT_COLOR)
    number_3 = MathTex(r'768', font_size=60, color=ACCENT_COLOR).move_to(3*RIGHT)
    numbers_group = VGroup(*[number_1, number_2, number_3])

    self.play(Create(numbers_group))
    self.wait(TIME)
    self.play(FadeOut(numbers_group))

    # Well if you have any brain capacity you’d spot the obvious factor, namely 2.

    text_1 = Text("2", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)

    self.play(Create(text_1))
    self.wait(TIME)
    self.play(FadeOut(text_1))

    # That said, finding 2 and its powers is for us humans quite trivial. And It turns out it’s really trivial for computers too.

    self.play(Create(numbers_group))
    self.wait(TIME)

    self.play(
        Transform(number_1, MathTex(r'3\cdot2', font_size=60, color=ACCENT_COLOR).move_to(3*LEFT) ),
        Transform(number_2, MathTex(r'13\cdot2', font_size=60, color=ACCENT_COLOR) ),
        Transform(number_3, MathTex(r'384\cdot2', font_size=60, color=ACCENT_COLOR).move_to(3*RIGHT) )
        )
    self.wait(TIME)
    self.play(
        Transform(number_3, MathTex(r'3\cdot2^8', font_size=60, color=ACCENT_COLOR).move_to(3*RIGHT) )
        )
    self.wait(TIME)

    self.play(FadeOut(numbers_group))

    # After taking care of the powers of two, we’re either done, or what we have left is an odd number.

    text_2_1 = MathTex(r'N=a\cdot b\wedge N\in\text{Odd}')
    text_2_2 = MathTex(r'\Rightarrow a\in\text{Odd}\wedge b\in\text{Odd}')

    text_2_2.move_to(1*DOWN)

    text_2 = VGroup(text_2_1, text_2_2)

    self.play(Create(text_2))
    self.wait(TIME)

    self.play(Uncreate(text_2))

    numline = NumberLine()

    self.play(Create(numline))

    Odd_1 = Dot(RIGHT*3, color=YELLOW, radius= DEFAULT_DOT_RADIUS*2)
    Odd_2 = Dot(LEFT*5, color=YELLOW, radius= DEFAULT_DOT_RADIUS*2)

    Mid = Dot((RIGHT*3+LEFT*5)/2, radius= DEFAULT_DOT_RADIUS*2)

    self.play(Create(Odd_1),Create(Odd_2))
    self.wait(TIME)
    self.play(Create(Mid))
    self.wait(TIME)
    
    text_3_1 = MathTex(r'N=a\cdot b\wedge N\in\text{Odd}').move_to(UP*3)
    text_3_1_2 = MathTex(r'N=(a+b)\cdot (a-b)\wedge N\in\text{Odd}').move_to(UP*3)
    text_3_2_1 = MathTex(r'N=(m-d)\cdot(m-d)').move_to(UP*2)

    text_3_2_2 = MathTex(r'N=m^2-d^2').move_to(text_3_2_1)
    text_3_2_3 = MathTex(r'N+d^2=m^2').move_to(text_3_2_1)

    text_3_2_3_2 = MathTex(r'N+d^2=m^2', font_size=60)

    text_3_2_4 = MathTex(r'N+a^2=b^2', font_size=60)

    self.play(Create(text_3_1), Create(text_3_2_1))
    self.wait(TIME)
    self.play(Transform(text_3_2_1, text_3_2_2))
    self.wait(TIME)
    self.play(Transform(text_3_2_1, text_3_2_3))
    self.wait(TIME)

    self.play(Uncreate(VGroup(Odd_1, Odd_2, Mid, numline)))

    self.play(Transform(text_3_2_1, text_3_2_3_2))
    self.wait(TIME)

    self.play(Transform(text_3_2_1, text_3_2_4))
    self.wait(TIME)
    self.play(Transform(text_3_1, text_3_1_2))
    self.wait(TIME)

    self.play(FadeOut(text_3_1), FadeOut(text_3_2_1))


def FermatExplanationExample(self):

    # 5063
    
    example_header = Text("Example", font="Futura Md BT", font_size=40).move_to(UP*3.4)
    text_1 = Text("N = 5063", **TEXT_ARGS_S)

    self.play(Create(example_header))
    self.wait(TIME)
    self.play(Create(text_1))
    self.wait(TIME)

    self.play(text_1.animate.to_edge(UP + LEFT))
    self.wait(TIME)

    STEP = UP*0.7
    
    value_1 = MathTex(r'5063+1^2=5064').move_to(UP)
    cross_1 = Cross(scale_factor=0.2).next_to(value_1, RIGHT)
    value_2 = MathTex(r'5063+2^2=5067').move_to(UP-STEP)
    cross_2 = Cross(scale_factor=0.2).next_to(value_2, RIGHT)
    value_3 = MathTex(r'5063+3^2=5072').move_to(UP-2*STEP)
    cross_3 = Cross(scale_factor=0.2).next_to(value_3, RIGHT)
    dots = MathTex(r'\dots').move_to(UP-3*STEP)
    value_4 = MathTex(r'5063+11^2=5184').move_to(UP-4*STEP)
    value_4_2 = MathTex(r'5063+11^2=72^2').move_to(UP-4*STEP)
    value_4_3 = MathTex(r'5063+11^2=72^2', font_size = 80)
    value_4_4 = MathTex(r'5063=72^2-11^2', font_size = 80)
    value_4_5 = MathTex(r'5063=(72+11)\cdot (72-11)', font_size = 80)
    value_4_6 = MathTex(r'5063=83\cdot 61', font_size = 80)

    self.play(Create(value_1))
    self.play(Create(cross_1))
    self.wait(TIME)
    self.play(Create(value_2))
    self.play(Create(cross_2))
    self.wait(TIME)
    self.play(Create(value_3))
    self.play(Create(cross_3))
    self.wait(TIME)

    self.play(Create(dots))
    self.wait(TIME)

    self.play(Create(value_4))
    self.wait(TIME)
    self.play(Transform(value_4, value_4_2))
    self.wait(TIME)

    self.play(FadeOut(VGroup(value_1, value_2, value_3, dots, cross_1, cross_2, cross_3)), Transform(value_4, value_4_3))
    self.wait(TIME)
    self.play(Transform(value_4, value_4_4))
    self.wait(TIME)
    self.play(Transform(value_4, value_4_5))
    self.wait(TIME)
    self.play(Transform(value_4, value_4_6))
    self.wait(TIME)
    self.play(*[FadeOut(mob)for mob in self.mobjects])

def KratsKritsExplanation(self):

    header = Text("Kraitchik's Factorization", font="Futura Md BT", font_size=60, color=ACCENT_COLOR)

    self.play(Create(header))
    self.wait(TIME)
    self.play(FadeOut(header))

    text_1 = MathTex(r'N=n_1\cdot n_2', font_size=60)
    text_1_2 = MathTex(r'kN=k\cdot n_1\cdot n_2', font_size=60)
    text_1_3 = MathTex(r'=(a+b)\cdot (a-b)', font_size=60).move_to(DOWN)
    text_1_4 = MathTex(r'gcd(N, a+b)', font_size=60).move_to(RIGHT*3+UP)

    self.play(Create(text_1))
    self.wait(TIME)
    self.play(Transform(text_1, text_1_2))
    self.wait(TIME)
    self.play(Create(text_1_3))
    self.wait(TIME)
    self.remove(text_1)
    self.play(text_1_2.animate.move_to(RIGHT*3), text_1_3.animate.move_to(RIGHT*3+DOWN))
    self.wait(TIME)

    table_h_1 = MathTex(r'a+b', font_size=60).move_to(LEFT*5 + UP*2.5)
    table_h_2 = MathTex(r'a-b', font_size=60).move_to(LEFT*3 + UP*2.5)

    table_r_1_1 = MathTex(r'k\cdot n_1', font_size=40).move_to(LEFT*5 + UP*1.5)
    table_r_1_2 = MathTex(r'n_2', font_size=40).move_to(LEFT*3 + UP*1.5)
    table_r_2_1 = MathTex(r'k\cdot n_2', font_size=40).move_to(LEFT*5 + UP*0.5)
    table_r_2_2 = MathTex(r'n_1', font_size=40).move_to(LEFT*3 + UP*0.5)
    table_r_3_1 = MathTex(r'k', font_size=40).move_to(LEFT*5 + DOWN*0.5)
    table_r_3_2 = MathTex(r'n_1\cdot n_2', font_size=40).move_to(LEFT*3 + DOWN*0.5)
    table_r_4_1 = MathTex(r'\dots', font_size=60).move_to(LEFT*5 + DOWN*1.5)
    table_r_4_2 = MathTex(r'\dots', font_size=60).move_to(LEFT*3 + DOWN*1.5)

    table_separators = VGroup(
        Line(LEFT*6 + DOWN*3, LEFT*6 + UP*3),
        Line(LEFT*4 + DOWN*3, LEFT*4 + UP*3),
        Line(LEFT*2 + DOWN*3, LEFT*2 + UP*3),
        Line(LEFT*6 + UP*2, LEFT*2 + UP*2)
    )

    self.play(Create(table_separators))
    self.play(Create(table_h_1), Create(table_h_2))
    self.wait(TIME)

    self.play(Create(table_r_1_1))
    self.play(Create(table_r_1_2))
    self.wait(TIME)

    self.play(Create(table_r_2_1))
    self.play(Create(table_r_2_2))
    self.wait(TIME)

    self.play(Create(table_r_3_1))
    self.play(Create(table_r_3_2))
    self.wait(TIME)

    self.play(Create(table_r_4_1))
    self.play(Create(table_r_4_2))
    self.wait(TIME)

    self.play(Create(text_1_4))
    self.wait(TIME)

    self.play(
        Transform( table_r_1_1, MathTex(r'n_1', font_size=40).move_to(LEFT*5 + UP*1.5) ),
        Transform( table_r_2_1, MathTex(r'n_2', font_size=40).move_to(LEFT*5 + UP*0.5) ),
        Transform( table_r_3_1, MathTex(r'1', font_size=40).move_to(LEFT*5 + DOWN*0.5) ),
        Transform( table_r_3_2, MathTex(r'N', font_size=40).move_to(LEFT*3 + DOWN*0.5) )
    )
    self.wait(TIME)

    correct = Rectangle(height=2, width=4, stroke_color = GREEN).move_to(LEFT*4+UP)
    self.play(Create(correct), Create(Cross(table_r_3_1)), Create(Cross(table_r_3_2)))
    self.wait(TIME)

    self.play( *[FadeOut(mob)for mob in self.mobjects] )

    text_2 = MathTex(r'N+a^2=b^2', font_size=60)
    text_2_1 = MathTex(r'k\cdotN+a^2=b^2', font_size=60)
    text_2_2 = MathTex(r'a^2\equiv b^2\ (\text{mod}\ N)', font_size=60)

    self.play(Create(text_2))
    self.wait(TIME)
    self.play(Transform(text_2, text_2_1))
    self.wait(TIME)
    self.play(Transform(text_2, text_2_2))
    self.wait(TIME)

    self.play(FadeOut(text_2))

    pass

def QuadraticSieveExplanation(self):

    header = Text("Quadratic Sieve", font="Futura Md BT", font_size=100, color=ACCENT_COLOR)
    self.play(Create(header))
    self.wait(TIME)
    self.play(Uncreate(header))

    bText = Text("B = 13", font="Futura Md BT", font_size=40, color=TEXT_COLOR)
    self.play(FadeIn(bText))

    self.wait(TIME)
    self.play(bText.animate.to_edge(UP + LEFT))
    self.wait(TIME)

    example1first = Text("20")
    example1second = MathTex(r"5\cdot2\cdot2")
    example1first.shift(-DOWN * 0.5)
    self.play(FadeIn(example1first), example1first.animate.shift(DOWN * 0.5))
    self.play(Transform(example1first, example1second))
    self.wait(TIME)
    checkmark = MathTex(r"\checkmark", color=GREEN).next_to(example1first, RIGHT)
    self.play(FadeIn(checkmark))
    self.wait(TIME)
    self.play(FadeOut(example1first), FadeOut(checkmark))


    example2first = Text("34")
    example2second = MathTex(r"17\cdot2")
    example2first.shift(-DOWN * 0.5)
    self.play(FadeIn(example2first), example2first.animate.shift(DOWN * 0.5))
    self.play(Transform(example2first, example2second))
    self.wait(TIME)
    self.play(example2first.animate.set_color(RED))
    self.wait(TIME)
    self.play(FadeOut(example2first))

    algorithmPart1 = CreateTextbox("Finding B-smooth numbers", ACCENT_COLOR).shift(UP * 0.5)
    algorithmPart2 = CreateTextbox("Solve kernels of a matrix", ACCENT2_COLOR)
    algorithmPart2.next_to(algorithmPart1, DOWN, buff=1)

    self.wait(TIME)
    ShowTextbox(self, algorithmPart1)
    self.wait(TIME)
    ShowTextbox(self, algorithmPart2)
    self.wait(TIME)

    self.play(
        algorithmPart1.animate.to_edge(UP),

        algorithmPart2.animate.shift(DOWN),
        FadeOut(algorithmPart2)
    )

    self.wait(TIME)
    self.play(FadeOut(algorithmPart1))
    algorithmPart2.shift(UP)
    self.wait(TIME)

    ############### Part 1 #################

    text1 = MathTex("x^2\ mod\ N \\text{ is B-smooth}", **MATH_ARGS).shift(UP)
    self.play(FadeIn(text1))
    self.wait(TIME)

    nText = Text("N = 1817", **TEXT_ARGS_S)
    self.play(Create(nText))
    self.wait(TIME)
    self.play(nText.animate.to_edge(UP + LEFT).shift(DOWN * 0.75))
    self.wait(TIME)

    guessText = Text("guess = 43", **TEXT_ARGS_S).to_edge(UP + LEFT).shift(DOWN * 1.5)
    self.play(FadeIn(guessText))
    self.wait(TIME)

    part1example = MathTex("34^2\ mod\ 1817", **MATH_ARGS)
    self.play(Create(part1example))
    self.wait(TIME)
    self.play(part1example.animate.shift(LEFT * 2))
    self.wait(TIME)
    part1exampleResult = MathTex("= 32", **MATH_ARGS).next_to(part1example, RIGHT, buff=0.5)
    _temp = MathTex("=\ 2\cdot2\cdot2\cdot2\cdot2", **MATH_ARGS).next_to(part1example, RIGHT, buff=0.5)

    self.play(FadeIn(part1exampleResult))
    self.wait(TIME)
    self.play(Transform(part1exampleResult, _temp))
    self.wait(TIME)

    _newGuess = Text("guess = 44", **TEXT_ARGS_S).move_to(guessText)
    self.play(Transform(guessText, _newGuess))
    self.wait(TIME)

    ############### Sieving ###############

    pauseEffect = Square(1000).set_fill(WHITE, 0.25)
    self.add(pauseEffect)

    self.wait(TIME)

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
    self.wait(TIME)


    pointer = Arrow(start=DOWN, end=UP, color=RED).next_to(primes[0], DOWN)

    self.play(Create(pointer))
    self.wait(TIME)

    temp = Text("2420", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("1 ").move_to(counts[0])))
    self.wait(TIME)

    temp = Text("1210", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("2 ").move_to(counts[0])))
    self.wait(TIME)

    temp = Text("605", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[0], Text("3 ").move_to(counts[0])))
    self.wait(TIME)

    self.play(pointer.animate.next_to(primes[1], DOWN))
    self.play(pointer.animate.next_to(primes[2], DOWN))
    self.wait(TIME)

    temp = Text("121", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[2], Text("1 ").move_to(counts[2])))
    self.wait(TIME)

    self.play(pointer.animate.next_to(primes[3], DOWN))
    self.play(pointer.animate.next_to(primes[4], DOWN))
    self.wait(TIME)

    temp = Text("11", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[4], Text("1 ").move_to(counts[4])))
    self.wait(TIME)

    temp = Text("1", **TEXT_ARGS).move_to(toFactor)
    self.play(Transform(toFactor, temp))
    self.play(Transform(counts[4], Text("2 ").move_to(counts[4])))
    self.wait(TIME)

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
    self.wait(TIME)
    arrow = Arrow(ORIGIN, 2 * RIGHT, color=RED).next_to(primes[-1], DOWN).shift(RIGHT * 0.5)
    self.play(Create(arrow))
    self.wait(TIME)

    self.play(
        FadeOut(morePrimes),
        FadeOut(primes),
        FadeOut(counts),
        Uncreate(toFactor),
        Uncreate(pointer),
        Uncreate(arrow)
    )
    self.wait(TIME)

    self.play(FadeIn(algorithmPart1))
    self.wait(TIME)
    self.play(algorithmPart1.animate.move_to(UP), algorithmPart2.animate.shift(DOWN), FadeIn(algorithmPart2))
    self.wait(TIME)

    self.play(FadeOut(algorithmPart1), algorithmPart2.animate.to_edge(UP))
    self.wait(TIME)
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
    self.wait(TIME)

    highlightBox = Rectangle(GRAY_D, 3.6, 1.1).shift(UP * 1.4 + LEFT * 0.5).set_fill(GRAY_D, 1)
    highlightBox.z_index = 0
    self.play(FadeIn(highlightBox))
    self.play(FadeIn(factoredForms))
    self.wait(TIME)
    self.play(FadeOut(factoredForms))
    self.play(FadeOut(highlightBox))
    self.wait(TIME)

    goal = MathTex("a^2\\equiv b^2\\ mod\\ N", **MATH_ARGS_S).shift(DOWN * 2)
    self.play(Create(goal))

    #self.play(FadeIn(highlightBox))
    #self.play(FadeOut(highlightBox))

    squareExample1 = MathTex("47","^2","\cdot","51","^2", font_size=50, color=BLUE).shift(3*LEFT + DOWN)
    squareExample1_2 = MathTex("(","47","\cdot","51",")","^2", font_size=50, color=BLUE).move_to(squareExample1)

    self.play(FadeIn(squareExample1))
    self.wait(TIME)
    self.play(TransformMatchingTex(squareExample1, squareExample1_2), run_time=2)
    self.wait(TIME)
    self.play(FadeOut(squareExample1_2))
    self.wait(TIME)

    self.play(FadeIn(highlightBox))
    self.play(FadeOut(highlightBox))
    self.wait(TIME)

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
    self.wait(TIME)
    factoredForms.move_to(numbers)
    factoredForms.color = TEXT_COLOR
    self.play(
        TransformMatchingTex(numbers[0], factoredForms[0]),
        TransformMatchingTex(numbers[1], factoredForms[1]),
        TransformMatchingTex(numbers[2], factoredForms[2]),
        TransformMatchingTex(numbers[3], factoredForms[3])
    )
    self.wait(TIME)

    
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
    self.wait(TIME)
    self.play(TransformMatchingTex(squareExample2[0].copy(), squareExample2[1]), run_time=2)
    self.play(TransformMatchingTex(squareExample2[1].copy(), squareExample2[2]), run_time=2)
    self.play(TransformMatchingTex(squareExample2[2].copy(), squareExample2[3]), run_time=2)
    self.wait(TIME)

    self.play(FadeOut(squareExample2))
    self.wait(TIME)

    fullFactoredForms = VGroup(
        MathTex("2^5","\cdot","3^0","\cdot","5^0","\cdot","7^0","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * 1.5),
        MathTex("2^4","\cdot","3^0","\cdot","5^0","\cdot","7^0","\cdot","11^0","\cdot","13^1", **MATH_ARGS).shift(UP * 0.5),
        MathTex("2^3","\cdot","3^0","\cdot","5^0","\cdot","7^2","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * -0.5),
        MathTex("2^4","\cdot","3^0","\cdot","5^0","\cdot","7^2","\cdot","11^0","\cdot","13^0", **MATH_ARGS).shift(UP * -1.5),
    ).move_to(factoredForms)
    for tex in fullFactoredForms:
        tex.set_color_by_tex("0", GRAY_D)

    self.play(TransformMatchingTex(factoredForms, fullFactoredForms), runTime=2)
    self.wait(TIME)

    even = Text("Even", **TEXT_ARGS).shift(RIGHT * 4 + UP * 1.3)
    even.color = RED
    evenMod = MathTex("x\equiv0\ mod\ 2").next_to(even, DOWN, buff=0.5)
    self.play(Create(even))
    self.play(FadeIn(evenMod))
    self.wait(TIME)

    odd = Text("Odd", **TEXT_ARGS).shift(RIGHT * 4 - UP * 1.3)
    odd.color = BLUE
    oddMod = MathTex("x\equiv1\ mod\ 2").next_to(odd, DOWN, buff=0.5)
    self.play(Create(odd))
    self.play(FadeIn(oddMod))
    self.wait(TIME)


    self.play(FadeOut(odd), FadeOut(oddMod), FadeOut(even), FadeOut(evenMod))
    self.play(fullFactoredForms.animate.to_edge(UP + RIGHT))
    self.wait(TIME)

    Xs = VGroup(
        MathTex("x_1", **MATH_ARGS).shift(UP * 1.5),
        MathTex("x_2", **MATH_ARGS).shift(UP * 0.5),
        MathTex("x_3", **MATH_ARGS).shift(UP * -0.5),
        MathTex("x_4", **MATH_ARGS).shift(UP * -1.5),
    ).next_to(fullFactoredForms, LEFT, buff=1.5)
    Xs.color = BLUE

    self.play(FadeIn(Xs))
    self.wait(TIME)

    exponents2 = MathTex("2^5","\ ","2^4","\ ","2^3","\ ","2^4", **MATH_ARGS_S).shift(DOWN * 2)
    exponents2_add = MathTex("5","x_1+","4","x_2+","3","x_3+","4","x_4", **MATH_ARGS_S).move_to(exponents2)
    modulo2Equiv  = MathTex("5","x_1+","4","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(exponents2)
    self.play(TransformMatchingTex(fullFactoredForms.copy(), exponents2))
    self.wait(TIME)
    self.play(TransformMatchingTex(exponents2, exponents2_add))
    self.wait(TIME)
    self.play(TransformMatchingTex(exponents2_add, modulo2Equiv))
    self.wait(TIME)

    modulo2Equiv_simple1  = MathTex("5","x_1+","0","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    modulo2Equiv_simple2  = MathTex("1","x_1+","0","x_2+","3","x_3+","4","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    modulo2Equiv_simple3  = MathTex("1","x_1+","0","x_2+","1","x_3+","0","x_4","\equiv0\ mod\ 2", **MATH_ARGS_S).move_to(modulo2Equiv)
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple1))
    self.wait(TIME)
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple2))
    self.wait(TIME)
    self.play(Transform(modulo2Equiv, modulo2Equiv_simple3))
    self.wait(TIME)

    linearEquations = VGroup(modulo2Equiv)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+0x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)
    linearEquations += MathTex("0x_1+1x_2+0x_3+0x_4\equiv0\ mod\ 2", **MATH_ARGS_S)

    self.play(FadeOut(fullFactoredForms), FadeOut(Xs), FadeOut(modulo2Equiv))
    self.wait(TIME)
    linearEquations.arrange(DOWN).move_to(ORIGIN)
    self.play(Create(linearEquations))
    self.wait(TIME)

    mat = Matrix([[1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])


    self.play(FadeOut(linearEquations))
    self.play(FadeIn(mat))
    self.wait(TIME)

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
    self.wait(TIME)

    highlight = SurroundingRectangle(mat.get_entries()[3 * 4 + 1])
    self.play(Create(highlight))
    self.wait(TIME)
    self.play(Uncreate(highlight))
    self.wait(TIME)

    image = ImageMobject("findKernelVideo.png")
    image.scale(2)
    image.shift(DOWN * 6)

    self.add(image)
    self.play(image.animate.shift(UP * 6))
    self.wait(TIME)
    self.play(image.animate.shift(DOWN * 6))
    self.wait(TIME)


    solutionVec = VGroup(
        MathTex("1", **MATH_ARGS),
        MathTex("0", **MATH_ARGS),
        MathTex("1", **MATH_ARGS),
        MathTex("0", **MATH_ARGS)
    ).arrange(RIGHT, buff=1.0).move_to(Xs)
    solutionVec.color = BLUE

    self.play(Transform(Xs, solutionVec))
    self.wait(TIME)

    self.play(FadeOut(Xs), FadeOut(primes), FadeOut(mat))
    numbers.move_to(ORIGIN)
    self.play(FadeIn(numbers))
    self.wait(TIME)

    takenNums = VGroup( MathTex("\\ 32", **MATH_ARGS),MathTex("392", **MATH_ARGS)).arrange(DOWN, buff=0.5)
    self.play(TransformMatchingTex(numbers, takenNums))
    self.play(takenNums[0].animate.set_color(RED), takenNums[1].animate.set_color(ORANGE))
    self.wait(TIME)

    self.play(takenNums.animate.shift(UP * 2))
    self.wait(TIME)

    finalEq = MathTex("43^2","\cdot ","47^2","\equiv ","2^5","\cdot ","2^3\cdot 7^2","\ mod\ 1817", **MATH_ARGS)
    finalEq.set_color_by_tex_to_color_map({"2^5": RED, "43^2": RED, "2^3\cdot 7^2": ORANGE, "47^2": ORANGE})
    finalEq_2 = MathTex("(43\cdot 47)^2\equiv (2^4\cdot 7^1)^2\ mod\ 1817", **MATH_ARGS).next_to(finalEq, DOWN, buff=0.5)

    goal.next_to(finalEq_2, DOWN, buff=1)
    gdc = MathTex("gdc(N,\ a-b)", **MATH_ARGS_S).move_to(goal).shift(RIGHT * 2)
    goal.shift(LEFT * 2)

    goal.color = BLUE
    gdc.color = BLUE

    self.play(Create(finalEq))
    self.wait(TIME)
    self.play(Create(finalEq_2))
    self.wait(TIME)
    self.play(FadeIn(goal))
    self.wait(TIME)
    self.play(FadeIn(gdc))
    self.wait(TIME)

    self.play(FadeOut(takenNums))

    solution1 = Text(" X   Y = 1817 ", font="Futura Md BT").shift(UP * 2)
    solution2 = Text("  X   23 = 1817", font="Futura Md BT").move_to(solution1)
    solution3 = Text("79   23 = 1817", font="Futura Md BT").move_to(solution1)

    dot = Text("⋅").move_to(solution1).shift(LEFT * 1.3)

    self.play(FadeIn(solution1), FadeIn(dot))
    self.wait(TIME)
    self.play(Transform(solution1, solution2), dot.animate.shift(LEFT *  0.2))
    self.wait(TIME)
    self.play(Transform(solution1, solution3), dot.animate.shift(LEFT * -0.2))
    self.wait(TIME)


    self.play(Uncreate(solution1), FadeOut(dot), FadeOut(gdc), FadeOut(goal), FadeOut(finalEq), FadeOut(finalEq_2))
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
    self.wait(TIME)
    ShowTextbox(self, tower[1])
    self.wait(TIME)
    ShowTextbox(self, tower[2])
    self.wait(TIME)

    ShowTextbox(self, tower[3][0][0])
    self.wait(TIME)
    ShowTextbox(self, tower[3][0][1])
    self.wait(TIME)
    ShowTextbox(self, tower[3][0][2])
    CreateArrow(tower[3][0])

    ShowTextbox(self, tower[3][1])
    self.wait(TIME)
    self.play(FadeIn(matVisual))
    self.wait(TIME)
    self.play(FadeOut(matVisual))

    ShowTextbox(self, tower[3][2][0])
    self.wait(TIME)
    ShowTextbox(self, tower[3][2][1])
    gdc = MathTex("gdc(N,\ a-b)", **MATH_ARGS_S).shift(RIGHT * 2.5)
    gdc.color = BLUE
    self.play(FadeIn(gdc))
    CreateArrow(tower[3][2])
    self.wait(TIME)
    ShowTextbox(self, tower[3][3])
    CreateArrow(tower[3])
    self.play(FadeOut(gdc))
    self.wait(TIME)

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
    self.wait(TIME)
    self.remove(tower)

    self.play( FadeOut(pickGuess), FadeOut(pickData), pickB.animate.move_to(ORIGIN).to_edge(UP))
    self.wait(TIME)

    bFormula = MathTex("B=(e^{\sqrt{\ln(N)\ln(\ln N)}})^{\\frac{1}{\sqrt{2}}}", **MATH_ARGS)
    self.play(Create(bFormula))
    self.wait(TIME)
    self.play(FadeOut(bFormula))

    self.play(FadeIn(pickGuess), FadeIn(pickData), pickB.animate.to_edge(UP + LEFT))
    self.wait(TIME)
    self.play( FadeOut(pickData), pickGuess.animate.move_to(ORIGIN).to_edge(UP), FadeOut(pickB))
    self.wait(TIME)

    guessFormula = MathTex("guess=\lceil \sqrt{N}\\rceil", **MATH_ARGS)
    guessCalc = MathTex("x=guess^2\ mod\ N", **MATH_ARGS).next_to(guessFormula, DOWN)

    self.play(FadeIn(guessCalc))
    self.wait(TIME)
    self.play(Create(guessFormula))
    self.wait(TIME)

    self.play(FadeOut(guessCalc), FadeOut(guessFormula))

    self.play(FadeIn(pickB), FadeIn(pickData), pickGuess.animate.move_to(ORIGIN).to_edge(UP))
    self.wait(TIME)
    self.play( FadeOut(pickB), pickData.animate.move_to(ORIGIN).to_edge(UP), FadeOut(pickGuess))
    self.wait(TIME)

    dataFormula = MathTex("\\text{amountTo}(B)+5")
    self.play(FadeIn(dataFormula))
    self.wait(TIME)
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
    self.wait(TIME)
    self.play(FadeOut(matVisual))
    self.wait(TIME)

    self.play(originalTower.animate.arrange(DOWN, buff=scalar * buffer).to_edge(UP + LEFT))
    self.play(originalTower[4].animate.shift(RIGHT * 0.5))
    self.wait(TIME)

    eulerCheck = MathTex("N^{\\frac{p-1}{2}}mod\ p", **MATH_ARGS).shift(RIGHT * 2)
    self.play(Create(eulerCheck))
    self.wait(TIME)
    self.play(FadeOut(eulerCheck))


    self.play(FadeIn(matVisual))
    self.wait(TIME)

    highlight1 = Rectangle(GRAY_D, 1.15, 3.6).shift(RIGHT * 2.4 + UP * 0.45).set_fill(GRAY_D, 1)
    highlight2 = Rectangle(GRAY_D, 0.6, 3.6).shift(RIGHT * 2.4 + DOWN * 1.05).set_fill(GRAY_D, 1)
    matVisual.z_index = 1
    highlight1.z_index = 0
    highlight2.z_index = 0

    self.play(FadeIn(highlight1), FadeIn(highlight2))
    self.wait(TIME)
    self.play(FadeOut(highlight1), FadeOut(highlight2))
    self.wait(TIME)

    self.play(FadeOut(matVisual))
    self.play(originalTower.animate.move_to(ORIGIN))