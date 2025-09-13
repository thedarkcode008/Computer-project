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
INSERT INTO `car_purchase` VALUES (1,'6282182971','Slavia','Blue','Top','EMI',2000000),(2,'6282182971','XUV 700','Black','Top','Net Banking',2400000),(3,'6282182971','Swift','Red','Mid','Net Banking',760000),(5,'9400627033','i20','Black','Top','Net Banking',1500000),(6,'6282182971','Jimny','Blue','Mid','Debit Card',1400000),(7,'6282182971','Brezza','Black','Mid','Net Banking',1270000),(8,'6282182971','Virtus','Black','Top','Net Banking',2000000),(9,'8237481938','Thar','White','Top','Credit Card',1800000);
/*!40000 ALTER TABLE `car_purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_service`
--

DROP TABLE IF EXISTS `car_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_service` (
  `service_id` int NOT NULL,
  `phno` varchar(15) DEFAULT NULL,
  `car_name` varchar(45) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `service_type` varchar(45) DEFAULT NULL,
  `problem` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`service_id`),
  UNIQUE KEY `service_id_UNIQUE` (`service_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_service`
--

LOCK TABLES `car_service` WRITE;
/*!40000 ALTER TABLE `car_service` DISABLE KEYS */;
INSERT INTO `car_service` VALUES (1,'6282182971','Thar','Mahindra','Full Service','Need full service','2025-08-14'),(2,'6282182971','Thar','Mahindra','Other','4 wheel drive not working','2025-08-15'),(3,'6282182971','Swift','Suzuki','Brake Check','Brake not working','2025-08-10');
/*!40000 ALTER TABLE `car_service` ENABLE KEYS */;
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
INSERT INTO `car_test` VALUES (1,'6282182971','i20','hyundai','11:00','2025-08-13'),(3,'6282182971','Slavia','skoda','10:00','2025-08-06'),(4,'8237481938','Eeco','Suzuki','12:00','2058-09-12');
/*!40000 ALTER TABLE `car_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `Car_no` int NOT NULL,
  `company` varchar(50) DEFAULT NULL,
  `car` varchar(45) NOT NULL,
  `price1` int DEFAULT NULL,
  `price2` int DEFAULT NULL,
  `price3` int DEFAULT NULL,
  PRIMARY KEY (`Car_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,'Citroen','C3',800000,900000,1000000),(2,'Citroen','C5',1200000,1250000,1370000),(3,'Citroen','Aircross',1100000,1200000,1250000),(4,'Citroen','Basalt',1000000,1100000,1200000),(5,'Citroen','eC3',1000000,1100000,1200000),(6,'Honda','City',1500000,1700000,2000000),(7,'Honda','Amaze',900000,1100000,1280000),(8,'Honda','Elevate',1300000,1450000,1600000),(9,'Hyundai','Alcazar',2500000,2700000,2780000),(10,'Hyundai','Creta',1400000,1600000,1700000),(11,'Hyundai','Exter',800000,900000,1100000),(12,'Hyundai','Ioniq',2500000,2600000,2800000),(13,'Hyundai','Verna',1600000,1800000,2000000),(14,'Hyundai','Venue',1200000,1300000,1400000),(15,'Hyundai','Tcson',2500000,2700000,2900000),(16,'Hyundai','Aura',1000000,1100000,1150000),(17,'Hyundai','i10',900000,950000,1000000),(18,'Hyundai','i20',1200000,1300000,1500000),(19,'Kia','Carnival',2500000,2800000,3000000),(20,'Kia','Seltos',1400000,1600000,1700000),(21,'Kia','Sonet',1100000,1200000,1400000),(22,'Kia','Carens',1300000,1500000,1700000),(23,'Kia','EV 6',2000000,2500000,2900000),(24,'Kia','EV 9',3200000,3800000,4000000),(25,'Kia','Carens Clavis',1400000,1700000,2000000),(26,'Mahindra','BE 6',2500000,2600000,2800000),(27,'Mahindra','XEV 9e',2300000,2400000,2700000),(28,'Mahindra','XUV 400',1400000,1450000,1500000),(29,'Mahindra','XUV 3XO',1000000,1200000,1300000),(30,'Mahindra','XUV 700',2000000,2200000,2400000),(31,'Mahindra','Bolero',1300000,1500000,1600000),(32,'Mahindra','Scorpio',2000000,2300000,2500000),(33,'Mahindra','Thar',1500000,1600000,1800000),(34,'Mahindra','Thar Roxx',1600000,1800000,2000000),(35,'Mahindra','Bolero neo',1400000,1600000,1800000),(36,'Mahindra','Scorpio N',2100000,2300000,2800000),(37,'Skoda','Kushaq',1100000,1200000,1400000),(38,'Skoda','Slavia',1500000,1800000,2000000),(39,'Skoda','Kodiaq',4500000,4800000,5200000),(40,'Skoda','Kylaq',850000,970000,1100000),(41,'Suzuki','Ignis',800000,870000,900000),(42,'Suzuki','Swift',700000,760000,800000),(43,'Suzuki','Dzire',600000,650000,700000),(44,'Suzuki','Fronx',950000,1000000,1150000),(45,'Suzuki','Brezza',1200000,1270000,1350000),(46,'Suzuki','Grand Vitara',1500000,1700000,2000000),(47,'Suzuki','Espresso',500000,550000,600000),(48,'Suzuki','Celerio',400000,450000,500000),(49,'Suzuki','Alto',350000,400000,470000),(50,'Suzuki','Baleno',850000,900000,1000000),(51,'Suzuki','Ertiga',1100000,1200000,1250000),(52,'Suzuki','XL6',1400000,1500000,1700000),(53,'Suzuki','Invicto',2200000,2400000,2600000),(54,'Suzuki','WagonR',540000,600000,650000),(55,'Suzuki','Jimny',1350000,1400000,1500000),(57,'Tata','Nexon',1200000,1300000,1400000),(58,'Tata','Altroz',800000,850000,900000),(59,'Tata','Harrier',1500000,1700000,2000000),(60,'Tata','Safari',1700000,2000000,2300000),(61,'Tata','Punch',700000,800000,880000),(62,'Tata','Tiago',600000,650000,700000),(63,'Tata','Tigor',650000,700000,770000),(64,'Tata','Harrier.ev',1900000,2200000,2500000),(65,'Tata','Punch.ev',850000,900000,1000000),(66,'Tata','Nexon.ev',1400000,1600000,1700000),(67,'Tata','Tiago.ev',1100000,1200000,1260000),(68,'Tata','Tigor.ev',1000000,1050000,1100000),(70,'Toyota','Urban Cruiser Hyryder',1400000,1600000,1900000),(71,'Toyota','Innova Hycross',2200000,2500000,2800000),(72,'Toyota','Fortuner',4000000,4500000,5000000),(73,'Toyota','Fortuner Legender',5500000,5800000,6000000),(74,'Toyota','Glanza',900000,1000000,1100000),(75,'Toyota','Vellfire',12000000,15000000,18000000),(76,'Toyota','Hilux',3000000,3500000,3700000),(77,'Toyota','Innova Crysta',1900000,2300000,2700000),(78,'Toyota','Land Cruiser',23000000,25000000,30000000),(79,'Volkswagen','Virtus',1500000,1700000,2000000),(80,'Volkswagen','Taigun',1300000,1400000,1600000),(81,'Volkswagen','Golf GTI',5300000,5500000,5600000),(82,'Volkswagen','Tiguan',3500000,3800000,4000000),(83,'Suzuki','Eeco',500000,540000,600000),(84,'Tata','Curvv.ev',1500000,1800000,2200000);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
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
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`phno`,`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('0','admin','admin','user',NULL,'0','admin@gmail.com'),('6282182971','asher123','Asher','Thomas Viju','Tharayil Pothara','8787654234','asherthomasv@gmail.com'),('8237481938','Joel123','Joel ','Kuttan','My House - arinjitt enthina?','9782348395','joelthomastiju@gmail.com'),('9400627033','vaishnav123','Vaishnav','Prasad','112 Bakar street','9430626900','vaishnavprasad@gmail.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-14  0:02:45
