# -*- coding: utf-8 -*-
# libIptablesLog plugin from logPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import re
from libTemplate import TemplateLog

class IptablesLog(TemplateLog):
	re_iptablesLog = re.compile(r"^(?P<date>[A-Za-z]{3} \d{1,2} {1,2}\d\d:\d\d:\d\d) (?P<hostname>.+?) kernel: (\[\d+\.\d+\] )?(?P<comment>.*?)IN=(?P<input_interface>.*?) OUT=(?P<output_interface>.*?) (MAC=(?P<mac>.*?) )?SRC=(?P<ip_source>.*?) DST=(?P<ip_destination>.*?) LEN=(?P<ip_lenght>.*?) TOS=(?P<ip_type_of_service>.*?) PREC=(?P<ip_precedence>.*?) TTL=(?P<ip_time_to_live>.*?) ID=(?P<ip_id>\d+) ((?P<ip_flag_df>DF) )?PROTO=(?P<ip_protocol>.*?) (?P<proto_data>.*)$")
	re_iptablesTcp = re.compile(r"SPT=(?P<tcp_udp_sport>.*?) DPT=(?P<tcp_udp_dport>.*?) WINDOW=(?P<tcp_window>.*?) RES=(?P<tcp_reserved>.*?) ((?P<tcp_flag_cwr>CWR?) )?((?P<tcp_flag_ece>ECE?) )?((?P<tcp_flag_urg>URG?) )?((?P<tcp_flag_ack>ACK?) )?((?P<tcp_flag_psh>PSH?) )?((?P<tcp_flag_rst>RST?) )?((?P<tcp_flag_syn>SYN?) )?((?P<tcp_flag_fin>FIN?) )?URGP=(?P<tcp_urgent_pointer>.*?)$")
	re_iptablesUdp = re.compile(r"LEN=(?P<udp_lenght>.*?)$")
	re_iptablesIcmp = re.compile(r"TYPE=(?P<icmp_type>.*?) CODE=(?P<icmp_code>.*?) ID=(?P<icmp_id>.*?) SEQ=(?P<icmp_seq>.*?)$")

	def __init__(self):
		pass
	
	def __del__(self):
		pass

	def insert(self, dbHandle, data):
		try:
			match = IptablesLog.re_iptablesLog.match(data)
			result = self._match2dict(match)
			if result.get('ip_protocol') == 'TCP':
				match = IptablesLog.re_iptablesTcp.match(result.get('proto_data'))
				result.update(self._match2dict(match))
				result = self._prepareSQL(result, ['ip_flag_df', 'tcp_flag_cwr', 'tcp_flag_ece', 'tcp_flag_urg', 'tcp_flag_ack', 'tcp_flag_psh', 'tcp_flag_rst', 'tcp_flag_syn', 'tcp_flag_fin'])
				result['date'] = "now()"
				sql = "INSERT INTO IptablesLog (date, hostname, comment, input_interface, output_interface, mac, ip_source, ip_destination, ip_lenght, ip_type_of_service, ip_precedence, ip_time_to_live, ip_id, ip_flag_df, ip_protocol, tcp_udp_sport, tcp_udp_dport, tcp_window, tcp_reserved, tcp_flag_cwr, tcp_flag_ece, tcp_flag_urg, tcp_flag_ack, tcp_flag_psh, tcp_flag_rst, tcp_flag_syn, tcp_flag_fin, tcp_urgent_pointer) VALUES (%(date)s, %(hostname)s, %(comment)s, %(input_interface)s, %(output_interface)s, %(mac)s, %(ip_source)s, %(ip_destination)s, %(ip_lenght)s, %(ip_type_of_service)s, %(ip_precedence)s, %(ip_time_to_live)s, %(ip_id)s, %(ip_flag_df)s, %(ip_protocol)s, %(tcp_udp_sport)s, %(tcp_udp_dport)s, %(tcp_window)s, %(tcp_reserved)s, %(tcp_flag_cwr)s, %(tcp_flag_ece)s, %(tcp_flag_urg)s, %(tcp_flag_ack)s, %(tcp_flag_psh)s, %(tcp_flag_rst)s, %(tcp_flag_syn)s, %(tcp_flag_fin)s, %(tcp_urgent_pointer)s)" % result
			elif result.get('ip_protocol') == 'UDP':
				match = IptablesLog.re_iptablesUdp.match(result.get('proto_data'))
				result.update(self._match2dict(match))
				result = self._prepareSQL(result, ['ip_flag_df'])
				result['date'] = "now()"
				sql = "INSERT INTO IptablesLog (date, hostname, comment, input_interface, output_interface, mac, ip_source, ip_destination, ip_lenght, ip_type_of_service, ip_precedence, ip_time_to_live, ip_id, ip_flag_df, ip_protocol, tcp_udp_sport, tcp_udp_dport, udp_lenght) VALUES (%(date)s, %(hostname)s, %(comment)s, %(input_interface)s, %(output_interface)s, %(mac)s, %(ip_source)s, %(ip_destination)s, %(ip_lenght)s, %(ip_type_of_service)s, %(ip_precedence)s, %(ip_time_to_live)s, %(ip_id)s, %(ip_flag_df)s, %(ip_protocol)s, %(tcp_udp_sport)s, %(tcp_udp_dport)s, %(udp_lenght)s)" % result
			elif result.get('ip_protocol') == 'ICMP':
				match = IptablesLog.re_iptablesIcmp.match(result.get('proto_data'))
				result.update(self._match2dict(match))
				result = self._prepareSQL(result, ['ip_flag_df'])
				result['date'] = "now()"
				sql = "INSERT INTO IptablesLog (date, hostname, comment, input_interface, output_interface, mac, ip_source, ip_destination, ip_lenght, ip_type_of_service, ip_precedence, ip_time_to_live, ip_id, ip_flag_df, ip_protocol, icmp_type, icmp_code, icmp_id, icmp_seq) VALUES (%(date)s, %(hostname)s, %(comment)s, %(input_interface)s, %(output_interface)s, %(mac)s, %(ip_source)s, %(ip_destination)s, %(ip_lenght)s, %(ip_type_of_service)s, %(ip_precedence)s, %(ip_time_to_live)s, %(ip_id)s, %(ip_flag_df)s, %(ip_protocol)s, %(icmp_type)s, %(icmp_code)s, %(icmp_id)s, %(icmp_seq)s)" % result
			else:
				result = self._prepareSQL(result, ['ip_flag_df'])
				result['date'] = "now()"
				sql = "INSERT INTO IptablesLog (date, hostname, comment, input_interface, output_interface, mac, ip_source, ip_destination, ip_lenght, ip_type_of_service, ip_precedence, ip_time_to_live, ip_id, ip_flag_df, ip_protocol) VALUES (%(date)s, %(hostname)s, %(comment)s, %(input_interface)s, %(output_interface)s, %(mac)s, %(ip_source)s, %(ip_destination)s, %(ip_lenght)s, %(ip_type_of_service)s, %(ip_precedence)s, %(ip_time_to_live)s, %(ip_id)s, %(ip_flag_df)s, %(ip_protocol)s)" % result
			if dbHandle.insert(sql):
				return True
			else:
				return False
		except:
			return False
