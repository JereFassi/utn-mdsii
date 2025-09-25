import { SystemFacade } from "../facade";

test("Facade orquesta start y shutdown", () => {
  const f = new SystemFacade();
  const start = f.startApp("alice");
  expect(start.startsWith("Logger: activo")).toBe(true);
  expect(start.includes("DB: conexión establecida")).toBe(true);
  expect(start.endsWith("Logger: Sistema inicializado")).toBe(true);
  const stop = f.shutdown();
  expect(stop).toBe("Logger: detenido | Auth: apagado | DB: conexión cerrada");
});
