import os
import platform
import psutil
from flask import Flask, jsonify, render_template

APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/info')
def get_info():
    integrantes = ["Mateus Roese Tucunduva", "Matheus Yamamoto Dias", "Victor Ryuki Tamezava"] 
    return jsonify(integrantes=integrantes)

@APP.route('/metricas')
def get_metricas():
    pid = os.getpid()

    processo = psutil.Process(pid)
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    uso_cpu = processo.cpu_percent(interval=0.1)
    so_nome = platform.system()
    so_versao = platform.version()

    metricas = {
        "PID": pid,
        "Memória usada": round(memoria_mb, 2),
        "Uso da CPU": uso_cpu,
        "Sistema Operacional": f"{so_nome} ({so_versao})"
    }
    return jsonify(metricas)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)