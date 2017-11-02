-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 01, 2017 at 10:11 PM
-- Server version: 5.5.57-0ubuntu0.14.04.1-log
-- PHP Version: 5.5.9-1ubuntu4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sw2projdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `Preference`
--

CREATE TABLE IF NOT EXISTS `Preference` (
  `idPreference` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `userEmail` varchar(45) NOT NULL,
  `raEmail` varchar(45) NOT NULL,
  `rdEmail` varchar(45) NOT NULL,
  `resHall` varchar(45) NOT NULL,
  `floorNumber` varchar(4) DEFAULT NULL,
  `roomNumber` varchar(4) DEFAULT NULL,
  `password` varchar(25) NOT NULL,
  PRIMARY KEY (`idPreference`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `Preference`
--

INSERT INTO `Preference` (`idPreference`, `name`, `userEmail`, `raEmail`, `rdEmail`, `resHall`, `floorNumber`, `roomNumber`, `password`) VALUES
(1, 'annjones', 'annjones@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'apt', '16C', 'A', 'password'),
(2, 'erinprimrose', 'erinprimrose@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'apt', '15C', 'A', 'password'),
(3, 'asdf', 'a@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '1', '115', 'password'),
(4, 'sdf', 'b@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '1', '114', 'password'),
(5, 'df', 'c@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '1', '113', 'password'),
(6, 'ff', 'd@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '1', '112', 'password'),
(7, 'qwer', 'e@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '1', '111', 'password'),
(8, 'wer', 'j@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'thom', '2', '110', 'password'),
(9, 'er', 'i@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'apt', '16C', 'B', 'password');

-- --------------------------------------------------------

--
-- Table structure for table `Status`
--

CREATE TABLE IF NOT EXISTS `Status` (
  `idStatus` int(11) NOT NULL AUTO_INCREMENT,
  `workOrderID` int(11) NOT NULL,
  `submissionDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idStatus`),
  KEY `workOrderID_idx` (`workOrderID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `Status`
--

INSERT INTO `Status` (`idStatus`, `workOrderID`, `submissionDate`, `status`) VALUES
(1, 1, '2017-09-15 10:00:00', 0),
(11, 1, '2017-11-02 02:57:56', 0),
(12, 2, '2017-11-02 02:57:56', 0),
(13, 3, '2017-11-02 02:57:56', 0),
(14, 4, '2017-11-02 02:57:56', 0),
(15, 5, '2017-11-02 02:57:56', 0),
(16, 6, '2017-11-02 02:57:56', 0),
(17, 7, '2017-11-02 02:57:56', 0),
(18, 8, '2017-11-02 02:57:56', 0);

-- --------------------------------------------------------

--
-- Table structure for table `workOrder`
--

CREATE TABLE IF NOT EXISTS `workOrder` (
  `idWorkOrder` int(11) NOT NULL AUTO_INCREMENT,
  `building` varchar(45) DEFAULT NULL,
  `coordinates` varchar(45) DEFAULT NULL,
  `description` text,
  `name` varchar(45) DEFAULT NULL,
  `preferencesID` varchar(45) DEFAULT NULL,
  `raEmail` varchar(45) DEFAULT NULL,
  `rdEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idWorkOrder`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `workOrder`
--

INSERT INTO `workOrder` (`idWorkOrder`, `building`, `coordinates`, `description`, `name`, `preferencesID`, `raEmail`, `rdEmail`) VALUES
(1, 'Apt', 'SW corner', 'work order 1 testing, auto fill in GUi, but not database cuz foreign keys...', 'annjones', '1', 'maria@letu.edu', 'ben@letu.edu'),
(2, 'apt', 'SW', 'yassssss', 'a', '1', 'maria@letu.edu', 'ben@letu.edu'),
(3, 'apt', 'SW', 'yassssss', 'a', '2', 'maria@letu.edu', 'ben@letu.edu'),
(4, 'apt', 'SW', 'yassssss', 'a', '3', 'maria@letu.edu', 'ben@letu.edu'),
(5, 'apt', 'SW', 'yassssss', 'a', '4', 'maria@letu.edu', 'ben@letu.edu'),
(6, 'apt', 'SW', 'yassssss', 'a', '5', 'maria@letu.edu', 'ben@letu.edu'),
(7, 'apt', 'SW', 'yassssss', 'a', '6', 'maria@letu.edu', 'ben@letu.edu'),
(8, 'apt', 'SW', 'yassssss', 'a', '7', 'maria@letu.edu', 'ben@letu.edu');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Status`
--
ALTER TABLE `Status`
  ADD CONSTRAINT `workOrderID` FOREIGN KEY (`workOrderID`) REFERENCES `workOrder` (`idWorkOrder`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `workOrder`
--
ALTER TABLE `workOrder`
  ADD CONSTRAINT `preferencesID` FOREIGN KEY (`idWorkOrder`) REFERENCES `Preference` (`idPreference`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
