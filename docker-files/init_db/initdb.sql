CREATE TABLE departments (
id int not null primary key,
department varchar(255) not null
);

CREATE TABLE jobs (
id int not null primary key,
job varchar(255) not null
);

CREATE TABLE hired_employees (
id int not null primary key,
name varchar(255) not null,
datetime varchar(255) not null,
department_id int not null references departments(id),
job_id int not null references jobs(job)
);


