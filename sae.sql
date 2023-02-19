-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : dim. 19 fév. 2023 à 12:49
-- Version du serveur : 10.6.11-MariaDB-0ubuntu0.22.04.1
-- Version de PHP : 8.1.2-1ubuntu2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae`
--

-- --------------------------------------------------------

--
-- Structure de la table `arp`
--

CREATE TABLE `arp` (
  `ID` int(11) NOT NULL,
  `FileNumber` int(11) DEFAULT NULL,
  `FrameNumber` int(11) DEFAULT NULL,
  `FrameDate` double DEFAULT NULL,
  `Bench_3` int(11) DEFAULT NULL,
  `Bench_5` int(11) DEFAULT NULL,
  `FrameSize` int(11) DEFAULT NULL,
  `MAC_Dest` varchar(17) DEFAULT NULL,
  `MAC_Source` varchar(17) DEFAULT NULL,
  `Field_1` varchar(5) DEFAULT NULL,
  `Field_2` int(11) DEFAULT NULL,
  `Field_3` int(11) DEFAULT NULL,
  `Field_4` int(11) DEFAULT NULL,
  `Field_5` int(11) DEFAULT NULL,
  `Field_6` int(11) DEFAULT NULL,
  `MAC_Sender` text DEFAULT NULL,
  `IP_Sender` varchar(15) DEFAULT NULL,
  `MAC_Target` varchar(17) DEFAULT NULL,
  `IP_Target` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `frames`
--

CREATE TABLE `frames` (
  `ID` int(11) NOT NULL,
  `FileNumber` int(11) NOT NULL,
  `FrameNumber` int(11) NOT NULL,
  `Size` int(11) NOT NULL,
  `Type` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `arp`
--
ALTER TABLE `arp`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `frames`
--
ALTER TABLE `frames`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `arp`
--
ALTER TABLE `arp`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `frames`
--
ALTER TABLE `frames`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
