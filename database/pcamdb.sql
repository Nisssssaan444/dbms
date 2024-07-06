

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";




USE pulchowkcampus;

-- --------------------------------------------------------

--



-- --------------------------------------------------------

--
-- Table structure for table `employee_table`
--

DROP TABLE IF EXISTS `employee_table`;
CREATE TABLE `employee_table` (
  `id` char(5) DEFAULT NULL,
  `name` char(30) NOT NULL,
  `designation` char(30) NOT NULL,
  `dept` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE employee_table ADD designation char(30) NOT NULL AFTER name;


-- --------------------------------------------------------

--
-- Table structure for table `global_values`
--

DROP TABLE IF EXISTS `global_values`;
CREATE TABLE `global_values` (
  `x` char(10) NOT NULL,
  `y` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `global_values`
--

INSERT INTO `global_values` (`x`, `y`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `notice_board`
--

DROP TABLE IF EXISTS `notice_board`;
CREATE TABLE `notice_board` (
  `id` char(5) NOT NULL,
  `topic` char(20) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student_table`
--

DROP TABLE IF EXISTS `student_table`;
CREATE TABLE `student_table` (
  `id` char(5) DEFAULT NULL,
  `name` char(30) NOT NULL,
  `sem` int(11) NOT NULL,
  `stream` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--

--
-- Indexes for table `company_list`
--

--
-- Indexes for table `employee_table`
--
ALTER TABLE `employee_table`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `global_values`
--
ALTER TABLE `global_values`
  ADD UNIQUE KEY `x` (`x`);

--
-- Indexes for table `notice_board`
--
ALTER TABLE `notice_board`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `student_table`
--
ALTER TABLE `student_table`
  ADD UNIQUE KEY `id` (`id`);
COMMIT;
