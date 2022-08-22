-- INNER JOIN
-- A와 B테이블에서 값이 일치하는 것들만

SELECT * FROM users INNER JOIN role ON users.role_id = role.id;

SELECT users.name, role.title FROM users INNER JOIN role ON users.role_id = role.id;

-- 스태프(2)만 출력
SELECT * FROM users INNER JOIN role ON users.role_id = role.id WHERE role.id = 2;

-- 이름을 내림착순으로 출력
SELECT * FROM users INNER JOIN role ON users.role_id = role.id ORDER BY uesrs.name DESC;

-- LEFT OUTER JOIN
SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id;

SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id WHERE articles.user_id IS NOT NULL;

-- FULL OUTER JOIN
SELECT * FROM articles FULL OUTER JOIN users ON articles.user_id = users.id;

-- CROSS JOIN
SELECT * FROM users CROSS JOIN role;