const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use('/', createProxyMiddleware({
  target: 'https://true.mmpctech.xyz', // ✅ DO VPS IP
  changeOrigin: true,
  ws: true,
  secure: false,  // for self-signed or V2Ray TLS cert
  xfwd: true,
}));

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Proxy running on port ${PORT}`);
});
