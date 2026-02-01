/*

Build a database for Copa America Centenario

To calculate standings for each group and build the bracket for the playoffs

Dave Kritzberg

6/12/2016

Later: do the same for European Cup 2016

Eventually: Implement ELO rankings

*/

DROP DATABASE IF EXISTS Copa_America;

CREATE DATABASE Copa_America;

GRANT ALL ON Copa_America TO dave@Kalmar;

USE Copa_America;

DROP TABLE IF EXISTS countries;

CREATE TABLE countries (id INT, country_name VARCHAR(50), country_group VARCHAR(1));

INSERT INTO countries (id, country_name, country_group) VALUES (1, 'United States', 'A');
INSERT INTO countries (id, country_name, country_group) VALUES (2, 'Colombia', 'A');
INSERT INTO countries (id, country_name, country_group) VALUES (3, 'Costa Rica', 'A');
INSERT INTO countries (id, country_name, country_group) VALUES (4, 'Paraguay', 'A');

INSERT INTO countries (id, country_name, country_group) VALUES (5, 'Brazil', 'B');
INSERT INTO countries (id, country_name, country_group) VALUES (6, 'Ecuador', 'B');
INSERT INTO countries (id, country_name, country_group) VALUES (7, 'Peru', 'B');
INSERT INTO countries (id, country_name, country_group) VALUES (8, 'Haiti', 'B');

INSERT INTO countries (id, country_name, country_group) VALUES (9, 'Uruguay', 'C');
INSERT INTO countries (id, country_name, country_group) VALUES (10, 'Mexico', 'C');
INSERT INTO countries (id, country_name, country_group) VALUES (11, 'Venezuela', 'C');
INSERT INTO countries (id, country_name, country_group) VALUES (12, 'Jamaica', 'C');

INSERT INTO countries (id, country_name, country_group) VALUES (13, 'Argentina', 'D');
INSERT INTO countries (id, country_name, country_group) VALUES (14, 'Chile', 'D');
INSERT INTO countries (id, country_name, country_group) VALUES (15, 'Bolivia', 'D');
INSERT INTO countries (id, country_name, country_group) VALUES (16, 'Panama', 'D');


DROP TABLE IF EXISTS match_days;

CREATE TABLE match_days (id INT)

INSERT INTO match_days (id) VALUES (1);
INSERT INTO match_days (id) VALUES (2);
INSERT INTO match_days (id) VALUES (3);


DROP TABLE IF EXISTS venues;

CREATE TABLE venues (id INT, city_name VARCHAR(50), stadium VARCHAR(50), capacity INT);

INSERT INTO venues (id, city_name, stadium, capacity) VALUES (1, 'Seattle', 'CenturyLink Field', 67000)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (2, 'Chicago', 'Soldier Field', 63500)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (3, 'Boston', 'Gillette Stadium', 68756)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (4, 'East Rutherford', 'MetLife Stadium', 82566)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (5, 'Santa Clara', 'Levis Stadium', 68500)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (6, 'Philadelphia', 'Lincoln Financial Field', 69176)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (7, 'Pasadena', 'Rose Bowl', 92542)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (8, 'Glendale', 'University of Phoenix Stadium', 63400)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (9, 'Houston', 'NRG Stadium', 71795)
INSERT INTO venues (id, city_name, stadium, capacity) VALUES (10, 'Orlando', 'Camping World Stadium', 60219)


DROP TABLE IF EXISTS matches;

CREATE TABLE matches (id INT, match_date DATE, match_day_id INT, venue_id INT,
       	     home_id INT, visitor_id INT, home_score INT, visitor_score INT);

INSERT INTO matches (id, match_date, match_day_id, venue_id, home_score, visitor_score) VALUES (1, '2016-06-03', 1, 5, 1, 2, 0, 2)
INSERT INTO matches (id, match_date, match_day_id, venue_id, home_score, visitor_score) VALUES (1, '2016-06-03', 1, 5, 1, 2, 0, 2)
