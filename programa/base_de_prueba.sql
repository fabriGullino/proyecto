-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-09-2023 a las 04:34:07
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base_de_prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidades`
--

CREATE TABLE `especialidades` (
  `cod_especialidad` int(10) NOT NULL,
  `Especialidad` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `especialidades`
--

INSERT INTO `especialidades` (`cod_especialidad`, `Especialidad`) VALUES
(2, 'ofalmologia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historia_clinica`
--

CREATE TABLE `historia_clinica` (
  `cod_historia` int(10) NOT NULL,
  `descripcion` mediumtext NOT NULL,
  `paciente` int(10) NOT NULL,
  `fecha` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historia_clinica`
--

INSERT INTO `historia_clinica` (`cod_historia`, `descripcion`, `paciente`, `fecha`) VALUES
(8, 'hola soy fabricio', 8, '03/05/2005'),
(9, 'hola soy fabricio', 8, '03/05/2005'),
(10, 'hola soy fabricio', 8, '03/05/2005'),
(12, 'hola soy fabricio', 8, '03/05/2005'),
(17, 'hola soy fabricio', 8, '03/05/2005'),
(18, 'hola soy fabricio', 8, '03/05/2005');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `internaciones`
--

CREATE TABLE `internaciones` (
  `cod_internacion` int(10) NOT NULL,
  `fecha` mediumtext NOT NULL,
  `hora` mediumtext NOT NULL,
  `paciente` int(10) NOT NULL,
  `medico` int(10) NOT NULL,
  `patologia` int(10) NOT NULL,
  `piso` mediumtext NOT NULL,
  `num_hab` mediumtext NOT NULL,
  `num_cama` mediumtext NOT NULL,
  `alta` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `cod_medico` int(10) NOT NULL,
  `Nombre` mediumtext NOT NULL,
  `Mapellido` mediumtext NOT NULL,
  `fecha_de_nac` mediumtext NOT NULL,
  `dni` mediumtext NOT NULL,
  `direc` mediumtext NOT NULL,
  `telefono` mediumtext NOT NULL,
  `especialidad` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `cod_paciente` int(10) NOT NULL,
  `Nombre` mediumtext NOT NULL,
  `Papellido` mediumtext NOT NULL,
  `fecha_de_nac` mediumtext NOT NULL,
  `dni` mediumtext NOT NULL,
  `direc` mediumtext NOT NULL,
  `telefono` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`cod_paciente`, `Nombre`, `Papellido`, `fecha_de_nac`, `dni`, `direc`, `telefono`) VALUES
(8, 'fabricio', 'gullino', '03/05/2005', '46114454', 'direccion uno', '3364253934'),
(10, 'yo', 'fdafdaf', 'dfadf', 'adfdaf', 'dfaf', 'dadafdaf'),
(11, 'cdacdac', 'dacdac', 'dacda', 'cdacdac', 'adcdacdac', '11223344');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `patologias`
--

CREATE TABLE `patologias` (
  `cod_patologia` int(10) NOT NULL,
  `Patologia` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `patologias`
--

INSERT INTO `patologias` (`cod_patologia`, `Patologia`) VALUES
(3, 'coso'),
(5, 'hola');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `cod_turno` int(10) NOT NULL,
  `fecha` mediumtext NOT NULL,
  `hora` mediumtext NOT NULL,
  `paciente` int(10) NOT NULL,
  `medico` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `cod_usuario` int(10) NOT NULL,
  `nom_usuario` mediumtext NOT NULL,
  `contraseña` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`cod_usuario`, `nom_usuario`, `contraseña`) VALUES
(1, 'admin', 'clinet');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `especialidades`
--
ALTER TABLE `especialidades`
  ADD PRIMARY KEY (`cod_especialidad`),
  ADD KEY `Especialidad` (`Especialidad`(768));

--
-- Indices de la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD PRIMARY KEY (`cod_historia`),
  ADD KEY `paciente` (`paciente`);

--
-- Indices de la tabla `internaciones`
--
ALTER TABLE `internaciones`
  ADD PRIMARY KEY (`cod_internacion`),
  ADD KEY `paciente` (`paciente`,`medico`),
  ADD KEY `medico` (`medico`),
  ADD KEY `patologia` (`patologia`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`cod_medico`),
  ADD KEY `especialidad` (`especialidad`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`cod_paciente`);

--
-- Indices de la tabla `patologias`
--
ALTER TABLE `patologias`
  ADD PRIMARY KEY (`cod_patologia`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`cod_turno`),
  ADD KEY `paciente` (`paciente`,`medico`),
  ADD KEY `medico` (`medico`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`cod_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `especialidades`
--
ALTER TABLE `especialidades`
  MODIFY `cod_especialidad` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  MODIFY `cod_historia` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `internaciones`
--
ALTER TABLE `internaciones`
  MODIFY `cod_internacion` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `cod_medico` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `cod_paciente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `patologias`
--
ALTER TABLE `patologias`
  MODIFY `cod_patologia` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `cod_turno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `cod_usuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD CONSTRAINT `historia_clinica_ibfk_1` FOREIGN KEY (`paciente`) REFERENCES `pacientes` (`cod_paciente`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `internaciones`
--
ALTER TABLE `internaciones`
  ADD CONSTRAINT `internaciones_ibfk_1` FOREIGN KEY (`paciente`) REFERENCES `pacientes` (`cod_paciente`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `internaciones_ibfk_2` FOREIGN KEY (`medico`) REFERENCES `medicos` (`cod_medico`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `internaciones_ibfk_3` FOREIGN KEY (`patologia`) REFERENCES `patologias` (`cod_patologia`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD CONSTRAINT `medicos_ibfk_1` FOREIGN KEY (`especialidad`) REFERENCES `especialidades` (`cod_especialidad`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `turnos_ibfk_1` FOREIGN KEY (`paciente`) REFERENCES `pacientes` (`cod_paciente`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnos_ibfk_2` FOREIGN KEY (`medico`) REFERENCES `medicos` (`cod_medico`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
