import cx_Freeze

executables = [cx_Freeze.Executable("sprite_game.py")]

cx_Freeze.setup(
    name="Sprite Game",
    options={"build.exe": {"packages": ["pygame"], "included_files": []}},
    executables=executables

)
