-- 1. 전체 데이터 조회하기
SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
-- --------
-- 1000000

-- 2. 하나만 조회하기
SELECT COUNT(*) FROM healthcare LIMIT 1;