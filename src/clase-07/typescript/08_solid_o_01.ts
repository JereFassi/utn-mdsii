// Antes: condicional para calcular descuentos
function calcularPrecio(tipo: string, monto: number): number {
  if (tipo === "normal") return monto;
  if (tipo === "blackFriday") return monto * 0.8;
  if (tipo === "navidad") return monto * 0.7;
  return monto;
}
