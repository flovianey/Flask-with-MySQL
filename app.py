from urllib import request
from flask import Flask, render_template, session, redirect, url_for
import pymysql
import os

app = Flask(__name__)


class Database:
    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = '1234567890'
        db = 'car_tracking'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def registered_users(self):
        self.cur.execute("SELECT id, Name, Gender, Role, Phone, Number_Plate FROM registered_number_plates")
        result = self.cur.fetchall()
        return result

    def users_entry(self):
        self.cur.execute("SELECT id, Name, Gender, Role, Phone, Number_Plate, Arrival_time FROM gctu_arrival")
        result = self.cur.fetchall()
        return result

    def users_exit(self):
        self.cur.execute("SELECT id, Name, Gender, Role, Phone, Number_Plate, Departure_time FROM gctu_departure")
        result = self.cur.fetchall()
        return result

    def guest_arrival(self):
        self.cur.execute("SELECT id, Name, rfid_uid, Number_Plate, Arrival_time FROM guest_arrival")
        result = self.cur.fetchall()
        return result

    def guest_departure(self):
        self.cur.execute("SELECT id, Name, rfid_uid, Number_Plate, Departure_time FROM guest_departure")
        result = self.cur.fetchall()
        return result


@app.route('/')
def index():
    def db_query():
        db = Database()
        my_users = db.registered_users()
        return my_users

    res = db_query()
    return render_template('users.html', result=res)


@app.route('/gctu_entry')
def gctu_entry():
    def db_query():
        db = Database()
        my_users = db.users_entry()
        return my_users

    res = db_query()
    return render_template('gctu_arrival.html', result=res)


@app.route('/gctu_exit')
def gctu_exit():
    def db_query():
        db = Database()
        my_users = db.users_exit()
        return my_users

    res = db_query()
    return render_template('gctu_departure.html', result=res)


@app.route('/guest_entry')
def guest_entry():
    def db_query():
        db = Database()
        my_users = db.guest_arrival()
        return my_users

    res = db_query()
    return render_template('guest_arrival.html', result=res)


@app.route('/guest_exit')
def guest_exit():
    def db_query():
        db = Database()
        my_users = db.guest_departure()
        return my_users

    res = db_query()
    return render_template('guest_departure.html', result=res)


if __name__ == '__main__':
    app.run()
