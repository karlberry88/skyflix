

DROP TABLE IF EXISTS `film`;

CREATE TABLE `film` (
  `film_id` int NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `genre` varchar(45) DEFAULT NULL,
  `age rating` varchar(45) DEFAULT NULL,
  `trailer` varchar(500) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL,
  PRIMARY KEY (`film_id`)
)
-- Dumping data for table `film`

INSERT INTO `film` VALUES (1,'cars	','talking cars','kids	','pg','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/-Vui-DhwIAg\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
