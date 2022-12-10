-- --------------------------------------------------------
-- Servidor:                     localhost
-- Versão do servidor:           10.9.4-MariaDB-1:10.9.4+maria~ubu2204 - mariadb.org binary distribution
-- OS do Servidor:               debian-linux-gnu
-- HeidiSQL Versão:              12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para horta_banco
CREATE DATABASE IF NOT EXISTS `horta_banco` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `horta_banco`;

-- Copiando estrutura para tabela horta_banco.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.estoque
CREATE TABLE IF NOT EXISTS `estoque` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `origem_nome` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `origem_id` int(11) DEFAULT NULL,
  `quantidade` decimal(15,2) DEFAULT 0.00,
  `tipo_movimento` int(11) DEFAULT NULL,
  `cancelado` int(11) DEFAULT 0,
  `observacoes` text CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.fertilizantes
CREATE TABLE IF NOT EXISTS `fertilizantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_id` int(11) NOT NULL,
  `nome` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `fabricante` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `data_fabricacao` date DEFAULT NULL,
  `data_validade` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categoria_id` (`categoria_id`),
  CONSTRAINT `fertilizantes_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`),
  CONSTRAINT `fertilizantes_ibfk_2` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.hortalicas
CREATE TABLE IF NOT EXISTS `hortalicas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_id` int(11) NOT NULL,
  `largura` decimal(10,2) DEFAULT NULL,
  `comprimento` decimal(10,2) DEFAULT NULL,
  `altura` decimal(10,2) DEFAULT NULL,
  `fertilizantes_id` int(11) NOT NULL,
  `nome` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categoria_id` (`categoria_id`),
  KEY `fertilizantes_id` (`fertilizantes_id`),
  CONSTRAINT `hortalicas_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`),
  CONSTRAINT `hortalicas_ibfk_2` FOREIGN KEY (`fertilizantes_id`) REFERENCES `fertilizantes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.hortas
CREATE TABLE IF NOT EXISTS `hortas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_plantio` decimal(10,2) DEFAULT NULL,
  `nome_horta` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.horta_item
CREATE TABLE IF NOT EXISTS `horta_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hortalicas_id` int(11) NOT NULL,
  `horta_id` int(11) NOT NULL,
  `quantidade` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hortalicas_id` (`hortalicas_id`),
  KEY `horta_id` (`horta_id`),
  CONSTRAINT `horta_item_ibfk_1` FOREIGN KEY (`hortalicas_id`) REFERENCES `hortalicas` (`id`),
  CONSTRAINT `horta_item_ibfk_2` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.irrigacao
CREATE TABLE IF NOT EXISTS `irrigacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_irrigacao` datetime DEFAULT NULL,
  `horta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `horta_id` (`horta_id`),
  CONSTRAINT `irrigacao_ibfk_1` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`),
  CONSTRAINT `irrigacao_ibfk_2` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`),
  CONSTRAINT `irrigacao_ibfk_3` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`),
  CONSTRAINT `irrigacao_ibfk_4` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela horta_banco.medicao
CREATE TABLE IF NOT EXISTS `medicao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valor_umidade` int(11) DEFAULT NULL,
  `data_leitura` datetime DEFAULT NULL,
  `horta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `horta_id` (`horta_id`),
  CONSTRAINT `medicao_ibfk_1` FOREIGN KEY (`horta_id`) REFERENCES `hortas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Exportação de dados foi desmarcado.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
