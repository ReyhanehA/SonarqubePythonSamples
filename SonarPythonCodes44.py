import logging

logger = logging.getLogger(__name__)

@app.route('/example')
def log():
    data = request.args["data"]
    logger.log(logging.CRITICAL, "%s", data) # Noncompliant

