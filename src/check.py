import os

checks = ["PROXY_HOST",
"API_USER",
"API_PASSWORD",
"LOGIN_PATH",
"API_PATH",
]

for c in checks:
    e = os.environ.get(c, '')
    if e == '':
        print(f"{c} is not set")


