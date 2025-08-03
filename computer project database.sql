CREATE DATABASE  IF NOT EXISTS `dealer_service` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dealer_service`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: dealer_service
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `car_purchase`
--

DROP TABLE IF EXISTS `car_purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_purchase` (
  `Purchase_no` int NOT NULL,
  `phno` varchar(15) DEFAULT NULL,
  `car_name` varchar(20) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  `variant` varchar(20) DEFAULT NULL,
  `payment` varchar(20) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Purchase_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_purchase`
--

LOCK TABLES `car_purchase` WRITE;
/*!40000 ALTER TABLE `car_purchase` DISABLE KEYS */;
INSERT INTO `car_purchase` VALUES (1,'6282182971','Slavia','Blue','Top','EMI',2000000),(2,'6282182971','XUV 700','Black','Top','Net Banking',2400000),(3,'6282182971','Kodiaq','Black','Mid','Net Banking',4800000);
/*!40000 ALTER TABLE `car_purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_test`
--

DROP TABLE IF EXISTS `car_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_test` (
  `Test_id` int NOT NULL,
  `phno` varchar(15) NOT NULL,
  `car_name` varchar(45) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`Test_id`),
  UNIQUE KEY `Phno_UNIQUE` (`Test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_test`
--

LOCK TABLES `car_test` WRITE;
/*!40000 ALTER TABLE `car_test` DISABLE KEYS */;
INSERT INTO `car_test` VALUES (1,'6282182971','i20','hyundai','11:00','2025-08-13');
/*!40000 ALTER TABLE `car_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citroen`
--

DROP TABLE IF EXISTS `citroen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citroen` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citroen`
--

LOCK TABLES `citroen` WRITE;
/*!40000 ALTER TABLE `citroen` DISABLE KEYS */;
INSERT INTO `citroen` VALUES (1,'C3',800000,900000,1000000),(2,'C5',1200000,1250000,1370000),(3,'Aircross',1100000,1200000,1250000),(4,'Basalt',1000000,1100000,1200000),(5,'eC3',1000000,1100000,1200000);
/*!40000 ALTER TABLE `citroen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `honda`
--

DROP TABLE IF EXISTS `honda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `honda` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `honda`
--

LOCK TABLES `honda` WRITE;
/*!40000 ALTER TABLE `honda` DISABLE KEYS */;
INSERT INTO `honda` VALUES (1,'City',1500000,1700000,2000000),(2,'Amaze',900000,1100000,1280000),(3,'Elevate',1300000,1450000,1600000);
/*!40000 ALTER TABLE `honda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hyundai`
--

DROP TABLE IF EXISTS `hyundai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hyundai` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hyundai`
--

LOCK TABLES `hyundai` WRITE;
/*!40000 ALTER TABLE `hyundai` DISABLE KEYS */;
INSERT INTO `hyundai` VALUES (1,'Alcazar',2500000,2700000,2780000),(2,'Creta',1400000,1600000,1700000),(3,'Exter',800000,900000,1100000),(4,'Ioniq',2500000,2600000,2800000),(5,'Verna',1600000,1800000,2000000),(6,'Venue',1200000,1300000,1400000),(7,'Tcson',2500000,2700000,2900000),(8,'Aura',1000000,1100000,1150000),(9,'i10',900000,950000,1000000),(10,'i20',1200000,1300000,1500000);
/*!40000 ALTER TABLE `hyundai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kia`
--

DROP TABLE IF EXISTS `kia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kia` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kia`
--

LOCK TABLES `kia` WRITE;
/*!40000 ALTER TABLE `kia` DISABLE KEYS */;
INSERT INTO `kia` VALUES (1,'Carnival',2500000,2800000,3000000),(2,'Seltos',1400000,1600000,1700000),(3,'Sonet',1100000,1200000,1400000),(4,'Carens',1300000,1500000,1700000),(5,'EV 6',2000000,2500000,2900000),(6,'EV 9',3200000,3800000,4000000),(7,'Carens Clavis',1400000,1700000,2000000);
/*!40000 ALTER TABLE `kia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahindra`
--

DROP TABLE IF EXISTS `mahindra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahindra` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahindra`
--

LOCK TABLES `mahindra` WRITE;
/*!40000 ALTER TABLE `mahindra` DISABLE KEYS */;
INSERT INTO `mahindra` VALUES (1,'BE 6',2500000,2600000,2800000),(2,'XEV 9e',2300000,2400000,2700000),(3,'XUV 400',1400000,1450000,1500000),(4,'XUV 3XO',1000000,1200000,1300000),(5,'XUV 700',2000000,2200000,2400000),(6,'Bolero',1300000,1500000,1600000),(7,'Scorpio',2000000,2300000,2500000),(8,'Thar',1500000,1600000,1800000),(9,'Thar Roxx',1600000,1800000,2000000),(10,'Bolero neo',1400000,1600000,1800000),(11,'Scorpio N',2200000,2500000,2600000);
/*!40000 ALTER TABLE `mahindra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skoda`
--

DROP TABLE IF EXISTS `skoda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skoda` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skoda`
--

LOCK TABLES `skoda` WRITE;
/*!40000 ALTER TABLE `skoda` DISABLE KEYS */;
INSERT INTO `skoda` VALUES (1,'Kushaq',1100000,1200000,1400000),(2,'Slavia',1500000,1800000,2000000),(3,'Kodiaq',4500000,4800000,5200000),(4,'Kylaq',850000,970000,1100000);
/*!40000 ALTER TABLE `skoda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suzuki`
--

DROP TABLE IF EXISTS `suzuki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suzuki` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Prize3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `car_no_UNIQUE` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suzuki`
--

LOCK TABLES `suzuki` WRITE;
/*!40000 ALTER TABLE `suzuki` DISABLE KEYS */;
INSERT INTO `suzuki` VALUES (1,'Ignis',800000,870000,900000),(2,'Swift',700000,760000,800000),(3,'Dzire',600000,650000,700000),(4,'Fronx',950000,1000000,1150000),(5,'Brezza',1200000,1270000,1350000),(6,'Grand Vitara',1500000,1700000,2000000),(7,'Espresso',500000,550000,600000),(8,'Celerio',400000,450000,500000),(9,'Alto',350000,400000,470000),(10,'Baleno',850000,900000,1000000),(11,'Ertiga',1100000,1200000,1250000),(12,'XL6',1400000,1500000,1700000),(13,'Invicto',2200000,2400000,2600000),(14,'Eeco',500000,550000,580000),(15,'WagonR',540000,600000,650000),(16,'Jimny',1300000,1400000,1500000);
/*!40000 ALTER TABLE `suzuki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tata`
--

DROP TABLE IF EXISTS `tata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tata` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `car_no_UNIQUE` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tata`
--

LOCK TABLES `tata` WRITE;
/*!40000 ALTER TABLE `tata` DISABLE KEYS */;
INSERT INTO `tata` VALUES (1,'Nexon',1200000,1300000,1400000),(2,'Altroz',800000,850000,900000),(3,'Harrier',1500000,1700000,2000000),(4,'Safari',1700000,2000000,2300000),(5,'Punch',700000,800000,880000),(6,'Tiago',600000,650000,700000),(7,'Tigor',650000,700000,770000),(8,'Harrier.ev',1900000,2200000,2500000),(9,'Punch.ev',850000,900000,1000000),(10,'Nexon.ev',1400000,1600000,1700000),(11,'Tiago.ev',1100000,1200000,1260000),(12,'Tigor.ev',1000000,1050000,1100000),(13,'Cruvv.ev',1500000,1800000,2200000);
/*!40000 ALTER TABLE `tata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `toyota`
--

DROP TABLE IF EXISTS `toyota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `toyota` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toyota`
--

LOCK TABLES `toyota` WRITE;
/*!40000 ALTER TABLE `toyota` DISABLE KEYS */;
INSERT INTO `toyota` VALUES (1,'Urban Cruiser Hyryder',1400000,1600000,1900000),(2,'Innova Hycross',2200000,2500000,2800000),(3,'Fortuner',4000000,4500000,5000000),(4,'Fortuner Legender',5500000,5800000,6000000),(5,'Glanza',900000,1000000,1100000),(6,'Vellfire',12000000,15000000,18000000),(7,'Hilux',3000000,3500000,3700000),(8,'Innova Crysta',1900000,2300000,2700000),(9,'Land Cruiser',23000000,25000000,30000000);
/*!40000 ALTER TABLE `toyota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `phno` varchar(15) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `sec_phno` varchar(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`phno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('0','admin','admin','user',NULL,'0',NULL),('6282182971','asher123','Asher','Thomas Viju','Tharayil Pothara','8787654234','asherthomasv@gmail.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volkswagen`
--

DROP TABLE IF EXISTS `volkswagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volkswagen` (
  `Car_no` int NOT NULL,
  `Car` varchar(45) NOT NULL,
  `Price1` int DEFAULT NULL,
  `Price2` int DEFAULT NULL,
  `Price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`),
  UNIQUE KEY `Car_no` (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volkswagen`
--

LOCK TABLES `volkswagen` WRITE;
/*!40000 ALTER TABLE `volkswagen` DISABLE KEYS */;
INSERT INTO `volkswagen` VALUES (1,'Virtus',1500000,1700000,2000000),(2,'Taigun',1300000,1400000,1600000),(3,'Golf GTI',5300000,5500000,5600000),(4,'Tiguan',3500000,3800000,4000000);
/*!40000 ALTER TABLE `volkswagen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-02 16:43:20
