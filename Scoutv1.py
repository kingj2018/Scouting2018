from appJar import gui

app = gui("Scouting", "700x400")
teams = []

def setupGUI():
    """Creates the GUI we use"""
    app.setPadding(5, 4)
    app.setFont(11)

    # Entry of team number and match
    app.addLabel("teamNum", "Team#:", 0, 0)
    app.setLabelAlign("teamNum", "right")
    app.addEntry("team", 0, 1)
    app.addLabel("matchNum", "Match:", 0, 2)
    app.setLabelAlign("matchNum", "right")
    app.addEntry("match", 0, 3)

    #Column 0-3 auto
    app.addCheckBox("AutoLine", 1, 0)


    #Column 4-whatever teleop
    app.addLabel("switch", "Switch Stats:", 1, 4)
    app.addDualMeter("percentSwitch", 2, 5)

    app.addLabel("scale", "Scale Stats:", 3, 4)
    app.addDualMeter("percentScale", 4, 5)

    # Width adjustments
    app.setLabelWidth("teamNum", 5)
    app.setEntryWidth("team", 10)
    app.setLabelWidth("matchNum", 8)
    app.setEntryWidth("match", 8)

    app.go()

setupGUI()