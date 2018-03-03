from appJar import gui

app = gui("Scouting", "600x400")
teams = []


def setupGUI():
    """Creates the GUI we use"""
    app.setPadding(2, 3)
    app.setFont(11)

    # Entry of team number and match
    app.addLabelEntry("Team", 0, 0)
    app.addLabelEntry("Match", 1, 0)
    app.addLabel("alliLabel", "Alliance", 0, 1)
    app.addRadioButton("alliButton", "Red", 0, 2)
    app.addRadioButton("alliButton", "Blue", 1, 2)

    # Width adjustments
    # app.setLabelWidth("teamNum", 5)
    app.setEntryWidth("Team", 10)
    # app.setLabelWidth("matchNum", 8)
    app.setEntryWidth("Match", 8)

    # Auto
    app.startLabelFrame("Autonomous", 4, 0, 3, 1)

    # Stuff we need
    app.addLabel("startPosLabel", "Starting Position:", 0, 0)
    app.addOptionBox("startPosOptionBox", ["Left", "Centre", "Right"], 0, 1)
    app.addCheckBox("AutoLine", 1, 0)
    app.addLabel("autoSwitch", "Switch:", 2, 0)
    app.addRadioButton("autoSwitchRadio", "Success", 3, 0)
    app.addRadioButton("autoSwitchRadio", "Attempt", 4, 0)
    app.addRadioButton("autoSwitchRadio", "No attempt", 5, 0)
    app.addLabel("autoScale", "Scale:", 2, 1)
    app.addRadioButton("autoScaleRadio", "Success", 3, 1)
    app.addRadioButton("autoScaleRadio", "Attempt", 4, 1)
    app.addRadioButton("autoScaleRadio", "No attempt", 5, 1)

    app.stopLabelFrame()

    # Team stuff
    app.startLabelFrame("Team Achievements", 5, 0, 3, 1)

    # Powerups
    app.addLabel("powerups", "Powerups Used:", 0, 0, 2, 1)
    app.addCheckBox("Boost", 1, 0)
    app.addSpinBoxRange("boostLvL", 0, 3, 1, 1)
    app.addCheckBox("Force", 2, 0)
    app.addSpinBoxRange("forceLvL", 0, 3, 2, 1)
    app.addCheckBox("Levitate", 3, 0)
    app.addSpinBoxRange("levitateLvL", 0, 3, 3, 1)
    # RPs
    app.addLabel("RPs", "Ranking Points:", 0, 2, 2, 1)
    app.addCheckBox("Auto RP", 1, 2, 2, 1)
    app.addCheckBox("Climbing RP", 2, 2, 2, 1)
    # Result
    app.addRadioButton("result", "Win", 3, 2)
    app.addRadioButton("result", "Loss", 3, 3)
    # Widths
    app.setSpinBoxWidth("boostLvL", 5)
    app.setSpinBoxWidth("forceLvL", 5)
    app.setSpinBoxWidth("levitateLvL", 5)

    app.stopLabelFrame()

    # teleop
    app.startLabelFrame("Teleop", 0, 3, 2, 6)

    # How the team interracts with the switch
    app.addLabel("switchStat", "Switch Stats:", 1, 0)
    app.addLabel("onSwitchLabel", "  - On Switch", 2, 0)
    app.addSpinBoxRange("onSwitchSpinBox", 0, 60, 2, 1)
    app.addLabel("attSwitchLabel", "  - Attempts", 3, 0)
    app.addSpinBoxRange("attSwitchSpinBox", 0,100, 3, 1)
    # How the team interracts with the scale
    app.addLabel("scaleStat", "Scale Stats:", 4, 0)
    app.addLabel("onScaleLabel", "  - On Scale", 5, 0)
    app.addSpinBoxRange("onScaleSpinBox", 0, 60, 5, 1)
    app.addLabel("attScaleLabel", "  - Attempts", 6, 0)
    app.addSpinBoxRange("attScaleSpinBox", 0,100, 6, 1)
    # How the team interracts with the Vault
    app.addLabel("vaultStat", "Vault Stats:", 7, 0)
    app.addLabel("inVaultLabel", "  - Cubes in Vault", 8, 0)
    app.addSpinBoxRange("inVaultSpinBox", 0, 9, 8, 1)
    # Did they climb
    app.addLabel("climbStat", "Climbing Stats:", 9, 0)
    app.addCheckBox("Can Climb", 10, 0)
    app.addCheckBox("Assisted", 10, 1)
    app.addLabel("didClimb", "  - Success", 11, 0)
    app.addRadioButton("climbed", "Yes", 12, 0)
    app.addRadioButton("climbed", "No", 13, 0)
    app.addLabel("climbAssistLabel", "Assists:", 11, 1)
    app.addSpinBoxRange("climbAssistSpinBox", 0, 2, 12, 1)

    # Widths
    app.setSpinBoxWidth("onSwitchSpinBox", 5)
    app.setSpinBoxWidth("attSwitchSpinBox", 5)
    app.setSpinBoxWidth("onScaleSpinBox", 5)
    app.setSpinBoxWidth("attScaleSpinBox", 5)
    app.setSpinBoxWidth("inVaultSpinBox", 5)
    app.setSpinBoxWidth("climbAssistSpinBox", 5)

    app.stopLabelFrame()

    app.addButton("View Rankings", rankings, 6, 3)
    app.addButton("Save Match", saveFile, 6, 4)

    app.go()

#functions :)
#TODO make a save file funtion
def saveFile(button):
    fileName = app.getEntry("Team") + "-" + app.getEntry("Match") + ".txt"
    print(fileName)
    #with (fileName, "w") as f:


def rankings(button):
#TODO make the extra subwindow(in setupGUI()) filter through to show all things with their rankings
# you should be able to click a team and view the team in depth with each match
# also search up a match and it shows everything
    pass


setupGUI()