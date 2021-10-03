# ***************************************************************************************


#    Title: Coffee and Wifi
#    Author: Jeffrey jeremiah
#    Date: 2021
#    Code version: 2.0
#    Availability: https://github.com/jeffreyjeremiah1
#
# **************************************************************************************#


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# Created Form for adding new cafe information
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = StringField('Coffee Rating', validators=[DataRequired()])
    wifi_rating = StringField('Wifi Strength Rating', validators=[DataRequired()])
    power_socket = StringField('Power Socket Availability', validators=[DataRequired()])
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# adds input from form to csv_file
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    info = [form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee_rating.data,
            form.wifi_rating.data, form.power_socket.data]
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow(info)
            return render_template('cafes.htm')
    return render_template('add.html', form=form)


# displays the data in the csv_file to the cafes page
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
