from sys import exit as super_quit
from pt.StateManager import StateManager, Surface, Color, State, KEYDOWN, K_SPACE
from random import randint as ri


dim = (1920, 1080)

### Test Area ###
state_manager = StateManager(dim=dim)

class MainMenu(State):
    def __init__(state, STATE) -> None:
        super().__init__(STATE)
        state.dim = STATE.dim
        state.GLOBALS = {"Menu Bar Shape": (state.dim[0],int(round(state.dim[1]*(11/540)))),
                         "File Explorer Shape":(state.dim[0]//11, state.dim[1] - state.dim[1]*(11/540)),
                         "Zen Space Shape": (state.dim[0]//10, state.dim[1] - state.dim[1]*(11/540)),
                         "Zen Space Left Location": (state.dim[0]//11, state.dim[1]*(11/540)),
                         "Zen Space Right Location": (state.dim[0]//11 * 7.8, state.dim[1]*(11/540)),
                         "Nav Bar Shape": (round(state.dim[0] - (state.dim[0]//11 * 7.8 + state.dim[0]//10)), state.dim[1] - state.dim[1]*(11/540)),
                         "Nav Bar Location": (state.dim[0], state.dim[1]*(11/540)),
                         "Workspace Shape": (state.dim[0] - (round(state.dim[0]//11 + state.dim[0]//10 * 2 + state.dim[0] - (state.dim[0]//11 * 7.8 + state.dim[0]//10))), state.dim[1] - state.dim[1]*(11/540)),
                         "Workspace Location": (state.dim[0]//11 + state.dim[0]//10, state.dim[1]*(11/540)),
                         "Workspace Color": Color(55, 55, 55),
                         "Menu Bar Color": Color(70, 70, 70),
                         "File Explorer Color": Color(35, 35, 35),
                         "Zen Space Color": Color(70, 70, 70),
                         "Nav Bar Color": Color(55, 55, 55),
                         "Menu Bar Button Spacing Y": state.dim[1] * (1/540),
                         "Menu Bar Button Spacing X": state.dim[0] * (3/240)}

        """Menu Bar"""
        state.Blit_Bucket.add("Menu Bar",
                              Surface(state.GLOBALS["Menu Bar Shape"]),
                              Surface(state.GLOBALS["Menu Bar Shape"]).get_rect(topleft = (0, 0)),
                              state.GLOBALS["Menu Bar Color"])
        
        # Menu Bar Buttons
        state.Blit_Bucket.Text_Bucket.add("File Button Str", "File", (state.GLOBALS["Menu Bar Button Spacing X"],state.GLOBALS["Menu Bar Button Spacing Y"]))
        state.Blit_Bucket.Text_Bucket.add("Edit Button Str", "Edit", (2 * state.GLOBALS["Menu Bar Button Spacing X"] + 
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["File Button Str"].get_surface_width(),
                                                                      state.GLOBALS["Menu Bar Button Spacing Y"]))
        state.Blit_Bucket.Text_Bucket.add("Run Button Str", "Run", (3 * state.GLOBALS["Menu Bar Button Spacing X"] + 
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["File Button Str"].get_surface_width() +
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["Edit Button Str"].get_surface_width(),
                                                                      state.GLOBALS["Menu Bar Button Spacing Y"]))
        state.Blit_Bucket.Text_Bucket.add("Terminal Button Str", "Terminal", (4 * state.GLOBALS["Menu Bar Button Spacing X"] + 
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["File Button Str"].get_surface_width() +
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["Edit Button Str"].get_surface_width() +
                                                                      state.Blit_Bucket.Text_Bucket.text_boxes["Run Button Str"].get_surface_width(),
                                                                      state.GLOBALS["Menu Bar Button Spacing Y"]))
        
        """File Explorer"""
        state.Blit_Bucket.add("File Explorer",
                              Surface(state.GLOBALS["File Explorer Shape"]),
                              Surface(state.GLOBALS["File Explorer Shape"]).get_rect(topleft = (0, state.dim[1]*(11/540))),
                              state.GLOBALS["File Explorer Color"])
        
        """Zen Space"""
        state.Blit_Bucket.add("Zen Space Left",
                              Surface(state.GLOBALS["Zen Space Shape"]),
                              Surface(state.GLOBALS["Zen Space Shape"]).get_rect(topleft = state.GLOBALS["Zen Space Left Location"]),
                              state.GLOBALS["Zen Space Color"])
        
        state.Blit_Bucket.add("Zen Space Right",
                              Surface(state.GLOBALS["Zen Space Shape"]),
                              Surface(state.GLOBALS["Zen Space Shape"]).get_rect(topleft = state.GLOBALS["Zen Space Right Location"]),
                              state.GLOBALS["Zen Space Color"])
        
        """Nav Bar"""
        state.Blit_Bucket.add("Nav Bar",
                              Surface(state.GLOBALS["Nav Bar Shape"]),
                              Surface(state.GLOBALS["Nav Bar Shape"]).get_rect(topright = state.GLOBALS["Nav Bar Location"]),
                              state.GLOBALS["Nav Bar Color"])
        
        """Workspace"""
        state.Blit_Bucket.add("Workspace",
                              Surface(state.GLOBALS["Workspace Shape"]),
                              Surface(state.GLOBALS["Workspace Shape"]).get_rect(topleft = state.GLOBALS["Workspace Location"]),
                              state.GLOBALS["Workspace Color"])
        state.Blit_Bucket.Text_Bucket.add_input_box("Workspace Input Box", state.Blit_Bucket.get_location("Workspace"), text="Some Default text.!")
    
    def partial_event_loop(state, event):
        super().partial_event_loop(event=event)
        if event.type == KEYDOWN:
            pass

state_manager.Add_State("Base App", MainMenu(STATE=state_manager))
state_manager.Change_State("Base App")
state_manager.Run()

### Test Area End ###
# Modification

quit()
super_quit()