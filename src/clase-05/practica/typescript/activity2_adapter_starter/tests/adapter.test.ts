import { Adapter, OldSystem } from "../adapter";

test("Adapter normaliza salida (termina en (normalizado) y simula JSON)", () => {
  const ad = new Adapter(new OldSystem());
  const out = ad.request();
  expect(out.endsWith("(normalizado)")).toBe(true);
  expect(out.includes("{'msg':'Respuesta del sistema antiguo'}")).toBe(true);
});
