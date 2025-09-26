import { Stock, EmailAlert, Dashboard } from './observer';

function captureConsole(fn: () => void): string[] {
  const logs: string[] = [];
  const orig = console.log;
  console.log = (...args: any[]) => { logs.push(args.join(' ')); };
  try { fn(); } finally { console.log = orig; }
  return logs;
}

const logs = captureConsole(() => {
  const s = new Stock();
  const e = new EmailAlert();
  const d = new Dashboard();
  s.subscribe(e); s.subscribe(d);
  s.setPrice(10.5);
});

if (!logs.some(x => x.includes('Nuevo precio: 10.5'))) throw new Error('EmailAlert no recibió notificación');
if (!logs.some(x => x.includes('Precio actualizado: 10.5'))) throw new Error('Dashboard no recibió notificación');

console.log('test_observer OK');
