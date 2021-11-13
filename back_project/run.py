from app import create_app
from constants import CONFIG_FILENAME

app= create_app(CONFIG_FILENAME)

if __name__ =='__main__':
    app.run(host=app.config['HOST'],port=app.config['PORT'], debug=app.config['DEBUG'])