dict_res = {
            "/": "./static/index.html",
            "/index": "./static/index.html",
            "/amusement":"./static/amusement.html",
            "/learn":"./static/learn.html",
            "/setupwebsite":"./static/setupwebsite.html",
            "/shop":"./static/shop.html",
            "/use":"./static/use.html"
        }

print(dict_res.get("/"))
print(type(dict_res.get("/")))