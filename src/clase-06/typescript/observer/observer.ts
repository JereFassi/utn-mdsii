interface Subscriber {
  update(data: any): void;
}

class Publisher {
  private subscribers: Subscriber[] = [];
  subscribe(s: Subscriber) { this.subscribers.push(s); }
  unsubscribe(s: Subscriber) { this.subscribers = this.subscribers.filter(x => x !== s); }
  protected notify(data: any) { this.subscribers.forEach(s => s.update(data)); }
}

export class Stock extends Publisher {
  private price = 0;
  setPrice(p: number){ this.price = p; this.notify(this.price); }
}

export class EmailAlert implements Subscriber {
  update(data: any): void { console.log(`[Email] Nuevo precio: ${data}`); }
}

export class Dashboard implements Subscriber {
  update(data: any): void { console.log(`[Dashboard] Precio actualizado: ${data}`); }
}

// Demo
if (require.main === module) {
  const s = new Stock();
  const e = new EmailAlert();
  const d = new Dashboard();
  s.subscribe(e); s.subscribe(d);
  s.setPrice(123.45);
}
