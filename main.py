# main.py
from dashboard import create_dash_application

if __name__ == "__main__":
    app = create_dash_application()
    app.run_server(debug=True)


