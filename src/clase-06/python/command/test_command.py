from python.command.command import Light, RemoteControl, LightOnCommand, LightOffCommand

def test_command_history_and_effect(capsys):
    light = Light()
    rc = RemoteControl()

    rc.run(LightOnCommand(light))
    rc.run(LightOffCommand(light))

    assert len(rc.history) == 2
    assert light.state == "off"

    out = capsys.readouterr().out
    assert "Luz encendida" in out
    assert "Luz apagada" in out
