// Servidor local para testar no seu computador:  npm run dev  →  http://localhost:3000
// (Na Vercel este arquivo não é usado: ela serve o index.html e a pasta api/ sozinha.)
import http from "node:http";
import { readFile } from "node:fs/promises";
import handler from "./api/rpc.js";

const PORT = process.env.PORT || 3000;
http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://localhost");
  if (url.pathname === "/api/rpc") return handler(req, res);
  if (url.pathname === "/" || url.pathname === "/index.html") {
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    return res.end(await readFile(new URL("./index.html", import.meta.url)));
  }
  res.statusCode = 404;
  res.end("Não encontrado");
}).listen(PORT, () => console.log(`VTAL Unidades rodando em http://localhost:${PORT}`));
