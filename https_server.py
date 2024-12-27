import http.server
import ssl

# 选择你想要的端口，假设是 8070
server_address = ('', 8070)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# 创建 SSL 上下文对象
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# 使用 SSL 上下文来包装 httpd 的套接字
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:8070")
httpd.serve_forever()
