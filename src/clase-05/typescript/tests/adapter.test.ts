import { Adapter, OldSystem } from "../adapter";

test("Adapter traduce interfaz y normaliza salida", () => {
  const ad = new Adapter(new OldSystem());
  expect(ad.request().endsWith("(normalizado)")).toBe(true);
});
