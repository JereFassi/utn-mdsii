export interface RouteStrategy {
  buildRoute(origin: string, destination: string): string;
}

export class CarRoute implements RouteStrategy {
  buildRoute(o: string, d: string) { return `Ruta en auto de ${o} a ${d}`; }
}
export class WalkRoute implements RouteStrategy {
  buildRoute(o: string, d: string) { return `Ruta a pie de ${o} a ${d}`; }
}
export class PublicTransportRoute implements RouteStrategy {
  buildRoute(o: string, d: string) { return `Ruta en transporte público de ${o} a ${d}`; }
}

export class Navigator {
  constructor(private strategy: RouteStrategy) {}
  setStrategy(s: RouteStrategy){ this.strategy = s; }
  buildRoute(o: string, d: string){ return this.strategy.buildRoute(o, d); }
}

// Demo
if (require.main === module) {
  const nav = new Navigator(new CarRoute());
  console.log(nav.buildRoute('Plaza','Aeropuerto'));
  nav.setStrategy(new WalkRoute());
  console.log(nav.buildRoute('Plaza','Aeropuerto'));
}
