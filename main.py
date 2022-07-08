from PIL import Image, ImageDraw

class LampScreen:
    gridcolor = (76, 45, 28)
    offcolor = (173, 101, 62)
    oncolor = (242, 201, 159)

    def __init__(self, sx, sy):
        self.image = None
        self.set_size(sx, sy)

    def set_size(self, sx, sy):
        self.image = Image.new("RGB", (sx * 10, sy * 10), color=LampScreen.gridcolor)

        for x in range(0, sx):
            for y in range(0, sy):
                self.draw_pixel(x, y, False)

    def draw_pixel(self, x, y, on=True):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle((x * 10, y * 10, x * 10 + 8, y * 10 + 8), LampScreen.oncolor if on else LampScreen.offcolor)

    def display(self):
        transposed = self.image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
        transposed.show()


def main():
    # Initialize screen with size 64 x 64
    my_screen = LampScreen(64, 64)

    # Draw pixels
    my_screen.draw_pixel(20, 30)
    my_screen.draw_pixel(2, 2)

    # Display
    my_screen.display()





if __name__ == '__main__':
    main()