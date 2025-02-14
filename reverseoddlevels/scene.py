from manim import *


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ReverseOddLevels(Scene):
    def reverse(self, root):
        if root == None or root.left == None or root.right == None:
            return

        root.val[2].set_fill(BLUE)
        self.wait(0.3)
        self.reverse_helper(root.left, root.right, True)

    def reverse_helper(self, left, right, flag):
        if left == None or right == None:
            return

        self.play(
            left.val[2].animate.set_fill(BLUE),
            right.val[2].animate.set_fill(BLUE),
        )

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
        l.set_z_index(2)

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
                ll.set_z_index(2)
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
                lr.set_z_index(2)
                line = Line(curr.val[2].get_center(), cr.get_center())
                line.set_z_index(0)
                anims.append(Create(cr))
                anims.append(Write(lr))
                anims.append(Create(line))

                curr.right = TreeNode([nodes[i], level, cr, lr])
                queue.append(curr.right)

            i += 1

        self.play(AnimationGroup(*anims, lag_ratio=0.1))
        self.wait(1)

        self.reverse(root)
