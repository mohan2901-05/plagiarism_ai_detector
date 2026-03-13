CREATE DATABASE plagiarism_ai;

USE plagiarism_ai;

CREATE TABLE reports (

id INT AUTO_INCREMENT PRIMARY KEY,

filename VARCHAR(255),

input_text TEXT,

plagiarism_score FLOAT,

matched_source VARCHAR(255),

ai_probability FLOAT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);