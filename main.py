from PIL import Image, ImageDraw


class LampColor(object):
    """red stone lamp color table.
    You can change the RGB color number before drawing to customize the picture style.
    """

    gridcolor = (76, 45, 28)  # Grid color
    offcolor = (173, 101, 62)  # Redstone lamp non-activated color
    oncolor = (242, 201, 159)  # Redstone lamp activated color


class LampScreen:
    activated_list: set[tuple[int, int]]
    screenX: int
    screenY: int
    scale: int
    grid_width: int

    def __init__(self, screenX: int, screenY: int, scale: int, grid_width: int) -> None:
        self.scale = scale
        self.grid_width = grid_width
        self.activated_list = set()  # Initialize active pixel record
        self.set_size(screenX, screenY)  # Set screen size
        self.clear()  # Clear screen

    def clear(self) -> None:
        self.activated_list.clear()  # Clear active pixels

    def set_size(self, screenX: int, screenY: int) -> None:
        self.screenX = screenX  # Settings screen X
        self.screenY = screenY  # Settings screen Y

    def pixel_is_active(self, point: tuple[int, int]) -> bool:
        return point in self.activated_list

    def erase_pixel(self, point: tuple[int, int]) -> None:
        if self.pixel_is_active(point):
            self.activated_list.remove(point)

    def draw_pixel(self, point: tuple[int, int]) -> None:
        if not self.pixel_is_active(point):
            self.activated_list.add(point)

    def build(self) -> Image.Image:
        scale = self.scale
        grid_width = self.grid_width

        Width = self.screenX * scale + grid_width - 1
        High = self.screenY * scale + grid_width - 1

        image = Image.new("RGB", (Width, High), color=LampColor.offcolor)
        draw = ImageDraw.Draw(image)

        for x, y in self.activated_list:
            x *= scale
            y *= scale
            draw.rectangle(
                (x, y, x + scale, y + scale),
                LampColor.oncolor,
            )

        for x in range(self.screenX + 1):
            x *= scale
            draw.line(
                [(x, 0), (x, High)],
                fill=LampColor.gridcolor,
                width=grid_width,
            )

        for y in range(self.screenY + 1):
            y *= scale
            draw.line(
                [(0, y), (Width, y)],
                fill=LampColor.gridcolor,
                width=grid_width,
            )

        return image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

    def display(self):
        image = self.build()
        image.show()


def main():
    # Initialize screen with size 64 x 64
    my_screen = LampScreen(10, 10, 30, 4)

    # Draw pixels
    my_screen.draw_pixel((20, 20))
    my_screen.draw_pixel((2, 2))

    # Display
    my_screen.display()


if __name__ == "__main__":
    main()
