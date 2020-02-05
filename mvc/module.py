# @@@@@@@@@@@@@@@@@@@ Sendinblue module End @@@@@@@@@@@@@@@@@@@@@@@@@
from mvc import app
from flask import Flask, render_template, url_for, request, redirect, jsonify
import pymongo
import string
import re
from random import *
# Password Hashing
from flask_bcrypt import Bcrypt

from mvc import database
