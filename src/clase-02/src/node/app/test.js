import { saludar } from "./service.js";

const esperado = "Hola, Clase 2!";
const recibido = saludar("Clase 2");
if (recibido !== esperado) {
  console.error("❌ Test falló:", { esperado, recibido });
  process.exit(1);
}
console.log("✅ Test pasó");