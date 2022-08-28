from blog import application

def run_app(environ, start_response):
    return application(environ, start_response)
