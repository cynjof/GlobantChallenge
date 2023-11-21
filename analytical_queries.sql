with quarter_year as (
SELECT  d.department,
		j.job,
		QUARTER(datetime) as Q,
		count(*) as hired_employees
FROM hired_employees he
JOIN jobs j
	ON j.id  = he.job_id
JOIN departments d
	ON d.id  = he.department_id
WHERE YEAR(he.datetime) = 2021
GROUP BY  d.department,
		  j.job,
		  QUARTER(datetime)
)
SELECT  department,
		job,
		CASE when Q = 1 THEN hired_employees ELSE 0 END Q1,
		CASE when Q = 2 THEN hired_employees ELSE 0 END Q2,
		CASE when Q = 3 THEN hired_employees ELSE 0 END Q3,
		CASE when Q = 4 THEN hired_employees ELSE 0 END Q4
FROM quarter_year
ORDER BY departmenT ASC ,
		job ASC
;


with hired_employees_dpto as (
SELECT d.department,
		COUNT(he.id) as hired_by_dpto
		FROM hired_employees he
		JOIN departments d
			ON d.id  = he.department_id
		WHERE YEAR(he.datetime) = 2021
		GROUP BY d.department
),
avg_hired as (
SELECT ROUND(AVG(hired_by_dpto))
FROM hired_employees_dpto
)
SELECT d.id,
		h.department,
		h.hired_by_dpto
FROM hired_employees_dpto h
JOIN departments d
	ON h.department = d.department
WHERE h.hired_by_dpto > (SELECT ROUND(AVG(hired_by_dpto))
							FROM hired_employees_dpto)
;
