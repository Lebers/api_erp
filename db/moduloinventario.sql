-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 18-03-2024 a las 06:36:33
-- Versión del servidor: 5.7.36
-- Versión de PHP: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `moduloinventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cajas`
--

DROP TABLE IF EXISTS `cajas`;
CREATE TABLE IF NOT EXISTS `cajas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `createDate` datetime NOT NULL,
  `createUser` varchar(255) DEFAULT NULL,
  `updateDate` datetime DEFAULT NULL,
  `updateUser` varchar(255) DEFAULT NULL,
  `deleteDate` datetime DEFAULT NULL,
  `deleteUser` varchar(255) DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`code`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cajas`
--

INSERT INTO `cajas` (`id`, `code`, `createDate`, `createUser`, `updateDate`, `updateUser`, `deleteDate`, `deleteUser`, `is_delete`) VALUES
(2, 'asds', '2024-03-17 22:54:22', 'feber', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE IF NOT EXISTS `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `logs`
--

INSERT INTO `logs` (`id`, `message`, `created_at`) VALUES
(17, '1146 (42S02): Table \'moduloinventario.userss\' doesn\'t exist', '2024-03-18 00:50:47'),
(16, '(\'body\', \'password\'): Field required', '2024-03-18 00:20:14'),
(15, '(\'body\', \'username\'): Field required; (\'body\', \'password\'): Field required', '2024-03-18 00:11:36'),
(14, '(\'body\', \'username\'): Field required; (\'body\', \'password\'): Field required', '2024-03-18 00:11:28'),
(13, '1146 (42S02): Table \'moduloinventario.userss\' doesn\'t exist', '2024-03-18 00:10:29'),
(12, '(\'body\', \'password\'): Field required', '2024-03-18 00:10:09'),
(11, '(\'body\', \'username\'): Field required; (\'body\', \'password\'): Field required', '2024-03-18 00:09:58'),
(10, '(\'body\', \'username\'): Field required; (\'body\', \'password\'): Field required', '2024-03-18 00:08:04'),
(18, '1146 (42S02): Table \'moduloinventario.userss\' doesn\'t exist', '2024-03-18 01:58:30'),
(19, '1146 (42S02): Table \'moduloinventario.userss\' doesn\'t exist', '2024-03-18 01:59:10'),
(20, '(\'body\', \'username\'): Field required; (\'body\', \'password\'): Field required', '2024-03-18 02:51:29'),
(21, '(\'body\', \'name\'): Field required', '2024-03-18 02:57:59'),
(22, '(\'body\',): Field required', '2024-03-18 04:40:47'),
(23, '(\'body\',): Field required', '2024-03-18 04:41:03'),
(24, '(\'body\',): Field required', '2024-03-18 04:43:13'),
(25, '(\'body\', \'fechaCreacion\'): Field required; (\'body\', \'userCreacion\'): Field required; (\'body\', \'fechaUpdate\'): Field required; (\'body\', \'userUpdate\'): Field required; (\'body\', \'fechaDelete\'): Field required; (\'body\', \'userDelete\'): Field required; (\'body\', \'is_delete\'): Field required', '2024-03-18 04:43:46'),
(26, 'Field \'(\'body\', \'fechaCreacion\')\': Field required; Field \'(\'body\', \'userCreacion\')\': Field required; Field \'(\'body\', \'fechaUpdate\')\': Field required; Field \'(\'body\', \'userUpdate\')\': Field required; Field \'(\'body\', \'fechaDelete\')\': Field required; Field \'(\'body\', \'userDelete\')\': Field required; Field \'(\'body\', \'is_delete\')\': Field required', '2024-03-18 04:45:06'),
(27, 'Field \'(\'body\',)\': Field required', '2024-03-18 05:11:28'),
(28, 'Field \'(\'body\',)\' is required', '2024-03-18 05:14:27'),
(29, 'Field \'body\' is required', '2024-03-18 05:14:55'),
(30, 'Field \'body\' is required', '2024-03-18 05:15:01'),
(31, 'Field \'body\' is required', '2024-03-18 05:15:41'),
(32, 'Field \'(\'body\',)\' is required', '2024-03-18 05:16:18'),
(33, 'Field \'(\'body\', \'codigo\')\' is required', '2024-03-18 05:16:33'),
(34, 'Field \'(\'body\', \'codigo\')\' is required', '2024-03-18 05:16:54'),
(35, 'Field \'(\'body\',)\' is required', '2024-03-18 05:17:02'),
(36, 'Field \'(\'body\', \'codigo\')\' is required', '2024-03-18 05:17:07'),
(37, 'Field \'(\'body\', \'codigo\')\' is required', '2024-03-18 05:17:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id auto incrementeble',
  `name` varchar(250) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(500) NOT NULL,
  `createDate` timestamp NOT NULL,
  `updateDate` timestamp NULL DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT NULL,
  `deleteDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `createDate`, `updateDate`, `is_delete`, `deleteDate`) VALUES
(15, 'el feber', 'feber02', '$2b$12$j1d8zV7RvptXfU3n62YObedDOxZRzf1fBYkOQ11U9v/J98N4TKE9K', '2024-03-18 03:52:04', NULL, 1, '2024-03-18 04:08:11'),
(16, 'el feber update', 'feber04', '$2b$12$IWSBFzmchKT6Te8alosF2.viNEp7pdJbh/S8NMhofgQAPq9a00CDC', '2024-03-18 04:09:58', '2024-03-18 04:13:07', NULL, NULL),
(17, 'el feber', 'feber02', '$2b$12$FAhQ8p93YZ8MjLLafuB4DO3Dm8RssBzRGaXnb0Hie8hPlp2WZ3/Wu', '2024-03-18 04:12:01', NULL, 1, '2024-03-18 04:14:17');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
