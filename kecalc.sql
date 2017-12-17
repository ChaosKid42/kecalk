--
-- Tabellenstruktur für Tabelle `menu`
--

CREATE TABLE `menu` (
  `me_id` int(11) NOT NULL,
  `me_date` date NOT NULL,
  `me_date_id` int(11) NOT NULL,
  `me_food` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `me_measure` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `me_amount` int(11) NOT NULL,
  `me_ke` double(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tabellenstruktur für Tabelle `params`
--

CREATE TABLE `params` (
  `pa_id` int(11) NOT NULL,
  `pa_name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pa_value` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


--
-- Indizes für die Tabelle `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`me_id`);

--
-- Indizes für die Tabelle `params`
--
ALTER TABLE `params`
  ADD PRIMARY KEY (`pa_id`);

--
-- AUTO_INCREMENT für Tabelle `menu`
--
ALTER TABLE `menu`
  MODIFY `me_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `params`
--
ALTER TABLE `params`
  MODIFY `pa_id` int(11) NOT NULL AUTO_INCREMENT;
