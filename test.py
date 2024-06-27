import subprocess as sp
import numpy as np
import os

def check_num_range(big_num, samll_num, limit_cmd) :
	r = []
	num_list = np.array(range(big_num, samll_num - 1, -1))
	r.append(sp.run(args=["./push_swap", ' '.join(map(str, num_list))], capture_output=True, text=True).stdout.count('\n'))
	for i in range(9) :
		r.append(sp.run(args=["./push_swap", ' '.join(map(str, np.random.permutation(num_list)))], 
					capture_output=True, text=True).stdout.count('\n'))

	print("\t./push_swap <5 random values>")
	print('\t\t', end="")
	for i in range(len(r)) :
		if i % 5 == 0 and i != 0:
			print("\n\t\t", end="")
		if r[i] < limit_cmd :
			print(f"{i+1}." + "\033[32m" + "OK" + "\033[0m", end="  ")
		else :
			print(f"{i+1}." + "\033[31m" + f"KO: {r[i]}" + "\033[0m", end="  ")
		if (i + 1 == len(r)) :
			print(check_leck(' '.join(map(str, num_list))))
	print("\n")

def check_leck(num_list) :
	r = sp.run(args=["valgrind", "--leak-check=full", "./push_swap", num_list], capture_output=True, text=True)
	lines = r.stderr.split('\n')
	search_free = [line for line in lines if "total heap usage:" in line][0]
	search_error = [line for line in lines if "ERROR SUMMARY:" in line][0]
	if (search_free[search_free.find("allocs") - 2] == search_free[search_free.find("frees") - 2] and 
	 int(search_error[search_error.find("errors") - 2]) == 0):
		return ("\033[32m" + "\tleak_OK" + "\033[0m")
	else :
		return ("\033[31m" + "\tleak_KO" + "\033[0m")

os.system('clear')
print("/* ************************************************************************** */")
print("/*                                                                            */")
print("/*                                                        :::      ::::::::   */")
print("/*   push_swap_tester                                   :+:      :+:    :+:   */")
print("/*                                                    +:+ +:+         +:+     */")
print("/*   By: seongkim <seongkim@student.42gyeongsan.    +#+  +:+       +#+        */")
print("/*                                                +#+#+#+#+#+   +#+           */")
print("/*   Created: 2024/06/28 by seongkim                   #+#    #+#             */")
print("/*   Updated: 2024/06/28 by seongkim                  ###   ########.fr       */")
print("/*                                                                            */")
print("/* ************************************************************************** */")
print("\n")

sp.run(args=["make"], capture_output=True, text=True)
files = os.listdir("./")
if ("push_swap" not in files) :
	print("not found \"push_swap\"\n")
	exit()

print("\033[1m1.Error management\033[0m")
r = sp.run(args=["./push_swap", "a 1"], capture_output=True, text=True)
check_leck("a 1")
print("\t./push_swap <Non-numeric arguments>", end="")
if r.stderr == "Error\n" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	print("\033[31m" + "\tKO" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap", "0 0"], capture_output=True, text=True)
print("\t./push_swap <Duplicate numbers>", end="\t")
if r.stderr == "Error\n" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	print("\033[31m" + "\tKO" + "\033[0m", end="")
print(check_leck("a 1"))
	
r = sp.run(args=["./push_swap", "-2147483649 2147483648"], capture_output=True, text=True)
print("\t./push_swap <int range exceeded>", end="")
if r.stderr == "Error\n" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	print("\033[31m" + "\tKO" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap"], capture_output=True, text=True)
print("\t./push_swap <Empty arguments>", end="\t")
if r.stderr == "" and r.stdout == "" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	r.stderr = r.stderr.split('\n')[0] 
	print("\033[31m" + f"\tKO : {r.stderr}{r.stdout}" + "\033[0m", end="")
print(check_leck("a 1"))

print("\033[1m2.Identity test & Simple version\033[0m")
r = sp.run(args=["./push_swap", "42"], capture_output=True, text=True)
print("\t./push_swap 42", end="\t\t\t")
if r.stdout == "" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	put = r.stdout.count('\n')
	print("\033[31m" + f"\tKO : {put}" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap", "0 1 2 3"], capture_output=True, text=True)
print("\t./push_swap \"0 1 2 3\"", end="\t\t")
if r.stdout == "" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	put = r.stdout.count('\n')
	print("\033[31m" + f"\tKO : {put}" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap", "0 1 2 3 4 5 6 7 8 9"], capture_output=True, text=True)
print("\t./push_swap \"0 1 2 3 4 5 6 7 8 9\"", end="")
if r.stdout == "" :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	put = r.stdout.count('\n')
	print("\033[31m" + f"\tKO : {put}" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap", "2 1 0"], capture_output=True, text=True)
print("\t./push_swap \"2 1 0\"", end="\t\t")
if r.stdout.count('\n') == 2 or r.stdout.count('\n') == 3 :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	put = r.stdout.count('\n')
	print("\033[31m" + f"\tKO : {put}" + "\033[0m", end="")
print(check_leck("a 1"))

r = sp.run(args=["./push_swap", "1 5 2 4 3"], capture_output=True, text=True)
print("\t./push_swap \"1 5 2 4 3\"", end="\t\t")
if r.stdout.count('\n') < 12 :
	print("\033[32m" + "\tOK" + "\033[0m", end="")
else :
	put = r.stdout.count('\n')
	print("\033[31m" + f"\tKO : {put}" + "\033[0m", end="")
print(check_leck("a 1"))

check_num_range(5, 1, 12)

print("\033[1m3.Middle version\033[0m")
check_num_range(100, 1, 700)

print("\033[1m4.Advanced version\033[0m")
check_num_range(500, 1, 5500)