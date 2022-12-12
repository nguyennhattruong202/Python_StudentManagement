CREATE DATABASE  IF NOT EXISTS `quanlyhocsinh` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `quanlyhocsinh`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: quanlyhocsinh
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `class_room`
--

DROP TABLE IF EXISTS `class_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `max_quantity` int NOT NULL,
  `grade_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grade_id` (`grade_id`),
  CONSTRAINT `class_room_ibfk_1` FOREIGN KEY (`grade_id`) REFERENCES `grade` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_room`
--

LOCK TABLES `class_room` WRITE;
/*!40000 ALTER TABLE `class_room` DISABLE KEYS */;
INSERT INTO `class_room` VALUES (25,'10A1',40,1),(26,'10A2',40,1),(27,'10A3',40,1),(28,'10A4',40,1),(29,'10A5',40,1),(30,'10A6',40,1),(31,'10A7',40,1),(32,'10A8',40,1),(33,'10A9',40,1),(34,'11B1',40,2),(35,'11B2',40,2),(36,'11B3',40,2),(37,'11B4',40,2),(38,'11B5',40,2),(39,'11B6',40,2),(40,'11B7',40,2),(41,'11B8',40,2),(42,'12C1',40,3),(43,'12C2',40,3),(44,'12C3',40,3),(45,'12C4',40,3),(46,'12C5',40,3),(47,'12C6',40,3),(48,'12C7',40,3);
/*!40000 ALTER TABLE `class_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES (1,'Khối 10'),(2,'Khối 11'),(3,'Khối 12');
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `score` (
  `id` int NOT NULL AUTO_INCREMENT,
  `score` float DEFAULT NULL,
  `student_id` int NOT NULL,
  `score_type_id` int NOT NULL,
  `semester_id` int NOT NULL,
  `subject_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  KEY `score_type_id` (`score_type_id`),
  KEY `semester_id` (`semester_id`),
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `score_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `score_ibfk_2` FOREIGN KEY (`score_type_id`) REFERENCES `score_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `score_ibfk_3` FOREIGN KEY (`semester_id`) REFERENCES `semester` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `score_ibfk_4` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score_type`
--

DROP TABLE IF EXISTS `score_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `score_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score_type`
--

LOCK TABLES `score_type` WRITE;
/*!40000 ALTER TABLE `score_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `score_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semester`
--

DROP TABLE IF EXISTS `semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semester` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `note` text COLLATE utf8mb4_unicode_520_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semester`
--

LOCK TABLES `semester` WRITE;
/*!40000 ALTER TABLE `semester` DISABLE KEYS */;
INSERT INTO `semester` VALUES (1,'HK I 2022-2023',NULL),(2,'HK II 2022 - 2023',NULL);
/*!40000 ALTER TABLE `semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `gender` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `birthday` date DEFAULT NULL,
  `phone` varchar(50) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `class_room_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_room_id` (`class_room_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_room_id`) REFERENCES `class_room` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Paul Mack','Male','2005-02-07','0344286589','paul@gmail.com',NULL),(2,'Sarah Phillips','Female','2005-06-05','0915645611','saral@gmail.com',NULL),(3,'Tina Flores','Female','2005-05-04','0347583858','tina@gmail.com',NULL),(4,'Michael Jacobs','Male','2005-11-24','0923728738','michael@gmail.com',NULL),(5,'Victor Peterson','Female','2005-10-06','0358768379','victor@gmail.com',NULL),(6,'Deborah Brown','Female','2006-07-05',NULL,NULL,NULL),(7,'Mary Scott','Female','2006-08-09',NULL,NULL,NULL),(8,'Megan Fernandez','Female','2006-09-23',NULL,NULL,NULL),(9,'Paul Gutierrez','Male','2006-05-29',NULL,NULL,NULL),(10,'Jennifer Martinez','Female','2006-04-14',NULL,NULL,NULL),(11,'Shirley Yates','Female','2007-12-04',NULL,NULL,NULL),(12,'Donna Velazquez','Female','2007-11-05',NULL,NULL,NULL),(13,'James Mccann','Male','2007-02-23',NULL,NULL,NULL),(14,'David Brewer','Male','2007-03-28',NULL,NULL,NULL),(15,'Rhonda Waters','Female','2007-02-23',NULL,NULL,NULL),(16,'Kristin Turner','Female','2005-05-26',NULL,NULL,NULL),(17,'Richard Hill','Male','2005-04-25',NULL,NULL,NULL),(18,'Donald Wilkinson','Male','2005-07-27',NULL,NULL,NULL),(19,'Steve Freeman','Male','2005-01-24',NULL,NULL,NULL),(20,'Shelly Davis','Female','2006-12-05',NULL,NULL,NULL),(21,'Richard Miller','Male','2006-06-21',NULL,NULL,NULL),(22,'Lori Peters','Male','2006-02-20',NULL,NULL,NULL),(23,'James Butler','Male','2007-08-12',NULL,NULL,NULL),(24,'Adam Lewis','Male','2007-04-23',NULL,NULL,NULL),(25,'Mariah Cole','Female','2005-05-05',NULL,NULL,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'Toán'),(2,'Văn '),(3,'Anh '),(4,'GDCD'),(5,'Sử'),(6,'Địa'),(7,'Sinh'),(8,'Lý'),(9,'Hóa'),(10,'Công Nghệ');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teach_detail`
--

DROP TABLE IF EXISTS `teach_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teach_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `startDate` date DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `subject_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `teach_detail_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `teach_detail_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teach_detail`
--

LOCK TABLES `teach_detail` WRITE;
/*!40000 ALTER TABLE `teach_detail` DISABLE KEYS */;
INSERT INTO `teach_detail` VALUES (1,'2022-12-08',1,3);
/*!40000 ALTER TABLE `teach_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `gender` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `birthday` date DEFAULT NULL,
  `phone` varchar(50) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `identity` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `degree` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `position` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `username` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `user_role` enum('ADMIN','TEACHER','EMPLOYEE') COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Hoàng Công Minh','Nam','2001-07-25','0909291469','1951012069minh@ou.edu.vn','097201000060','Thạc sĩ','Giáo viên','congminh','e10adc3949ba59abbe56e057f20f883e','TEACHER'),(2,'Nguyễn Duy Hải Anh','Nam','2001-04-05','0941996309','1951052009anh@ou.edu.vn','097201006660',NULL,'Admin','haianh','e10adc3949ba59abbe56e057f20f883e','ADMIN'),(3,'Nguyễn Nhật Trường','Nam','2001-02-20','0865789234','1951012146truong@ou.edu.vn','073301005567',NULL,'Nhân viên','nhattruong','e10adc3949ba59abbe56e057f20f883e','EMPLOYEE');
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

-- Dump completed on 2022-12-12 18:14:39
