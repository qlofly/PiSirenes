import re
import os
import subprocess

# from flask import request
from multiprocessing import Value
from subprocess import Popen, PIPE
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	uptim = subprocess.Popen(["awk", r'{printf("%d day(s) %02d:%02d:%02d\n",($1/60/60/24),($1/60/60%24),($1/60%60),($1%60))}', "/proc/uptime"], stdout=subprocess.PIPE).communicate()
	uptime = re.findall(r'\d\ \w\w\w\D\D\D \d\d:\d\d:\d\d', str(uptim))
	empty = ""
	templateData = {'timenow': empty.join(uptime)}
	return render_template('index.html', **templateData)
