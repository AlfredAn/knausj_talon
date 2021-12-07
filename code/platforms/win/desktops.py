from talon import Context, Module, actions
ctx = Context()
ctx.matches = r"""
os: windows
"""

@ctx.action_class("user")
class Actions:
    def desktop(number: int):
        actions.key(f"f{number+12}")

    def desktop_show():
        actions.key("super-tab")

    def desktop_next():
        actions.key("f22")

    def desktop_last():
        actions.key("f23")

    def desktop_last_used():
        actions.key("f24")

    def desktop_new():
        actions.key("super-ctrl-d")

    def desktop_remove():
        actions.key("super-ctrl-f4")

    def window_move_desktop_left():
        actions.key("shift-f23")

    def window_move_desktop_right():
        actions.key("shift-f22")

    def window_move_desktop(desktop_number: int):
        actions.key(f"shift-f{desktop_number+12}")
