-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2024 at 09:54 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `singha_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `userID` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
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
  `idarena` int(11) NOT NULL,
  `competName` varchar(100) NOT NULL,
  `arenaName` varchar(100) NOT NULL,
  `image` varchar(255) NOT NULL,
  `pending` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `player_db`
--

CREATE TABLE `player_db` (
  `idteam` int(11) NOT NULL,
  `namePlayer` varchar(255) NOT NULL,
  `datePlayer` varchar(20) NOT NULL,
  `phonePlayer` varchar(20) NOT NULL,
  `namePlayer2` varchar(255) NOT NULL,
  `datePlayer2` varchar(20) NOT NULL,
  `phonePlayer2` varchar(20) NOT NULL,
  `namePlayer3` varchar(255) NOT NULL,
  `datePlayer3` varchar(20) NOT NULL,
  `phonePlayer3` varchar(20) NOT NULL,
  `namePlayer4` varchar(255) NOT NULL,
  `datePlayer4` varchar(20) NOT NULL,
  `phonePlayer4` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `result_db`
--

CREATE TABLE `result_db` (
  `idresult` int(11) NOT NULL,
  `idarena` int(11) NOT NULL,
  `arenaName` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `pending` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_db`
--

CREATE TABLE `team_db` (
  `idteam` int(11) NOT NULL,
  `nameTeam` varchar(100) NOT NULL,
  `nameArena` varchar(100) NOT NULL,
  `nameCoach` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `idline` varchar(255) NOT NULL,
  `image` varchar(200) NOT NULL,
  `pending` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  ADD PRIMARY KEY (`idteam`);

--
-- Indexes for table `result_db`
--
ALTER TABLE `result_db`
  ADD PRIMARY KEY (`idresult`);

--
-- Indexes for table `team_db`
--
ALTER TABLE `team_db`
  ADD PRIMARY KEY (`idteam`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arena_db`
--
ALTER TABLE `arena_db`
  MODIFY `idarena` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `result_db`
--
ALTER TABLE `result_db`
  MODIFY `idresult` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `team_db`
--
ALTER TABLE `team_db`
  MODIFY `idteam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
