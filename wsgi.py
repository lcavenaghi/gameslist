import logging
from main import app

if __name__ == '__main__':
    app.logger= logging.getLogger(__name__)
    app.run(debug=True, port=80)