DROP TABLE IF EXISTS `film`;

CREATE TABLE `film` (
  `film_id` int NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `genre` varchar(45) DEFAULT NULL,
  `age rating` varchar(45) DEFAULT NULL,
  `trailer` varchar(500) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL,
  PRIMARY KEY (`film_id`)
);

INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (1,'Cars	','Cars is a 2006 American computer-animated sports comedy film produced by Pixar Animation Studios for Walt Disney Pictures.','kids	','pg','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/-Vui-DhwIAg\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (2,'The Godfather','Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.\n\n','drama','18','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/sY1S34973zA\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (3,'Frozen','When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.\n\nDirectors\n','kids','pg','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/TbQm5doF_Uc\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (4,'Moana','In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana\'s island, she answers the Ocean\'s call to seek out the Demigod to set things right.\n\nDirectors\nRon ClementsJohn MuskerDon Hall\n','kids','pg','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/yVzEjS6q05Q\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (5,'Guardians of the Galaxy','A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.','action','13','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/d96cjJhvlMA\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (6,'Deadpool	','A wisecracking mercenary gets experimented on and becomes immortal but ugly, and sets out to track down the man who ruined his looks.','action ','18','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/Xithigfg7dA\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (7,'Pretty Woman','A man in a legal but hurtful business needs an escort for some social events, and hires a beautiful prostitute he meets... only to fall in love.','rom com','15','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/2EBAVoN8L_U\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (8,'Life of Pi','A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.','fantasy','pg','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/3mMN693-F3U\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (9,'Jaws','When a killer shark unleashes chaos on a beach community off Cape Cod, it\'s up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.','adventure','12','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/QSDqB7T8ItM\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
INSERT INTO `film` (`film_id`,`title`,`description`,`genre`,`age rating`,`trailer`) VALUES (10,'Jurrasic Park','A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park\'s cloned dinosaurs to run loose.','adventure','pg','<iframe width=\"200\" height=\"150\" src=\"https://www.youtube.com/embed/lc0UehYemQA\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>');
