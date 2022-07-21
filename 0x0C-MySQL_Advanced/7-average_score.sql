-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DELIMITER | CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id int) BEGIN
UPDATE users
SET average_score = (
        SELECT AVG(score)
        FROM corrections AS c
        WHERE c.user_id = user_id
    );
UPDATE users
SET average_score = avg_score
WHERE id = user_id;
END;
|
