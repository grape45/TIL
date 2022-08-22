-- INNER JOIN
-- A와 B테이블에서 값이 일치하는 것들만

SELECT * FROM users INNER JOIN role ON users.role_id = role.id;

SELECT users.name, role.title FROM users INNER JOIN role ON users.role_id = role.id;