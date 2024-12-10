from livereload import Server, shell


def rebuild():
    print("Site rebuilt")

rebuild()

server = Server()
server.watch('index.html', rebuild)
server.serve(root='.')