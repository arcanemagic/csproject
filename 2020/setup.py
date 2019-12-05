import cx_Freeze

executables = [cx_Freeze.Executable("Menu.py")]

cx_Freeze.setup(
    name="Project Gamezone",
    options={"build_exe": {"packages":["pygame", "pygameMenu"],
                           "include_files":["fonts/AD.ttf", "fonts/Norwester.otf", "images/game.png", "images/gamezone.png", "images/intro.png", "images/lose.png", "images/snake.png", "images/stackie.png", "images/win.png", "music/shake.ogg"]}},
    executables = executables

    )
