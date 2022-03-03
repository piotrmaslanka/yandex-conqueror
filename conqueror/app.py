import os

import flask
import flask_json
import yaml
from flasgger import Swagger
from flask_cors import CORS

from flask_satella_metrics import SatellaMetricsMiddleware
from satella.instrumentation.metrics import getMetric
from flask_satella_metrics.prometheus_exporter import PrometheusExporter

from flask_requests_logging import FlaskRequestsLogging

__version__ = '1.0'

app = flask.Flask(__name__)

app.config['JSON_ADD_STATUS'] = False
app.config['DEBUG'] = os.environ.get('DEBUG', '1') == '1'
app.config['TESTING'] = os.environ.get('CI', '0') == '1'

flask_json.FlaskJSON(app)
CORS(app, supports_credentials=True)
FlaskRequestsLogging(app)

with open('/app/app-template.yml', 'r') as f_in:
    template = yaml.load(f_in, Loader=yaml.Loader)

template['info']['version'] = __version__
app.config['SWAGGER'] = {'openapi': '3.0.2'}
Swagger(app, template=template)


@app.route('/')
def redirect_to_swagger():
    return flask.redirect('/apidocs')


SatellaMetricsMiddleware(app, summary_metric=getMetric('yandex.api.call_time.summary', 'summary',
                                                       quantiles=[0.5, 0.95, 0.99]),
                         histogram_metric=getMetric('yandex.api.call_time.histogram', 'histogram'),
                         response_codes_metric=getMetric('yandex.api.response_codes', 'counter'))

app.register_blueprint(PrometheusExporter({'service_name': 'yandex'}))


