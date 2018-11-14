DELIMITER //
DROP PROCEDURE IF EXISTS getAVideoFromAUser //

CREATE PROCEDURE getAVideoFromAUser(IN search VARCHAR(250), IN id INT)
BEGIN
  SELECT *
    FROM videos WHERE title = search AND userId = id;
END //
DELIMITER ;
