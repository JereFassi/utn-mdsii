import express from 'express';

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (_req, res) => {
  res.json({ ok: true, msg: 'Hola desde Clase 3 (JS) - Express' });
});

app.listen(port, () => {
  console.log(`[JS] Servidor escuchando en http://localhost:${port}`);
});