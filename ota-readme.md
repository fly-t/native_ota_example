# ota升级

menuconfig 配置wifi 和密码

# 配置软件版本

如果有version.txt修改软件版本, 默认项目会检测版本号

# 根据需求启动http或者https服务器

默认是使用https, 如果使用http记得修改url

``` c
esp_http_client_config_t config = {
        .url = "http://192.168.33.181:8070/blink.bin",
        .cert_pem = (char *)server_cert_pem_start,
        .timeout_ms = CONFIG_EXAMPLE_OTA_RECV_TIMEOUT,
        .keep_alive_enable = true,
    };
```

启动http: server命令

``` cmd
python -m http.server 8070
```

启动https:server脚本

生成证书文件

``` c
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout key.pem -out cert.pem
```


``` python
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
```


设置软件版本

添加version.txt

``` cmake
# 读取 version.txt 中的版本信息
file(READ ${CMAKE_SOURCE_DIR}/version.txt VERSION)
string(STRIP ${VERSION} VERSION)  # 去除文件中的换行符
```