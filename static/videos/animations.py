from manim import *

class CHSHGame(Scene):
    def construct(self):
        eqn_x = Tex("$x$", font_size=80, color=ORANGE).to_corner(UP+LEFT).shift(DOWN)
        eqn_cdot = Tex("$\cdot$", font_size=80, color=ORANGE).next_to(eqn_x, RIGHT)
        eqn_y = Tex("$y$", font_size=80, color=ORANGE).next_to(eqn_cdot, RIGHT)
        eqn_equal = Tex("$\stackrel{?}{=}$", font_size=80, ).next_to(eqn_y, RIGHT)
        eqn_a = Tex("$a$", font_size=80, color=BLUE).next_to(eqn_equal, RIGHT)
        eqn_xor = Tex("$\oplus$", font_size=80, color=BLUE).next_to(eqn_a, RIGHT)
        eqn_b = Tex("$b$", font_size=80, color=BLUE).next_to(eqn_xor, RIGHT)
        
        step1 = Text("Step 1:").to_corner(UP+LEFT)
        step2 = Text("Step 2:").to_corner(UP+LEFT)
        step3 = Text("Step 3:").to_corner(UP+LEFT)
        
        Alice = Text("Alice").shift(2*DOWN+4*LEFT)
        Bob = Text("Bob").shift(2*DOWN+4*RIGHT)
        Carol = Text("Carol").shift(UP)
        self.play(
            LaggedStart(Write(Alice)),
            LaggedStart(Write(Bob)),
            LaggedStart(Write(Carol)),
        )
        self.wait(2)
        
        # Step 1
        arrow_x = Arrow(start=Carol.get_bottom(), end=Alice.get_top()+RIGHT, color=ORANGE)
        arrow_y = Arrow(start=Carol.get_bottom(), end=Bob.get_top()+LEFT, color=ORANGE)
        label_x = Tex("$x$", font_size=80, color=ORANGE).move_to(arrow_x.get_midpoint()+LEFT)
        label_y = Tex("$y$", font_size=80, color=ORANGE).move_to(arrow_y.get_midpoint()+RIGHT)
        self.play(
            Write(step1),
        )
        self.play(
            LaggedStart(Create(arrow_x)),
            LaggedStart(Create(arrow_y)),
            LaggedStart(Write(label_x)),
            LaggedStart(Write(label_y)),
        )
        self.wait(2)
        arrow_a = Arrow(start=Alice.get_top(), end=Carol.get_bottom()+LEFT, color=BLUE)
        arrow_b = Arrow(start=Bob.get_top(), end=Carol.get_bottom()+RIGHT, color=BLUE)
        label_a = Tex("$a$", font_size=80, color=BLUE).move_to(arrow_a.get_midpoint()+RIGHT)
        label_b = Tex("$b$", font_size=80, color=BLUE).move_to(arrow_b.get_midpoint()+LEFT)
        self.play(
            LaggedStart(Uncreate(arrow_x)),
            LaggedStart(Uncreate(arrow_y)),
        )
        self.play(
            ReplacementTransform(label_x, eqn_x),
            ReplacementTransform(label_y, eqn_y),
            Write(eqn_cdot),
        )
        self.wait(2)
        
        # Step 2
        self.play(
            ReplacementTransform(step1, step2),
        )
        self.play(
            LaggedStart(Create(arrow_a)),
            LaggedStart(Create(arrow_b)),
            LaggedStart(Write(label_a)),
            LaggedStart(Write(label_b)),
        )
        self.wait(2)
        self.play(
            LaggedStart(Uncreate(arrow_a)),
            LaggedStart(Uncreate(arrow_b)),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(label_a, eqn_a),
            ReplacementTransform(label_b, eqn_b),
            Write(eqn_xor),
        )
        self.wait(2)
        
        # Step 3
        self.play(
            ReplacementTransform(step2, step3),
        )
        self.play(
            Write(eqn_equal),
        )
        self.wait(2)
        self.play(
            LaggedStart(FadeOut(Alice)),
            LaggedStart(FadeOut(Bob)),
            LaggedStart(FadeOut(Carol)),
            LaggedStart(FadeOut(eqn_x)),
            LaggedStart(FadeOut(eqn_cdot)),
            LaggedStart(FadeOut(eqn_y)),
            LaggedStart(FadeOut(eqn_equal)),
            LaggedStart(FadeOut(eqn_a)),
            LaggedStart(FadeOut(eqn_xor)),
            LaggedStart(FadeOut(eqn_b)),
            LaggedStart(FadeOut(step3)),
        )
