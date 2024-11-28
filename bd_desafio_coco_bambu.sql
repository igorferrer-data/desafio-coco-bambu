CREATE DATABASE  IF NOT EXISTS `desafio_coco_bambu` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `desafio_coco_bambu`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: desafio_coco_bambu
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detail_lines`
--

DROP TABLE IF EXISTS `detail_lines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail_lines` (
  `lineItemId` int NOT NULL AUTO_INCREMENT,
  `guestCheckId` int DEFAULT NULL,
  `detailUTC` timestamp NULL DEFAULT NULL,
  `dspQty` int DEFAULT NULL,
  `aggTtl` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`lineItemId`),
  KEY `guestCheckId` (`guestCheckId`),
  CONSTRAINT `detail_lines_ibfk_1` FOREIGN KEY (`guestCheckId`) REFERENCES `fato_pedidos` (`guestCheckId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_lines`
--

LOCK TABLES `detail_lines` WRITE;
/*!40000 ALTER TABLE `detail_lines` DISABLE KEYS */;
INSERT INTO `detail_lines` VALUES (1,1122334455,'2024-01-01 12:09:09',1,45.50);
/*!40000 ALTER TABLE `detail_lines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail_metadata`
--

DROP TABLE IF EXISTS `detail_metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail_metadata` (
  `metadataId` int NOT NULL AUTO_INCREMENT,
  `lineItemId` int DEFAULT NULL,
  `metadataType` varchar(50) DEFAULT NULL,
  `metadataKey` varchar(50) DEFAULT NULL,
  `metadataValue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`metadataId`),
  KEY `lineItemId` (`lineItemId`),
  CONSTRAINT `detail_metadata_ibfk_1` FOREIGN KEY (`lineItemId`) REFERENCES `detail_lines` (`lineItemId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_metadata`
--

LOCK TABLES `detail_metadata` WRITE;
/*!40000 ALTER TABLE `detail_metadata` DISABLE KEYS */;
INSERT INTO `detail_metadata` VALUES (1,1,'discount','discountValue','-4.50'),(2,1,'serviceCharge','chargeValue','5.00'),(3,1,'tenderMedia','paymentMethod','Cartão de Crédito'),(4,1,'errorCode','errorMessage','Erro ao finalizar pagamento');
/*!40000 ALTER TABLE `detail_metadata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_datas`
--

DROP TABLE IF EXISTS `dim_datas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_datas` (
  `bus_dt` date NOT NULL,
  `ano` int DEFAULT NULL,
  `mes` int DEFAULT NULL,
  `dia` int DEFAULT NULL,
  `dia_da_semana` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bus_dt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_datas`
--

LOCK TABLES `dim_datas` WRITE;
/*!40000 ALTER TABLE `dim_datas` DISABLE KEYS */;
INSERT INTO `dim_datas` VALUES ('2024-01-01',2024,1,1,'Segunda-feira'),('2024-01-02',2024,1,2,'Terça-feira');
/*!40000 ALTER TABLE `dim_datas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_itens`
--

DROP TABLE IF EXISTS `dim_itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_itens` (
  `menuItemId` int NOT NULL,
  `nome_item` varchar(100) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`menuItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_itens`
--

LOCK TABLES `dim_itens` WRITE;
/*!40000 ALTER TABLE `dim_itens` DISABLE KEYS */;
INSERT INTO `dim_itens` VALUES (101,'Camarão Internacional','Prato Principal',45.50),(102,'Refrigerante Lata','Bebida',5.00);
/*!40000 ALTER TABLE `dim_itens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_lojas`
--

DROP TABLE IF EXISTS `dim_lojas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_lojas` (
  `store_id` int NOT NULL,
  `locRef` varchar(50) DEFAULT NULL,
  `nome_loja` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_lojas`
--

LOCK TABLES `dim_lojas` WRITE;
/*!40000 ALTER TABLE `dim_lojas` DISABLE KEYS */;
INSERT INTO `dim_lojas` VALUES (1,'99 CB CB','Loja Lago Sul'),(2,'02 CB DF','Loja Brasília');
/*!40000 ALTER TABLE `dim_lojas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fato_pedidos`
--

DROP TABLE IF EXISTS `fato_pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fato_pedidos` (
  `guestCheckId` int NOT NULL,
  `store_id` int DEFAULT NULL,
  `bus_dt` date DEFAULT NULL,
  `menuItemId` int DEFAULT NULL,
  `subTtl` decimal(10,2) DEFAULT NULL,
  `chkTtl` decimal(10,2) DEFAULT NULL,
  `dscTtl` decimal(10,2) DEFAULT NULL,
  `taxTtl` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`guestCheckId`),
  KEY `store_id` (`store_id`),
  KEY `bus_dt` (`bus_dt`),
  KEY `menuItemId` (`menuItemId`),
  CONSTRAINT `fato_pedidos_ibfk_1` FOREIGN KEY (`store_id`) REFERENCES `dim_lojas` (`store_id`),
  CONSTRAINT `fato_pedidos_ibfk_2` FOREIGN KEY (`bus_dt`) REFERENCES `dim_datas` (`bus_dt`),
  CONSTRAINT `fato_pedidos_ibfk_3` FOREIGN KEY (`menuItemId`) REFERENCES `dim_itens` (`menuItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fato_pedidos`
--

LOCK TABLES `fato_pedidos` WRITE;
/*!40000 ALTER TABLE `fato_pedidos` DISABLE KEYS */;
INSERT INTO `fato_pedidos` VALUES (1122334455,1,'2024-01-01',101,45.50,50.00,-4.50,5.00);
/*!40000 ALTER TABLE `fato_pedidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-27  23:42:21
