from pygame import constants
from string import printable
from time import time

class Blueprint:
    def __init__(self) -> None:
        pass

class Key:
    def __init__(ky, action, alt_action) -> None:
        ky.action = action
        ky.alt_action = alt_action

        ky.being_pressed = False

        ky.button_down_time = 0.0
        ky.button_up_time = 0.0
        ky.pressed_time = 0.0
        ky.elapsed_time = 0.0
    
    def button_down(ky):
        ky.button_down_time = time()
        ky.button_up_time = None
        ky.being_pressed = True

    def button_up(ky):
        ky.button_up_time = time()
        ky.pressed_time = ky.button_up_time - ky.button_down_time
        ky.elapsed_time = 0.0
        ky.being_pressed = False
    
    def update_elapsed_time(ky):
        try:
            ky.elapsed_time = round(time() - ky.button_down_time, 3)
        except Exception as E:
            print(E)
    
    def get_elapsed_time(ky):
        return ky.elapsed_time

    def get_acton(ky):
        return ky.action
    
    def get_alt_action(ky):
        return ky.alt_action
    
    def set_action(ky):
        return ky.action
    
    def set_alt_action(ky):
        return ky.alt_action

class VirtualKeyboard:
    def __init__(vk, blueprint: Blueprint = None) -> None:
        # Action Keys
        vk.escape = Key(0, 0)
        vk.backspace = Key(98, 0)
        vk.tab = Key("    ", 0)
        vk.left_shift = Key(0, 0)
        vk.right_shift = Key(0, 0)
        vk.arrow_down = Key(0, 0)
        vk.arrow_up = Key(0, 0)
        vk.arrow_left = Key(0, 0)
        vk.arrow_right = Key(0, 0)
        vk.enter = Key(0, 0)
        vk.left_ctrl = Key(0, 0)
        vk.right_ctrl = Key(0, 0)
        vk.left_ctrl = Key(0, 0)
        vk.right_alt = Key(0, 0)
        vk.spacebar = Key(" ", 0)

        # Number Keys 
        vk.one = Key("1", 0)
        vk.two = Key("2", 0)
        vk.three = Key("3", 0)
        vk.four = Key("4", 0)
        vk.five = Key("5", 0)
        vk.six = Key("6", 0)
        vk.seven = Key("7", 0)
        vk.eight = Key("8", 0)
        vk.nine = Key("9", 0)
        vk.zero = Key("0", 0)

        # Other Characters
        vk.backquote = Key("`", "~")
        vk.hyphen = Key("-", "_")
        vk.equal = Key("=", "+")
        vk.open_bracket = Key("[", "{")
        vk.closed_bracket = Key("]", "}")
        vk.backslash = Key("\\", "|")
        vk.semi_colon = Key(";", ":")
        vk.apostrophe = Key("'", "\"")
        vk.comma = Key(",", "<")
        vk.period = Key(".", ">")
        vk.slash = Key("/", "?")

        # Characters
        vk.q = Key("q", "Q")
        vk.w = Key("w", "W")
        vk.e = Key("e", "E")
        vk.r = Key("r", "R")
        vk.t = Key("t", "T")
        vk.y = Key("y", "Y")
        vk.u = Key("u", "U")
        vk.i = Key("i", "I")
        vk.o = Key("o", "O")
        vk.p = Key("p", "P")
        vk.a = Key("a", "A")
        vk.s = Key("s", "S")
        vk.d = Key("d", "D")
        vk.f = Key("f", "F")
        vk.g = Key("g", "G")
        vk.h = Key("h", "H")
        vk.j = Key("j", "J")
        vk.k = Key("k", "K")
        vk.l = Key("l", "L")
        vk.z = Key("z", "Z")
        vk.x = Key("x", "X")
        vk.c = Key("c", "C")
        vk.v = Key("v", "V")
        vk.b = Key("b", "B")
        vk.n = Key("n", "N")
        vk.m = Key("m", "M")

class UserInputManager:
    def __init__(uim, canvas_text: str) -> None:
        uim.canvas_text: str = canvas_text
        uim.VK = VirtualKeyboard()
        uim.cargo = None

    # Need to finish all possible cases for keydown checker.
    def keydown_checker(uim, key):
        match key:
            case constants.K_BACKSPACE:
                uim.VK.backspace.button_down()
                return uim.VK.backspace.get_acton()
            case constants.K_TAB:
                uim.VK.tab.button_down()
                return uim.VK.tab.get_acton()
            case constants.K_BACKSLASH:
                uim.VK.backslash.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.backslash.get_alt_action()
                else: return uim.VK.backslash.get_acton()
            case constants.K_RIGHTBRACKET:
                uim.VK.closed_bracket.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.closed_bracket.get_alt_action()
                else: return uim.VK.closed_bracket.get_acton()
            case constants.K_LEFTBRACKET:
                uim.VK.open_bracket.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.open_bracket.get_alt_action()
                else: return uim.VK.open_bracket.get_acton()
            case constants.K_SEMICOLON:
                uim.VK.semi_colon.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.semi_colon.get_alt_action()
                else: return uim.VK.semi_colon.get_acton()
            case constants.K_COMMA:
                uim.VK.comma.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.comma.get_alt_action()
                else: return uim.VK.comma.get_acton()
            case constants.K_PERIOD:
                uim.VK.period.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.period.get_alt_action()
                else: return uim.VK.period.get_acton()
            case constants.K_QUOTE:
                uim.VK.apostrophe.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.apostrophe.get_alt_action()
                else: return uim.VK.apostrophe.get_acton()
            case constants.K_SLASH:
                uim.VK.slash.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.slash.get_alt_action()
                else: return uim.VK.slash.get_acton()
            case constants.K_SPACE:
                uim.VK.spacebar.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.spacebar.get_alt_action()
                else: return uim.VK.spacebar.get_acton()
            case constants.K_0:
                uim.VK.zero.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.zero.get_alt_action()
                else: return uim.VK.zero.get_acton()
            case constants.K_1:
                uim.VK.one.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.one.get_alt_action()
                else: return uim.VK.one.get_acton()
            case constants.K_2:
                uim.VK.two.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.two.get_alt_action()
                else: return uim.VK.two.get_acton()
            case constants.K_3:
                uim.VK.three.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.three.get_alt_action()
                else: return uim.VK.three.get_acton()
            case constants.K_4:
                uim.VK.four.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.four.get_alt_action()
                else: return uim.VK.four.get_acton()
            case constants.K_5:
                uim.VK.five.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.five.get_alt_action()
                else: return uim.VK.five.get_acton()
            case constants.K_6:
                uim.VK.six.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.six.get_alt_action()
                else: return uim.VK.six.get_acton()
            case constants.K_7:
                uim.VK.seven.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.seven.get_alt_action()
                else: return uim.VK.seven.get_acton()
            case constants.K_8:
                uim.VK.eight.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.eight.get_alt_action()
                else: return uim.VK.eight.get_acton()
            case constants.K_9:
                uim.VK.nine.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.nine.get_alt_action()
                else: return uim.VK.nine.get_acton()
            case constants.K_MINUS:
                uim.VK.hyphen.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.hyphen.get_alt_action()
                else: return uim.VK.hyphen.get_acton()
            case constants.K_EQUALS:
                uim.VK.equal.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.equal.get_alt_action()
                else: return uim.VK.equal.get_acton()
            case constants.K_BACKQUOTE:
                uim.VK.backquote.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.backquote.get_alt_action()
                else: return uim.VK.backquote.get_acton()
            case constants.K_q:
                uim.VK.q.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.q.get_alt_action()
                else: return uim.VK.q.get_acton()
            case constants.K_w:
                uim.VK.w.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.w.get_alt_action()
                else: return uim.VK.w.get_acton()
            case constants.K_e:
                uim.VK.e.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.e.get_alt_action()
                else: return uim.VK.e.get_acton()
            case constants.K_r:
                uim.VK.r.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.r.get_alt_action()
                else: return uim.VK.r.get_acton()
            case constants.K_t:
                uim.VK.t.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.t.get_alt_action()
                else: return uim.VK.t.get_acton()
            case constants.K_u:
                uim.VK.u.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.u.get_alt_action()
                else: return uim.VK.u.get_acton()
            case constants.K_i:
                uim.VK.i.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.i.get_alt_action()
                else: return uim.VK.i.get_acton()
            case constants.K_o:
                uim.VK.o.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.o.get_alt_action()
                else: return uim.VK.o.get_acton()
            case constants.K_p:
                uim.VK.p.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.p.get_alt_action()
                else: return uim.VK.p.get_acton()
            case constants.K_a:
                uim.VK.a.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.a.get_alt_action()
                else: return uim.VK.a.get_acton()
            case constants.K_s:
                uim.VK.s.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.s.get_alt_action()
                else: return uim.VK.s.get_acton()
            case constants.K_d:
                uim.VK.d.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.d.get_alt_action()
                else: return uim.VK.d.get_acton()
            case constants.K_f:
                uim.VK.f.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.f.get_alt_action()
                else: return uim.VK.f.get_acton()
            case constants.K_g:
                uim.VK.g.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.g.get_alt_action()
                else: return uim.VK.g.get_acton()
            case constants.K_h:
                uim.VK.h.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.h.get_alt_action()
                else: return uim.VK.h.get_acton()
            case constants.K_j:
                uim.VK.j.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.j.get_alt_action()
                else: return uim.VK.j.get_acton()
            case constants.K_k:
                uim.VK.k.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.k.get_alt_action()
                else: return uim.VK.k.get_acton()
            case constants.K_l:
                uim.VK.l.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.l.get_alt_action()
                else: return uim.VK.l.get_acton()
            case constants.K_z:
                uim.VK.z.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.z.get_alt_action()
                else: return uim.VK.z.get_acton()
            case constants.K_x:
                uim.VK.x.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.x.get_alt_action()
                else: return uim.VK.x.get_acton()
            case constants.K_c:
                uim.VK.c.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.c.get_alt_action()
                else: return uim.VK.c.get_acton()
            case constants.K_v:
                uim.VK.v.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.v.get_alt_action()
                else: return uim.VK.v.get_acton()
            case constants.K_b:
                uim.VK.b.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.b.get_alt_action()
                else: return uim.VK.b.get_acton()
            case constants.K_n:
                uim.VK.n.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.n.get_alt_action()
                else: return uim.VK.n.get_acton()
            case constants.K_m:
                uim.VK.m.button_down()
                if uim.VK.left_shift.being_pressed: return uim.VK.m.get_alt_action()
                else: return uim.VK.m.get_acton()
            case _:
                return None

    # Need to finish all possible cases for keyup checker.
    def keyup_checker(uim, key):
        match key:
            case constants.K_0:
                uim.VK.zero.button_up()
                if uim.VK.left_shift.being_pressed: return uim.VK.zero.get_alt_action()
                else: return uim.VK.zero.get_acton()
            case constants.K_1:
                uim.VK.one.button_up()
                if uim.VK.left_shift.being_pressed: return uim.VK.one.get_alt_action()
                else: return uim.VK.one.get_acton()
            case _:
                return None
    
    def key_action_checker(uim, action):
        if isinstance(action, str):
            uim.canvas_text += action
            print(f"New Canvas Text: \n{uim.canvas_text}")
        else:
            match action:
                case 98:
                    uim.canvas_text = uim.canvas_text[:-1]
            
    
    def check_event(uim, event):
        if event.type == constants.KEYDOWN:
            print("A key was pressed.")
            uim.key_action_checker(uim.keydown_checker(event.key))
        elif event.type == constants.KEYUP:
            pass
    
    def get_canvas_text(uim):
        return uim.canvas_text