'''
entry point for wsgi server when developing locally, point at this when
developing with a debugger
'''

from tabletop_utils import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
