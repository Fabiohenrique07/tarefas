DROP DATABASE IF

CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `terefas`;

CREATE TABLE IF NOT EXISTS `tarefas` (
    `id_tarefa` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL
);
