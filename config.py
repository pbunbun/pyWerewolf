#!/usr/bin/env python

# IRC config
class irc:
    server      = "irc.redbrick.dcu.ie"
    port        = 6667
    channel     = "#werewolf-test"
    nickname    = ("pyWerewolf", "pyWerewolf_")
    password    = "werewolf"
    admins      = ["bunbun"]

# Game config
class game:
    signup          = 90  # signup time
    cycle           = {}
    cycle['day']    = 120 # length of day cycle
    cycle['night']  = 60  # length of night cycle
    min_players     = 6   # minimum amount of players for game
    max_players     = 42  # maximum amount of players for game