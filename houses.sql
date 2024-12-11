use houses;

Set global local_infile = 1;

LOAD DATA LOCAL INFILE 'D:/Files/code/python_learning/houses.csv'
INTO TABLE houses
FIELDS TERMINATED BY ','  -- CSV delimiter
LINES TERMINATED BY '\n'  -- New line to mark each record
(website, price, link);

SELECT * from houses;

INSERT INTO houses (website, price, link)
VALUES
('', '', '');

delimiter $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Insert_House`(
IN h_website text,
IN h_price float,
IN h_link text,
IN h_status varchar(20),
IN h_notes text
)
BEGIN
INSERT INTO houses (website, price, link, I_status, notes)
VALUES (h_website, h_price, h_link, h_status, h_notes);
select * from houses;
END $$
delimiter ;

ALTER TABLE houses
ADD COLUMN WBS bool;

DELETE FROM HOUSES
WHERE id = 48;

select * from houses;


call Insert_House(
'howoge',
692,
'https://www.howoge.de/immobiliensuche/wohnungssuche/detail/1910-33140-57.html?t=ibw',
'request not sent',
NULL,
FALSE);

ALTER TABLE houses AUTO_INCREMENT = 47;

ALTER TABLE houses
ADD UNIQUE (link);

ALTER TABLE houses
MODIFY COLUMN link VARCHAR(500);

SELECT * from houses
where link like 'https://www.howoge.de/immobiliensuche/wohnungssuche/detail/1771%';

update houses
set link = NULL
WHERE id = 44;

SELECT * FROM houses
WHERE date_time > '2024-12-10 19:50:54'
AND I_status = 'request not sent';

SELECT * FROM houses
WHERE website = 'howoge'
AND I_status = 'request not sent'
AND WBS = 0;

SELECT * FROM houses;
WHERE website = 'howoge';
