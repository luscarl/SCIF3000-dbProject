qry = """SELECT SUM ("Total Pax")FROM cirium_traffic_northamerica
WHERE "Orig" in ('ABE', 'ABI', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AGS', 'AKC', 'ALB', 'ALW', 'AMA', 'ANC', 'APN', 'ASE', 'ATL', 'ATW', 'AUG', 'AUS', 'AVL', 'AVP', 'AZO', 'BDL', 'BET', 'BFF', 'BFL', 'BGM', 'BGR', 'BHM', 'BIL', 'BIS', 'BLI', 'BMI', 'BNA', 'BOI', 'BOS', 'BPT', 'BQK', 'BQN', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 'BUF', 'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 'CIC', 'CID', 'CKB', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'COD', 'COS', 'CPR', 'CRP', 'CRW', 'CSG', 'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DIK', 'DLG', 'DLH', 'DRO', 'DSM', 'DTW', 'DVL', 'EAR', 'EAT', 'EAU', 'ECP', 'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 'FAR', 'FAT', 'FAY', 'FCA', 'FCM', 'FLL', 'FLO', 'FNT', 'FSD', 'FSM', 'FWA', 'FYV', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT', 'GRB', 'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'HNL', 'HOB', 'HOU', 'HPN', 'HRL', 'HSV', 'HTS', 'IAD', 'IAH', 'ICT', 'IDA', 'ILG', 'IND', 'INL', 'ISN', 'ISP', 'ITH', 'ITO', 'IYK', 'JAC', 'JAN', 'JAX', 'JFK', 'JNU', 'KTN', 'LAN', 'LAS', 'LBB', 'LBE', 'LBF', 'LCH', 'LCK', 'LEW', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LMT', 'LNK', 'LRD', 'LSE', 'LWB', 'LYH', 'MBS', 'MCI', 'MCN', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM', 'MFE', 'MFR', 'MHT', 'MIA', 'MKE', 'MKG', 'MLB', 'MLU', 'MOB', 'MOD', 'MOT', 'MQT', 'MVY', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'ONT', 'ORD', 'ORF', 'OTZ', 'OXR', 'PBI', 'PDX', 'PGD', 'PHL', 'PHX', 'PIE', 'PIR', 'PIT', 'PSC', 'PSG', 'PSP', 'PVD', 'PWM', 'RAP', 'RDD', 'RDM', 'RDU', 'RFD', 'RHI', 'RIC', 'RNO', 'ROC', 'ROW', 'RST', 'RSW', 'SAF', 'SAN', 'SAT', 'SAV', 'SBA', 'SCE', 'SDF', 'SEA', 'SFB', 'SFO', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF', 'SNA', 'SPI', 'SPN', 'SRQ', 'STC', 'STL', 'STT', 'STX', 'SUN', 'SWF', 'SYR', 'TLH', 'TOL', 'TPA', 'TRI', 'TTN', 'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 'UIN', 'USA', 'VLD', 'VPS', 'WRG', 'WYS', 'XNA', 'YAK', 'YUM')
AND "Dest" in ('SYD')
AND "Stop-2 Airport" in ('LAX')
AND "Stop-2 Al" in ('AA','DL','UA','QF')
AND "Year-Month-Day" BETWEEN '2022-01-01 00:00:00' AND '2023-06-01 00:00:00'
GROUP BY TO_CHAR("Year-Month-Day", 'YYYY-MM')
ORDER BY TO_CHAR("Year-Month-Day", 'YYYY-MM');"""

