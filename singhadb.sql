-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 22, 2024 at 02:02 PM
-- Server version: 8.0.35-0ubuntu0.22.04.1
-- PHP Version: 8.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `singhadb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `userID` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`userID`, `password`) VALUES
('admin', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `arena_db`
--

CREATE TABLE `arena_db` (
  `idarena` int NOT NULL,
  `competName` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `arenaName` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `pending` varchar(20) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `arena_db`
--

INSERT INTO `arena_db` (`idarena`, `competName`, `arenaName`, `image`, `pending`) VALUES
(1, 'tester', 'สนาม Kick Off Arena CMI', 'https://drive.google.com/thumbnail?id=1T6XjB6Rmn-vG6F4jiaUIoCxPgjw795zi', 'รอการอนุมัติ');

-- --------------------------------------------------------

--
-- Table structure for table `player_db`
--

CREATE TABLE `player_db` (
  `nameTeam` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `namePlayer` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `datePlayer` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `phonePlayer` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `namePlayer2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `datePlayer2` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `phonePlayer2` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `namePlayer3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `datePlayer3` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `phonePlayer3` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `namePlayer4` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `datePlayer4` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `phonePlayer4` varchar(20) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `player_db`
--

INSERT INTO `player_db` (`nameTeam`, `namePlayer`, `datePlayer`, `phonePlayer`, `namePlayer2`, `datePlayer2`, `phonePlayer2`, `namePlayer3`, `datePlayer3`, `phonePlayer3`, `namePlayer4`, `datePlayer4`, `phonePlayer4`) VALUES
('JJKA', 'MINA', '2020-05-13', '0855453651', 'DREAMM', '2020-06-11', '0856501566', 'ศักรินน์ ศีวิทานนท์', '2024-01-20', '0522142325', 'ชัชดนัย', '2024-01-21', '0854632465'),
('มีน', 'นภัสสรรรร รรร', '2013-01-09', '0983031004', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `result_db`
--

CREATE TABLE `result_db` (
  `idresult` int NOT NULL,
  `idarena` int NOT NULL,
  `arenaName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `pending` varchar(30) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `result_db`
--

INSERT INTO `result_db` (`idresult`, `idarena`, `arenaName`, `image`, `pending`) VALUES
(1, 1, 'tester', 'https://drive.google.com/thumbnail?id=15qgqW4N8aCAwPrh2StwBo5nXUS_vf81k', 'รอการอนุมัติ');

-- --------------------------------------------------------

--
-- Table structure for table `team_db`
--

CREATE TABLE `team_db` (
  `nameTeam` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `nameArena` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `nameCoach` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `idline` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `pending` varchar(20) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `team_db`
--

INSERT INTO `team_db` (`nameTeam`, `nameArena`, `nameCoach`, `phone`, `email`, `idline`, `image`, `pending`) VALUES
('JJKA', 'สนาม Sport Arena', 'Chisanupong Limsakul', '0989904873', 'zvcx1236@gmail.com', 'DRED', 'https://drive.google.com/thumbnail?id=1dX3JhDKK91U-pZ30UnjMwimB4noJ6_RY', 'ไม่อนุมัติ'),
('มีน', 'สนาม Kick Off Arena CMI', 'นภัสสร รุ่ง', '0983031004', 'nnoey.npsw@gmail.com', 'Noeynpsw', 'https://drive.google.com/thumbnail?id=1xuHPMH5AAa6NCgKgvQVIf25zRpmQ5MkZ', 'รอดำเนินการ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arena_db`
--
ALTER TABLE `arena_db`
  ADD PRIMARY KEY (`idarena`);

--
-- Indexes for table `player_db`
--
ALTER TABLE `player_db`
  ADD PRIMARY KEY (`nameTeam`);

--
-- Indexes for table `result_db`
--
ALTER TABLE `result_db`
  ADD PRIMARY KEY (`idresult`);

--
-- Indexes for table `team_db`
--
ALTER TABLE `team_db`
  ADD PRIMARY KEY (`nameTeam`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arena_db`
--
ALTER TABLE `arena_db`
  MODIFY `idarena` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `result_db`
--
ALTER TABLE `result_db`
  MODIFY `idresult` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
