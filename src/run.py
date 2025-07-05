"""Run RetroBoard server"""

from app import create_app
from app.routes.board_routes import register_static_routes

app = create_app()
register_static_routes(app)

if __name__ == '__main__':
    app.run()
