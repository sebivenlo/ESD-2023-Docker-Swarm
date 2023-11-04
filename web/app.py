from flask import Flask, render_template
import docker

app = Flask(__name__, template_folder='templates')
client = docker.from_env()


@app.route('/')
def list_services():
    services = client.services.list()
    tasks = {service.id: service.tasks() for service in services}
    return render_template('services.html', services=services, tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
