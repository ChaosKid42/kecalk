--
-- Tabellenstruktur für Tabelle `menu`
--

CREATE TABLE `menu` (
  `me_id` int(11) NOT NULL,
  `me_date` date NOT NULL,
  `me_date_id` int(11) NOT NULL,
  `me_food` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `me_measure` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `me_amount` int(11) NOT NULL,
  `me_ke` double(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indizes für die Tabelle `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`me_id`);

--
-- AUTO_INCREMENT für Tabelle `menu`
--
ALTER TABLE `menu`
  MODIFY `me_id` int(11) NOT NULL AUTO_INCREMENT;
