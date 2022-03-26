Globally:
pip3 install pysqlcipher3 
pip3 install psycopg2-binary 

in venv:
pip3 install flask-SQLAlchemy

FLASK_APP=app.py FLASK_ENV=development && flask run

select * from donor; join donation 
on donor.id = donor_id
join volunteer 
on Volunteer.id = volunteer_id;

INSERT INTO Donor(name,city,address,phone,facebook_link) VALUES('Talha', 'Debrecen', 'Kassai', '+363077954', 'httpst');
INSERT INTO Volunteer(name,city,address,phone,facebook_link) VALUES('darwish', 'BP', 'Corvin', '+3630773454', 'httpsd');
INSERT INTO Donation(donor_id,volunteer_id,genre,pickup_time,pickup_address) VALUES(1, 1, 'food', '20120618 10:34:09 AM', 'Nyugati');

INSERT INTO Donor(name,city,address,phone,facebook_link) VALUES('Talha', 'Debrecen', 'Kassai', '+363077954', 'httpst');
SELECT * from donor;
delete from donor;

