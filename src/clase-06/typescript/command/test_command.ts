import { Light, RemoteControl, LightOnCommand, LightOffCommand } from './command';

const light = new Light();
const rc = new RemoteControl();
rc.run(new LightOnCommand(light));
rc.run(new LightOffCommand(light));

if (rc.getHistory().length !== 2) throw new Error('Historial incorrecto');
if (light.state !== 'off') throw new Error('Estado final incorrecto');
console.log('test_command OK');
