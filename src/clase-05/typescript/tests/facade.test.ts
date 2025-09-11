import { SystemFacade } from "../facade";

test("Facade orquesta el flujo y encapsula la complejidad", () => {
  const f = new SystemFacade();
  const out = f.runWorkflow("SELECT 1");
  expect(out.startsWith("A: conexión establecida")).toBe(true);
  expect(out.endsWith("A: conexión cerrada")).toBe(true);
});
