
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TINYTEXT,
    age TINYINT UNSIGNED,
    gender TINYTEXT,
    group_id TINYINT,
    FOREIGN KEY (group_id) REFERENCES groups (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    
    CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TINYTEXT
    );

    CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TINYTEXT,
    age TINYINT UNSIGNED,
    gender TINYTEXT
    );

    CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TINYTEXT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );

    CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value TINYTEXT UNSIGNED,
    student_id INT,
    subject_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
    );