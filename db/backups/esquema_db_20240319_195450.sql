
CREATE TABLE `cajas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `createDate` datetime NOT NULL,
  `createUser` varchar(255) DEFAULT NULL,
  `updateDate` datetime DEFAULT NULL,
  `updateUser` varchar(255) DEFAULT NULL,
  `deleteDate` datetime DEFAULT NULL,
  `deleteUser` varchar(255) DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT '0',
  `amount` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`code`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;


CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id auto incrementeble',
  `name` varchar(250) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(500) NOT NULL,
  `createDate` timestamp NOT NULL,
  `updateDate` timestamp NULL DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT NULL,
  `deleteDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


CREATE TABLE `carpetas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `caja_id` int(11) NOT NULL,
  `code` varchar(250) NOT NULL,
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `createUser` varchar(50) DEFAULT NULL,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updateUser` varchar(50) DEFAULT NULL,
  `deleteDate` datetime DEFAULT NULL,
  `deleteUser` varchar(50) DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


CREATE TABLE `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;



