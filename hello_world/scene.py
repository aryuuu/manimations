from manim import *

class FourSquares(Scene):
    def construct(self):
        
        title = Text("""
        Kagebunshin
        """, font="Monocraft", color=GREY)

        final_shape = Circle()
        final_shape.set_fill(WHITE, opacity=.7)

        square_one = Square()
        square_one.set_fill(BLUE, opacity=.5)
        square_two = Square()
        square_two.set_fill(PINK, opacity=.5)
        square_three = Square()
        square_three.set_fill(GREEN, opacity=.5)
        square_three.shift(UP)
        square_four = Square()
        square_four.set_fill(RED, opacity=.5)
        square_four.shift(DOWN)
        square_one.is_off_screen

        # self.play(Create(square_one), Create(square_two))
        self.play(Write(title))
        self.play(ReplacementTransform(title, square_one))
        # self.play(Create(square_one))
        self.play(
            square_one.animate.shift(UP),
            square_two.animate.shift(DOWN),
        )
        self.play(
            square_one.animate.shift(LEFT),
            square_two.animate.shift(LEFT),
            square_three.animate.shift(RIGHT),
            square_four.animate.shift(RIGHT),
        )
        self.play(
            Rotate(square_one, PI / 4),
            Rotate(square_two, -PI / 4),
            Rotate(square_three, PI/ 4),
            Rotate(square_four, -PI/ 4),
        )
        self.play(
            square_one.animate.become(final_shape),
            square_two.animate.become(final_shape),
            square_three.animate.become(final_shape),
            square_four.animate.become(final_shape),
        )
