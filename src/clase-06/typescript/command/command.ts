export interface Command { execute(): void; }

export class Light {
  public state: 'on'|'off' = 'off';
  on(){ this.state = 'on'; console.log('Luz encendida'); }
  off(){ this.state = 'off'; console.log('Luz apagada'); }
}

export class LightOnCommand implements Command {
  constructor(private light: Light) {}
  execute(){ this.light.on(); }
}
export class LightOffCommand implements Command {
  constructor(private light: Light) {}
  execute(){ this.light.off(); }
}

export class RemoteControl {
  private history: Command[] = [];
  run(c: Command){ c.execute(); this.history.push(c); }
  getHistory(){ return this.history.slice(); }
}

// Demo
if (require.main === module) {
  const light = new Light();
  const remote = new RemoteControl();
  remote.run(new LightOnCommand(light));
  remote.run(new LightOffCommand(light));
}
