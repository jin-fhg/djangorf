## ENV Preparation
1. Create a python virtual environment by going to the project folder and type: python<version> -m venv <virtual-environment-name>
2. install the libraries found in the requirements.txt file using: pip install -r requirements.txt 
3. Open the djangorf/restful/restful/settings.py file and replace the database credentials according to your preference
4. Make sure that your local server and database are up and running
5. Start by making migrations to avoid error. Type:
   - python manage.py makemigrations
   - then type: python manage.py migrate
7. You can create an admin user first by typing: django-admin createsuperuser
8. Start the project by going to djangorf/restful/ and type: python manage.py runserver


## Issue encountered
I had an issue doing the OrderFilter for distance, since this is not a model field. I cannot include it to the same viewset for Ride without adding it as one of the Model Field.

## Bonus SQL Command

WITH RideDurations AS (
  SELECT
    r.id,
    u.first_name,
    u.last_name,
    DATE_FORMAT(e1.created_at, '%Y-%m') AS ride_month,
    TIMEDIFF(MAX(CASE WHEN e2.description = "Status changed to dropoff" THEN e2.created_at END),
             MIN(CASE WHEN e1.description = "Status changed to pickup" THEN e1.created_at END)) AS duration
  FROM djangorf.api_ride r
  JOIN djangorf.api_user u ON r.driver_id = u.id
  JOIN djangorf.api_ride_event e1 ON r.id = e1.ride_id
  JOIN djangorf.api_ride_event e2 ON r.id = e2.ride_id
  GROUP BY r.id, u.first_name, u.last_name, DATE_FORMAT(e1.created_at, '%Y-%m')
  HAVING TIMEDIFF(MAX(CASE WHEN e2.description = "Status changed to dropoff" THEN e2.created_at END),
                 MIN(CASE WHEN e1.description = "Status changed to pickup" THEN e1.created_at END)) > '1:00:00'
)
SELECT
  ride_month,
  CONCAT(first_name, " ", last_name) AS driver,
  COUNT(*) AS trips_over_hour
FROM RideDurations
GROUP BY ride_month, driver;


