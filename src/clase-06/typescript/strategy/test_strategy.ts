import { Navigator, CarRoute, WalkRoute, PublicTransportRoute } from './strategy';

const nav = new Navigator(new CarRoute());
const r1 = nav.buildRoute('A','B');
if (!r1.includes('auto')) throw new Error('CarRoute falló');

nav.setStrategy(new WalkRoute());
const r2 = nav.buildRoute('A','B');
if (!r2.includes('pie')) throw new Error('WalkRoute falló');

nav.setStrategy(new PublicTransportRoute());
const r3 = nav.buildRoute('A','B');
if (!r3.includes('transporte público')) throw new Error('PublicTransportRoute falló');

console.log('test_strategy OK');
