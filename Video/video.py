from tkinter import font
from manim import *

# Background color defined in manim.cfg
TEXT_COLOR = GRAY_A
ACCENT_COLOR = BLUE
ACCENT2_COLOR = ORANGE


class CreateVideo(Scene):
    def construct(self):
        #StartExplanation(self)
        #FermatExplanation(self)
        #KratsKritsExplanation(self)
        QuadraticSieveExplanation(self)
        #OptimizeExplanation(self)
        

def CreateTextbox(string: str, color) -> VGroup:
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=1.25, width=9, fill_color=color, 
        fill_opacity=0.1, stroke_color=color
    )
    text = Text(string, font="Futura Md BT", font_size=50).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result

def StartExplanation(self):
    pass

def FermatExplanation(self):
    pass

def KratsKritsExplanation(self):
    pass

def QuadraticSieveExplanation(self):
    header = Text("Quadratic Sieve", font="Futura Md BT", font_size=100, color=ACCENT_COLOR)
    self.play(Create(header))
    self.wait(1)
    self.play(Uncreate(header))

    bText = Text("B = 13", font="Futura Md BT", font_size=50, color=TEXT_COLOR)
    self.play(FadeIn(bText))

    self.wait(1)
    self.play(bText.animate.to_edge(UP + LEFT))
    self.wait()

    example1first = Text("20")
    example1second = MathTex(r"5\cdot2\cdot2")
    example1first.shift(-DOWN * 0.5)
    self.play(FadeIn(example1first), example1first.animate.shift(DOWN * 0.5))
    self.play(Transform(example1first, example1second))
    self.wait(1)
    checkmark = MathTex(r"\checkmark", color=GREEN).shift(RIGHT)
    self.play(FadeIn(checkmark))
    self.wait(1)
    self.play(FadeOut(example1first), FadeOut(checkmark))


    example2first = Text("34")
    example2second = MathTex(r"17\cdot2")
    example2first.shift(-DOWN * 0.5)
    self.play(FadeIn(example2first), example2first.animate.shift(DOWN * 0.5))
    self.play(Transform(example2first, example2second))
    self.wait(1)
    self.play(example2first.animate.set_color(RED))
    self.wait(1)
    self.play(FadeOut(example2first))

    algorithmPart1 = CreateTextbox("Finding B-smooth numbers", ACCENT_COLOR).shift(UP * 0.5)
    algorithmPart2 = CreateTextbox("Solve kernels of a matrix", ACCENT2_COLOR)
    algorithmPart2.next_to(algorithmPart1, DOWN, buff=1)

    self.play(DrawBorderThenFill(algorithmPart1))
    self.play(DrawBorderThenFill(algorithmPart2))

    self.play(algorithmPart1.animate.scale(10))

    self.wait()




    

def OptimizeExplanation(self):
    pass