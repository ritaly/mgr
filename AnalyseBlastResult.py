import time

start_time = time.time()
print(time.strftime("%d-%b-%Y-%H:%M:%S", time.localtime()))

def convert(value):
	if value == '':
		return ''
	if '.' in value:
		 return float(value)
	else:
		return int(value)

def check_start(current, last):
	query_cond = current[4] >= last[0] and current[4] < last[1]
	subject_cond = current[6] >= last[2] and current[6] < last[3]
	return (query_cond and subject_cond)

def check_qend(current, last):
	return current[5] >= last[1]

def check_send(current, last):
	return current[7] >= last[3]

# def add_LCR(curr):
# 	array_with_LCR.append([curr[4], curr[5], curr[6], curr[7]])

array_with_LCR = [] #ad 1 [qstar, qend,sstart,send]

with open('chr_test_2019_15-Apr-2019-200538.txt', 'r') as file:

	data = file.readlines()
	#import code; code.interact(local=dict(globals(), **locals()))

	prev_line = ''
	for curr_line in data:
		curr = [convert(i) for i in curr_line.split()] 
		prev = [convert(i) for i in prev_line.split()] 
		if prev_line == '':
			prev_line = curr_line
			array_with_LCR.append([curr[4], curr[5], curr[6], curr[7], curr[2]])
			continue

		dist = curr[0] - prev[0]
		dist2 = curr[1] - prev[1]
		if dist > 500 or dist2 > 500:
			#print(int(prev[0]), int(curr[0]))
			array_with_LCR.append([curr[4], curr[5], curr[6], curr[7], curr[2]])
			prev_line = curr_line

		if (dist == 0 or dist == 500) and (dist2 == 0 or dist2 == 500):
			last_align = array_with_LCR[-1]
			if check_start(curr, last_align):
				if curr[2] > last_align[4]:
					last_align[4] = curr[2]
				#to jest jaknajbardziej ok
				if check_qend(curr, last_align):
					last_align[1] = curr[5]
				if check_send(curr, last_align):
					last_align[3] = curr[7]
			array_with_LCR[-1] = last_align
			prev_line = curr_line

		#poprzednia linia odległa od 0 lub o 500
			#czy nowe qstart >= prev_qstart ale =< prev_end

timestamp = time.strftime("%d-%b-%Y-%H%M%S", time.localtime())
save_file = open("chr3_result_2019_" + timestamp + "NOC.txt", "w")

for i in array_with_LCR:
	align_len = i[1] - i[0]
	row = ", ".join(map(str, i))
	row = row + ", " + str(align_len) + "\n"
	save_file.write(row)

end_time = time.time()
execution_time = end_time - start_time
print("Zapisano!")
print("Czas wykonywania: ", execution_time)


"""
ad 1 
LCR inaczej segmentalne duplikacje (SD) [Bailey et al., 2002], 
	są zdefiniowane jako pary sekwencji DNA dłuższe niż 1 kb, 
	o współczynniku podobieństwa sekwencyjnego powyżej 90%.
	W pracy [Stankiewicz and Lupski,2002] zostało pokazane,
	że długie (10 − 400 kb) fragmenty LCRs o wysokim
(powyżej 97%) współczynniku podobieństwa sekwencyjnego mogą sprzyjać
zachodzeniu m.in. inwersji (w przypadku par sekwencji LCRs o orientacji
odwrotnej), oraz delecji i duplikacji (sekwencje LCRs o orientacji zgodnej).
"""