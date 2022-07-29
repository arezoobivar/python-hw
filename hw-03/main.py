#
# (C) ehsanha, 2022.
# Ehsan Haghpanah; haghpanah@scenus.com
#

#
# tries to parse provided string as an integer
#
# @param    text : a string representing an integer number
# @return   an integer if possible otherwise none
#
def try_parse_a(text: str) -> int:
    try:
        return int(text)
    except:
        return None

#
# tries to parse provided string as an integer
#
# @param    s : a string representing an integer number
# @return   an integer if possible otherwise none
#
try_parse_b = lambda s : int(s) if s.isdigit() else None

#
# returns a list of sub-folders in provided path
#
# @param    pa : a string representing the path
# @return   a list of sub-folders
#
def is_perfect_number(nm: int) -> bool:
	ls = [qo for qo in range(2, ((nm // 2) + 1)) if ((nm % qo) == 0)]
	return ((sum(ls) + 1) == nm)

#
# main routine
def main_run() -> None:
	nm = try_parse_b(input("please give me a number = "))
	if (nm == None):
		print("ERROR: not a valid integer number!")
		exit()

	if (is_perfect_number(nm)):
		print(f"number = {nm} is perfect")
	else:
		print(f"number = {nm} is not perfect")

main_run()