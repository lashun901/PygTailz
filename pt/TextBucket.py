from pygame import Surface, Rect, Color, font, KEYDOWN
from pygame.constants import *
from pygame.font import Font
from pt.UserInput import UserInputManager, printable

available_inputs = list(printable)

class TextBox:
    def __init__(tb, text: str, font: Font, location: tuple | Rect, text_color: Color = Color(0, 0, 0)) -> None:
        tb.text = text
        tb.font = font
        tb.location = location
        tb.surface = tb.font.render(tb.text, True, text_color)
        tb.active = True
        tb.show = True
    
    def set_location(tb, location: tuple | Rect) -> tuple | Rect:
        if isinstance(location, (tuple, Rect)):
            tb.location = location
        else: print("Invalid location given.")
    
    def get_surface_width(tb) -> int:
        return tb.surface.get_width()

    def get_surface_height(tb) -> int:
        return tb.surface.get_height()

    def partial_event_loop(tb, event):
        pass

class InputBox:
    def __init__(ib, rect_location: Rect, font_obj: Font, text: str = "") -> None:
        ib.active = False
        ib.location = rect_location
        ib.font = font_obj
        ib.text = text
        ib.canvas_text = text
        ib.surface = ib.font.render(ib.text, True, Color(255, 255, 255))
        ib.show = True
        ib.active = True
        ib.User_Input_Manager = UserInputManager(ib.canvas_text)
    
    def render(ib):
        ib.surface = ib.font.render(ib.text, True, Color(255, 255, 255))

    def partial_event_loop(ib, event):
        ib.User_Input_Manager.check_event(event)
        ib.canvas_text = ib.User_Input_Manager.get_canvas_text()

class TextBucket:
    def __init__(tb, canvas: Surface) -> None:
        tb.canvas = canvas
        tb.fonts = {"Consolas": font.SysFont("Consolas", 18)}
        tb.text_boxes = {}
        tb.input_boxes = {}

    def _create_text_box(tb, text: str, location: tuple):
        return TextBox(text, tb.fonts["Consolas"], location)

    def _create_input_box(tb, rect_location: Rect, font_obj: Font, text: str = ""):
        return InputBox(rect_location, font_obj, text)
    
    def add_font(tb, font_name: str, point_size: int):
        tb.fonts[font_name] = font.SysFont(font_name, point_size)

    def add(tb, id: str, text: str, location: tuple):
        try:
            tb.text_boxes[id] = tb._create_text_box(text, location)
        except Exception as E:
            print(E)
    
    def add_input_box(tb, id: str, rect_location: Rect, font_obj: Font = None, text: str = ""):
        try:
            if font_obj: tb.input_boxes[id] = tb._create_input_box(rect_location, font_obj, text)
            else: tb.input_boxes[id] = tb._create_input_box(rect_location, tb.fonts["Consolas"], text)
        except Exception as E:
            print(E)
    
    def dump(tb, id: str):
        try:
            del tb.text_boxes[id]
        except:
            print("Something went wrong. Could Not Delete Text Box.")
    
    def alter_location(tb, id: str, location: tuple | Rect):
        try:
            tb.text_boxes[id].set_location(location)
        except:
            print("Something went wrong. Could Not Alter Text Box Location.")

    def update(tb):
        for index, key in enumerate(tb.text_boxes):
            text_box = tb.text_boxes[key]
            if text_box.show:
                tb.canvas.blit(text_box.surface, text_box.location)
        
        for index, key in enumerate(tb.input_boxes):
            input_box = tb.input_boxes[key]
            if input_box.show:
                tb.canvas.blit(input_box.surface, input_box.location)
    
    def partial_event_loop(tb, event):
        for index, key in enumerate(tb.input_boxes):
            input_box: InputBox = tb.input_boxes[key]
            if input_box.active:
                input_box.partial_event_loop(event)
                if input_box.canvas_text != input_box.text:
                    input_box.text = input_box.canvas_text
                    input_box.render()
                    print("re-rendering...")