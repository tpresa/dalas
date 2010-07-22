-- MySQL dump 10.11
-- Server version       5.0.51a-24+lenny2
--
-- Current Database: `Log`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `Log` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `Log`;

CREATE TABLE `RawLog` (
  `id` bigint(20) NOT NULL auto_increment,
  `date_now` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `rawdata` varchar(512) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='RawLog is a full text';

CREATE TABLE `GenericLog` (
  `id` bigint(20) NOT NULL auto_increment,
  `date_now` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `date_syslog` varchar(32) NOT NULL,
  `hostname` varchar(64) NOT NULL,
  `process` varchar(64) NOT NULL,
  `data` varchar(512) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='GenericLog data';

CREATE TABLE `PostfixLog` (
  `id` bigint(20) NOT NULL auto_increment,
  `date_now` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `date_syslog` varchar(32) NOT NULL,
  `hostname` varchar(64) NOT NULL,
  `process` varchar(64) NOT NULL,
  `queue_id` varchar(20) NOT NULL,
  `subject` varchar(256) NOT NULL,
  `mail_from` varchar(128) NOT NULL,
  `rcpts` varchar(2048) NOT NULL,
  `helo` varchar(64) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Postfix Log';

CREATE TABLE `PostfixLog` (
  `id` bigint(20) NOT NULL auto_increment,
  `date_now` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `date_syslog` varchar(32) NOT NULL,
  `hostname` varchar(64) NOT NULL,
  `process` varchar(64) NOT NULL,
  `queue_id` varchar(20) NOT NULL,
  `subject` varchar(256) NOT NULL,
  `client_ip_hostname` varchar(64) NOT NULL,
  `client_ip` varchar(15) NOT NULL,
  `mail_from` varchar(128) NOT NULL,
  `rcpts` varchar(2048) NOT NULL,
  `helo` varchar(64) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Postfix Log';

CREATE TABLE  `IptablesLog` (
  `id` bigint(20) NOT NULL auto_increment,
  `date_now` timestamp NOT NULL,
  `date_syslog` varchar(32) NOT NULL,
  `hostname` varchar(64) NOT NULL,
  `rule_comment` varchar(64) default NULL,
  `input_interface` varchar(16) default NULL,
  `output_interface` varchar(16) default NULL,
  `eth_mac_source` varchar(17) default NULL,
  `eth_mac_destination` varchar(17) default NULL,
  `eth_frame_type` varchar(5) default NULL,
  `ip_source` varchar(15) NOT NULL,
  `ip_destination` varchar(15) NOT NULL,
  `ip_lenght` varchar(5) NOT NULL,
  `ip_type_of_service` varchar(4) NOT NULL,
  `ip_precedence` varchar(4) NOT NULL,
  `ip_time_to_live` varchar(3) NOT NULL,
  `ip_id` varchar(5) NOT NULL,
  `ip_flag_ce` tinyint(1) default NULL,
  `ip_flag_df` tinyint(1) default NULL,
  `ip_flag_mf` tinyint(1) default NULL,
  `ip_fragment_offset` varchar(4) default NULL,
  `ip_options` varchar(80) default NULL,
  `ip_protocol` varchar(10) default NULL,
  `tcp_udp_sport` varchar(5) default NULL,
  `tcp_udp_dport` varchar(5) default NULL,
  `tcp_sequence_number` varchar(10) default NULL,
  `tcp_acknowledgement` varchar(10) default NULL,
  `tcp_window` varchar(10) default NULL,
  `tcp_reserved` varchar(4) default NULL,
  `tcp_flag_cwr` tinyint(1) default NULL,
  `tcp_flag_ece` tinyint(1) default NULL,
  `tcp_flag_urg` tinyint(1) default NULL,
  `tcp_flag_ack` tinyint(1) default NULL,
  `tcp_flag_psh` tinyint(1) default NULL,
  `tcp_flag_rst` tinyint(1) default NULL,
  `tcp_flag_syn` tinyint(1) default NULL,
  `tcp_flag_fin` tinyint(1) default NULL,
  `tcp_urgent_pointer` varchar(10) default NULL,
  `tcp_options` varchar(80) default NULL,
  `udp_lenght` varchar(10) default NULL,
  `icmp_type` varchar(2) default NULL,
  `icmp_code` varchar(2) default NULL,
  `icmp_id` varchar(5) default NULL,
  `icmp_seq` varchar(5) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Iptables Log Fields'

