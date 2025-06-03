import web


urls = ("/", "Index")
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        pass
    

    def GET(self):
        
        clientes=["dejah", "luis", "carlos", "mario"]
        return render.Index(clientes)
class Static:
    
    def GET(self, filename):
        return web.httpserver.staticfile('static/' + filename)  


if __name__ == "__main__":
    app.run()