from manim import *


class MonotonicStack(Scene):
    def construct(self):

        SIDE = 0.5
        FONT_SIZE = 18
        FILL_OPACITY = 0.5

        INPUT_CURR_COLOR = YELLOW
        INPUT_DONE_COLOR = GREEN
        INPUT_BASE_COLOR = GRAY
        INPUT_SELECTED_COLOR = BLUE
        INPUT_LIST_START_X = -5
        INPUT_LIST_START_Y = 0

        OUTPUT_CURR_COLOR = YELLOW
        OUTPUT_DONE_COLOR = GREEN
        OUTPUT_BASE_COLOR = GRAY
        OUTPUT_LIST_START_X = -5
        OUTPUT_LIST_START_Y = -2

        STACK_TOP_COLOR = YELLOW
        STACK_GOOD_COLOR = GREEN
        STACK_BAD_COLOR = RED
        STACK_BASE_COLOR = GRAY
        STACK_LIST_START_X = 2
        STACK_LIST_START_Y = -2

        input_list = [73, 74, 75, 71, 69, 72, 76, 73]
        output_list = [0 for _ in range(len(input_list))]
        stack = []

        # init input array, output array, and the stack

        input_shapes = []
        input_labels = []
        output_shapes = []
        output_labels = []
        init_anims = []
        for i, val in enumerate(input_list):
            in_square = (
                Square(side_length=SIDE, color=INPUT_BASE_COLOR)
                .move_to([INPUT_LIST_START_X + (i * SIDE), INPUT_LIST_START_Y, 0])
                .set_fill(INPUT_BASE_COLOR, opacity=FILL_OPACITY)
            )
            input_shapes.append(in_square)
            in_label = Text(str(val), font_size=FONT_SIZE).move_to(
                in_square.get_center()
            )
            input_labels.append(in_label)

            out_square = (
                Square(side_length=SIDE, color=OUTPUT_BASE_COLOR)
                .move_to([OUTPUT_LIST_START_X + (i * SIDE), OUTPUT_LIST_START_Y, 0])
                .set_fill(OUTPUT_BASE_COLOR, opacity=FILL_OPACITY)
            )
            output_shapes.append(out_square)
            out_label = Text(str(output_list[i]), font_size=FONT_SIZE).move_to(
                out_square.get_center()
            )
            output_labels.append(out_label)

            init_anims.append(Create(in_square))
            init_anims.append(Create(out_square))
            init_anims.append(Write(in_label))
            init_anims.append(Write(out_label))

        self.play(AnimationGroup(*init_anims, lag_ratio=0.03))

        # highlight last item
        curr_in = input_shapes[len(input_shapes) - 1]
        curr_out = output_shapes[len(output_shapes) - 1]
        curr_in.set_color(INPUT_CURR_COLOR).set_fill(
            INPUT_CURR_COLOR, opacity=FILL_OPACITY
        )
        curr_out.set_color(OUTPUT_CURR_COLOR).set_fill(
            OUTPUT_CURR_COLOR, opacity=FILL_OPACITY
        )
        self.wait(0.5)

        # init the stack
        stack.append(len(input_list) - 1)
        stack_shapes = []
        stack_labels = []

        s = (
            Square(side_length=SIDE, color=STACK_BASE_COLOR)
            .move_to([STACK_LIST_START_X, STACK_LIST_START_Y, 0])
            .set_fill(STACK_BASE_COLOR, opacity=FILL_OPACITY)
        )
        stack_shapes.append(s)
        l = Text(str(input_list[stack[0]]), font_size=FONT_SIZE).move_to(s.get_center())
        stack_labels.append(l)

        self.play(AnimationGroup(*[Create(s), Write(l)], lag_ratio=0.1))
        self.wait(0.1)

        # here goes the meat
        for i in range(len(input_list) - 2, -1, -1):
            input_shapes[i + 1].set_color(INPUT_CURR_COLOR).set_fill(
                INPUT_DONE_COLOR, opacity=FILL_OPACITY
            )
            output_shapes[i + 1].set_color(OUTPUT_CURR_COLOR).set_fill(
                OUTPUT_DONE_COLOR, opacity=FILL_OPACITY
            )
            input_shapes[i].set_color(INPUT_CURR_COLOR).set_fill(
                INPUT_CURR_COLOR, opacity=FILL_OPACITY
            )
            output_shapes[i].set_color(OUTPUT_CURR_COLOR).set_fill(
                OUTPUT_CURR_COLOR, opacity=FILL_OPACITY
            )

            while len(stack) > 0 and input_list[stack[len(stack) - 1]] <= input_list[i]:
                # mark top as red
                stack_shapes[len(stack) - 1].set_color(STACK_BAD_COLOR).set_fill(
                    STACK_BAD_COLOR, opacity=FILL_OPACITY
                )
                self.play(
                    AnimationGroup(
                        *[
                            FadeOut(stack_labels[len(stack) - 1]),
                            FadeOut(stack_shapes[len(stack) - 1]),
                        ]
                    )
                )

                # pop it out
                stack_shapes.pop()
                stack_labels.pop()
                stack.pop()

            if len(stack) > 0:
                updated = Text(
                    str(stack[len(stack) - 1] - i), font_size=FONT_SIZE
                ).move_to(output_labels[i])
                self.play(Transform(output_labels[i], updated))
                self.wait(0.2)

            new_top = (
                Square(side_length=SIDE, color=STACK_BASE_COLOR)
                .move_to(
                    [
                        STACK_LIST_START_X,
                        STACK_LIST_START_Y + (len(stack) * SIDE),
                        0,
                    ]
                )
                .set_fill(STACK_BASE_COLOR, opacity=FILL_OPACITY)
            )
            stack_shapes.append(new_top)
            new_label = Text(str(input_list[i]), font_size=FONT_SIZE).move_to(
                new_top.get_center()
            )
            stack_labels.append(new_label)
            stack.append(i)

            self.play(
                AnimationGroup(*[FadeIn(new_top), Write(new_label)], lag_ratio=0.1)
            )
            self.wait(0.1)

        self.wait(1)
