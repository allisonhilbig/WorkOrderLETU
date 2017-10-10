-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 09, 2017 at 10:12 PM
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
  `idPreference` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `userEmail` varchar(45) NOT NULL,
  `raEmail` varchar(45) NOT NULL,
  `rdEmail` varchar(45) NOT NULL,
  `resHall` varchar(45) NOT NULL,
  `floorNumber` varchar(4) DEFAULT NULL,
  `roomNumber` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`idPreference`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Preference`
--

INSERT INTO `Preference` (`idPreference`, `name`, `userEmail`, `raEmail`, `rdEmail`, `resHall`, `floorNumber`, `roomNumber`) VALUES
(1, 'annjones', 'annjones@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'apt', '16C', 'A'),
(2, 'erinprimrose', 'erinprimrose@letu.edu', 'maria@letu.edu', 'ben@letu.edu', 'apt', '15C', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `Status`
--

CREATE TABLE IF NOT EXISTS `Status` (
  `idStatus` int(11) NOT NULL,
  `workOrderID` int(11) DEFAULT NULL,
  `submissionDate` timestamp NULL DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idStatus`),
  KEY `workOrderID_idx` (`workOrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Status`
--

INSERT INTO `Status` (`idStatus`, `workOrderID`, `submissionDate`, `status`) VALUES
(1, 1, '2017-09-15 05:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Work Order`
--

CREATE TABLE IF NOT EXISTS `Work Order` (
  `idWork Order` int(11) NOT NULL,
  `Building` varchar(45) DEFAULT NULL,
  `Coordinates` varchar(45) DEFAULT NULL,
  `Description` text,
  `name` varchar(45) DEFAULT NULL,
  `preferencesID` varchar(45) DEFAULT NULL,
  `raEmail` varchar(45) DEFAULT NULL,
  `rdEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idWork Order`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Work Order`
--

INSERT INTO `Work Order` (`idWork Order`, `Building`, `Coordinates`, `Description`, `name`, `preferencesID`, `raEmail`, `rdEmail`) VALUES
(1, 'Apt', 'SW corner', 'work order 1 testing, auto fill in GUi, but not database cuz foreign keys...', 'annjones', '1', 'maria@letu.edu', 'ben@letu.edu');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Status`
--
ALTER TABLE `Status`
  ADD CONSTRAINT `workOrderID` FOREIGN KEY (`workOrderID`) REFERENCES `Work Order` (`idWork Order`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Work Order`
--
ALTER TABLE `Work Order`
  ADD CONSTRAINT `preferencesID` FOREIGN KEY (`idWork Order`) REFERENCES `Preference` (`idPreference`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
