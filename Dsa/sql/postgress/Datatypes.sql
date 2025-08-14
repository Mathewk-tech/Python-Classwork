CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    Created_at TIMESTAMP
);

--INSER INTO student (name,email,dob,phone,marks)
--VALUES('alice','alice@gmail.com','2002-05-14',)