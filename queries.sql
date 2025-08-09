USE nj_state_teachers_salaries;
SELECT AVG(salary) FROM nj_state_teachers_salaries.salaries;
SELECT COUNT(last_name) FROM nj_state_teachers_salaries.salaries WHERE salary > 150000;
SELECT last_name FROM nj_state_teachers_salaries.salaries WHERE salary > 150000 and experience_total < 5;
SELECT MAX(salary) FROM nj_state_teachers_salaries.salaries WHERE primary_job like('%Preschool%');
SELECT MAX(salary) FROM nj_state_teachers_salaries.salaries WHERE primary_job like('%School Counselor%');
SELECT MAX(salary) FROM nj_state_teachers_salaries.salaries WHERE primary_job like('%Principal%');
SELECT MAX(salary) FROM nj_state_teachers_salaries.salaries WHERE primary_job like('%School Psychologist%');
SELECT MAX(salary) FROM nj_state_teachers_salaries.salaries WHERE primary_job like('%Kindergarten%');
SELECT last_name, first_name, salary, MIN(salary) FROM nj_state_teachers_salaries.salaries 
WHERE district = 'Atlantic City'
GROUP BY last_name, first_name, salary;
SELECT COUNT(last_name) FROM nj_state_teachers_salaries.salaries WHERE district = 'Passaic City' and 
experience_total > 10;