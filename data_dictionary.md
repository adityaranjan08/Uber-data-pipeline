# 📘 Uber Ride Data Dictionary

| Column Name      | Type     | Description                             |
|------------------|----------|-----------------------------------------|
| ride_id          | String   | Unique ID of the ride                   |
| timestamp        | Datetime | Ride start time                         |
| pickup_location  | String   | Where the ride started                  |
| drop_location    | String   | Where the ride ended                    |
| distance_km      | Float    | Total distance covered                  |
| fare_amount      | Float    | Fare charged in INR                     |
| payment_method   | String   | Card / Cash / UPI / Wallet              |
| driver_id        | String   | ID assigned to the driver               |
| rating           | Float    | Rating given by the passenger (1 to 5)  |
