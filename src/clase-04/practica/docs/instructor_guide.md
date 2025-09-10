## Sugerencias de evaluación
- Revisar que **Singleton** garantice una sola instancia (constructor privado/`__new__`, propiedad estática).
- En **Factory**, validar una interfaz/base y al menos 3 productos concretos.
- En **Builder**, verificar method chaining y objetos válidos con configuraciones parciales.

## Extensiones (si hay tiempo)
- Singleton 'copy-on-write' inmutable para Config.
- Factory con registro dinámico (mapa de constructores).
- Builder con validaciones en `build()` (campos obligatorios).
