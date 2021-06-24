tag: user.mouse_grid_enabled
-
M grid:
    user.grid_select_screen(1)
    user.grid_activate()

[M] grid win:
    user.grid_place_window()
    user.grid_activate()

[M] grid <user.number_key>+:
    user.grid_activate()
    user.grid_narrow_list(number_key_list)

[M] grid screen [<number>]:
    user.grid_select_screen(number or 1)
    user.grid_activate()
