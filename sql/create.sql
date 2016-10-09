CREATE table iot_temperature (
  id serial primary key,
  sensor varchar(200),
  measured_at timestamp,
  reading decimal not null
);