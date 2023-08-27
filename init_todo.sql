-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(56) NOT NULL,
    students_groups INTEGER,
    FOREIGN KEY (students_groups) REFERENCES students_groups (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- Table: groups
DROP TABLE IF EXISTS students_groups;
CREATE TABLE students_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(56) NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(56) NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(56) NOT NULL,
    teachers_id INTEGER,
    FOREIGN KEY (teachers_id) REFERENCES teachers (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- Table: rating
DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rate INTEGER NOT NULL,
    students_id INTEGER,
    subjects_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (students_id) REFERENCES students (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    FOREIGN KEY (subjects_id) REFERENCES subjects (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);