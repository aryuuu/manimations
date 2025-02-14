from manim import *
from manim.typing import Point3D


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ReverseOddLevels(Scene):
    def reverse(self, root):
        if root == None or root.left == None or root.right == None:
            return

        root.val[2].set_fill(GREEN)
        self.wait(.3)
        self.reverse_helper(root.left, root.right, True)

    def reverse_helper(self, left, right, flag):
        if left == None or right == None:
            return

        if flag:
            self.play(
                left.val[3].animate.move_to(right.val[3].get_center()),
                right.val[3].animate.move_to(left.val[3].get_center()),
            )
            self.play(
                left.val[2].animate.set_fill(GREEN),
                right.val[2].animate.set_fill(GREEN),
            )
            # self.wait(.3)

            left.val[0], right.val[0] = right.val[0], left.val[0]
            left.val[3], right.val[3] = right.val[3], left.val[3]

        self.reverse_helper(left.left, right.right, not flag)
        self.reverse_helper(right.left, left.right, not flag)

    def construct(self):

        RADIUS = 0.25
        FONT_SIZE = 18
        FILL_OPACITY = 1
        ROOT_X = 0
        ROOT_Y = 3

        X_HOP = 3
        Y_HOP = 1

        NODE_LINE_COLOR = WHITE
        BASE_NODE_COLOR = GRAY
        EVAL_NODE_COLOR = YELLOW

        # this is a perfect binary tree
        nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        # init the binary tree
        c = (
            Circle(RADIUS, color=NODE_LINE_COLOR)
            .move_to([ROOT_X, ROOT_Y, 1])
            .set_fill(BASE_NODE_COLOR, opacity=FILL_OPACITY)
        )
        c.set_z_index(1)
        l = Text(str(nodes[0]), font_size=FONT_SIZE).move_to(c.get_center())
        l.set_z_index(1)

        # val, level, circle, label
        root = TreeNode([nodes[0], 0, c, l])
        queue = [root]
        anims = [Create(c), Write(l)]
        i = 1
        while len(queue) > 0 and i < len(nodes):
            curr = queue.pop(0)
            level = curr.val[1] + 1

            # add left child
            if i < len(nodes):
                cl = (
                    Circle(RADIUS, color=NODE_LINE_COLOR)
                    .move_to(
                        [
                            curr.val[2].get_x() - (X_HOP / (2**level)),
                            ROOT_Y - (level * Y_HOP),
                            1,
                        ]
                    )
                    .set_fill(BASE_NODE_COLOR, opacity=FILL_OPACITY)
                )
                cl.set_z_index(1)
                ll = Text(str(nodes[i]), font_size=FONT_SIZE).move_to(cl.get_center())
                ll.set_z_index(1)
                line = Line(curr.val[2].get_center(), cl.get_center())
                line.set_z_index(0)
                anims.append(Create(cl))
                anims.append(Write(ll))
                anims.append(Create(line))

                curr.left = TreeNode([nodes[i], level, cl, ll])
                queue.append(curr.left)

            i += 1

            # add right child
            if i < len(nodes):
                cr = (
                    Circle(RADIUS, color=NODE_LINE_COLOR)
                    .move_to(
                        [
                            curr.val[2].get_x() + (X_HOP / (2**level)),
                            ROOT_Y - (level * Y_HOP),
                            1,
                        ]
                    )
                    .set_fill(BASE_NODE_COLOR, opacity=FILL_OPACITY)
                )
                cr.set_z_index(1)
                lr = Text(str(nodes[i]), font_size=FONT_SIZE).move_to(cr.get_center())
                lr.set_z_index(1)
                line = Line(curr.val[2].get_center(), cr.get_center())
                line.set_z_index(0)
                anims.append(Create(cr))
                anims.append(Write(lr))
                anims.append(Create(line))

                curr.right = TreeNode([nodes[i], level, cr, lr])
                queue.append(curr.right)

            i += 1

        # 
        self.play(AnimationGroup(*anims, lag_ratio=.1))
        self.wait(1)

        self.reverse(root)

        # input_shapes = []
        # input_labels = []
        # output_shapes = []
        # output_labels = []
        # init_anims = []
        # for i, val in enumerate(input_list):
        #     in_square = (
        #         Square(side_length=SIDE, color=INPUT_BASE_COLOR)
        #         .move_to([INPUT_LIST_START_X + (i * SIDE), INPUT_LIST_START_Y, 0])
        #         .set_fill(INPUT_BASE_COLOR, opacity=FILL_OPACITY)
        #     )
        #     input_shapes.append(in_square)
        #     in_label = Text(str(val), font_size=FONT_SIZE).move_to(
        #         in_square.get_center()
        #     )
        #     input_labels.append(in_label)

        #     out_square = (
        #         Square(side_length=SIDE, color=OUTPUT_BASE_COLOR)
        #         .move_to([OUTPUT_LIST_START_X + (i * SIDE), OUTPUT_LIST_START_Y, 0])
        #         .set_fill(OUTPUT_BASE_COLOR, opacity=FILL_OPACITY)
        #     )
        #     output_shapes.append(out_square)
        #     out_label = Text(str(output_list[i]), font_size=FONT_SIZE).move_to(
        #         out_square.get_center()
        #     )
        #     output_labels.append(out_label)

        #     init_anims.append(Create(in_square))
        #     init_anims.append(Create(out_square))
        #     init_anims.append(Write(in_label))
        #     init_anims.append(Write(out_label))

        # self.play(AnimationGroup(*init_anims, lag_ratio=0.03))

        # # highlight last item
        # curr_in = input_shapes[len(input_shapes) - 1]
        # curr_out = output_shapes[len(output_shapes) - 1]
        # curr_in.set_color(INPUT_CURR_COLOR).set_fill(
        #     INPUT_CURR_COLOR, opacity=FILL_OPACITY
        # )
        # curr_out.set_color(OUTPUT_CURR_COLOR).set_fill(
        #     OUTPUT_CURR_COLOR, opacity=FILL_OPACITY
        # )
        # self.wait(0.5)

        # # init the stack
        # stack.append(len(input_list) - 1)
        # stack_shapes = []
        # stack_labels = []

        # s = (
        #     Square(side_length=SIDE, color=STACK_BASE_COLOR)
        #     .move_to([STACK_LIST_START_X, STACK_LIST_START_Y, 0])
        #     .set_fill(STACK_BASE_COLOR, opacity=FILL_OPACITY)
        # )
        # stack_shapes.append(s)
        # l = Text(str(input_list[stack[0]]), font_size=FONT_SIZE).move_to(s.get_center())
        # stack_labels.append(l)

        # self.play(AnimationGroup(*[Create(s), Write(l)], lag_ratio=0.1))
        # self.wait(0.1)

        # # here goes the meat
        # for i in range(len(input_list) - 2, -1, -1):
        #     input_shapes[i + 1].set_color(INPUT_CURR_COLOR).set_fill(
        #         INPUT_DONE_COLOR, opacity=FILL_OPACITY
        #     )
        #     output_shapes[i + 1].set_color(OUTPUT_CURR_COLOR).set_fill(
        #         OUTPUT_DONE_COLOR, opacity=FILL_OPACITY
        #     )
        #     input_shapes[i].set_color(INPUT_CURR_COLOR).set_fill(
        #         INPUT_CURR_COLOR, opacity=FILL_OPACITY
        #     )
        #     output_shapes[i].set_color(OUTPUT_CURR_COLOR).set_fill(
        #         OUTPUT_CURR_COLOR, opacity=FILL_OPACITY
        #     )

        #     while len(stack) > 0 and input_list[stack[len(stack) - 1]] <= input_list[i]:
        #         # mark top as red
        #         stack_shapes[len(stack) - 1].set_color(STACK_BAD_COLOR).set_fill(
        #             STACK_BAD_COLOR, opacity=FILL_OPACITY
        #         )
        #         self.play(
        #             AnimationGroup(
        #                 *[
        #                     FadeOut(stack_labels[len(stack) - 1]),
        #                     FadeOut(stack_shapes[len(stack) - 1]),
        #                 ]
        #             )
        #         )

        #         # pop it out
        #         stack_shapes.pop()
        #         stack_labels.pop()
        #         stack.pop()

        #     if len(stack) > 0:
        #         updated = Text(
        #             str(stack[len(stack) - 1] - i), font_size=FONT_SIZE
        #         ).move_to(output_labels[i])
        #         self.play(Transform(output_labels[i], updated))
        #         self.wait(0.2)

        #     new_top = (
        #         Square(side_length=SIDE, color=STACK_BASE_COLOR)
        #         .move_to(
        #             [
        #                 STACK_LIST_START_X,
        #                 STACK_LIST_START_Y + (len(stack) * SIDE),
        #                 0,
        #             ]
        #         )
        #         .set_fill(STACK_BASE_COLOR, opacity=FILL_OPACITY)
        #     )
        #     stack_shapes.append(new_top)
        #     new_label = Text(str(input_list[i]), font_size=FONT_SIZE).move_to(
        #         new_top.get_center()
        #     )
        #     stack_labels.append(new_label)
        #     stack.append(i)

        #     self.play(
        #         AnimationGroup(*[FadeIn(new_top), Write(new_label)], lag_ratio=0.1)
        #     )
        #     self.wait(0.1)

        # self.wait(1)
