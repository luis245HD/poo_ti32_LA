import web


urls = ("/", "Index", "/Bienvenida", "Bienvenida")
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        pass
    def GET(self):
        texto = "Holaaaaaa"
        return render.index()  

class Bienvenida:
    def GET(self):
        return render.Bienvenida()  

if __name__ == "__main__":
    app.run()