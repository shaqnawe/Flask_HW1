from app import create_app

app = create_app()

@app.shell_context_processor
def application_context():
    return f'<h1>Hello</h1>'