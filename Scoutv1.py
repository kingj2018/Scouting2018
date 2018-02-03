from appJar import gui

app = gui("Scouting", "700x400")
teams = []

def setupGUI():
    """Creates the GUI we use"""
    app.setPadding(8,5)
    app.setFont(11)

    # Entry of team number and match
    app.addLabel("teamNum", "Team#:", 0, 0)
    app.addEntry("team", 0, 1)
    app.addLabel("matchNum", "Match:", 0, 2)
    app.addEntry("match", 0, 3)

    #Column 1-4 auto


    #Column 5-whatever teleop
    app.addLabel

    # Width adjustments
    app.setEntryWidth("team", 30)
    app.setEntryWidth("match", 10)

    app.go()

setupGUI()