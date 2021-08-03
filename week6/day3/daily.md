
<!-- Daily
 -->
|	|
|:----|
|	|
|CREATE TABLE student(|
|    id SERIAL PRIMARY KEY NOT NULL,|
|    student_name VARCHAR (100) NOT NULL)|
|CREATE TABLE student_course AS s_c(|
|    id SERIAL PRIMARY KEY NOT NULL,|
|    course_name VARCHAR (255) NOT NULL,|
|    course_id INT NOT NULL REFERENCES student(id),    FOREIGN KEY (course_id);)|
|CREATE TABLE course(|
|    id SERIAL PRIMARY KEY NOT NULL,|
|    course_name VARCHAR (255) NOT NULL,|
|	teacher VARCHAR (100),|
|    student_id INT NOT NULL REFERENCES student(id),|
|   	s_c_id INT NOT NULL REFERENCES s_c(id),|
|    FOREIGN KEY (student_id, s_c);|
|)|
|--> INNER|
|SELECT * FROM student AS s|
|INNER JOIN s_c ON s.id = s_c.band_id|
|---> LEFT|
|SELECT * FROM s_c|
|LEFT JOIN course ON bands.id = s_c.band_id|
|-->RIGHT|
|SELECT * FROM s_c|
|RIGHT JOIN course ON s_c.id = course.band_id|
|-- -->FULL|
|select * FROM student|
|FULL JOIN course|
|on student.id = course.albums_id|
|	|
