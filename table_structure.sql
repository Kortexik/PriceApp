CREATE TABLE `data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NULL DEFAULT NULL,
  `name` varchar(125) DEFAULT NULL,
  `price` decimal(7,2) DEFAULT NULL,
  `link` varchar(1000) DEFAULT NULL,
  `date_only` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TRIGGER `calculate_date_only` AFTER INSERT ON `data` FOR EACH ROW SET NEW.date_only = DATE(NEW.datetime);