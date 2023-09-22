import sys

ts = 34

class UI:
	def dynamic_progress_bar(self, percentage, width=ts*2):
		spaces = ' ' * (width - len(self.trackLine['start']['staz']) - len(self.trackLine['end']['staz']) - 1)
		sys.stdout.write(f'{self.trackLine["start"]["staz"]} {spaces} {self.trackLine["end"]["staz"]}\n')

		progress = percentage / 100.0
		arrow = '=' * int(round(progress * width) - 1)
		spaces = ' ' * (width - len(arrow) -1)
		sys.stdout.write(f'\r[{arrow}{spaces}] {int(percentage)}%')
		sys.stdout.flush()

	def __init__(self):
		self.gps = {"isGpsValid":True,"ultimaStazione":"--","eta":"--", "speed":"--","delay":"--", "isOdoValid":False,"tracknum":"--", "isTrackOnGPS": True, "delay2": "--", "postreno": "--"}
		self.trackLine = {"start": {"staz": "--"}, "trainprogress": 0, "postreno": 0.0, "mid": {"staz": "--"}, "end": {"staz": "--"}}
		self.stops = []

	def _clear_terminal(self):
		print("\033[2J")
		print("\033[0;0f")

	def _print_train(self):
		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;252;65;3m")
		sys.stdout.write("                                	         __   __\n")
		sys.stdout.write("                                                 /'   `\\\n")
		sys.stdout.write("                                                Y.     .Y\n")
		sys.stdout.write("                                      _______    \\`. .'/\n")
		sys.stdout.write("                       ,-------------'=======\"--\"\"\"\"-\"\"\"\"---.\n")
		sys.stdout.write("                 __,=+'-------------------------------------|\n")
		sys.stdout.write("              .-/__|_]_]  :\"/:\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"|\n")
		sys.stdout.write("           ,-'__________[];/_;_____F R E C C I A R O S S A__|\n")
		sys.stdout.write("         ,\".../_|___________________________________________|\n")
		sys.stdout.write("        (_>        ,-------.                     ,-------.  |\n")
		sys.stdout.write("         `-._____.'(_)`='(_)\\_7___7___7___7__7_.'(_)`='(_)\\_/\n")
		sys.stdout.write("\033[000m")
		sys.stdout.flush()
	
	def printError(self):
		self._clear_terminal()
		# self._print_train()

		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;252;65;3m")
		sys.stdout.write('='*ts +" Error " + '='*(ts-1)+"\n")
		sys.stdout.write("\033[000m")
		print("The train is not providing valid data :(\n")

	def print(self):
		self._clear_terminal()
		self._print_train()

		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;194;245;66m")
		sys.stdout.write("\n" + '='*ts +" Data " + '='*ts+"\n")
		sys.stdout.write("\033[000m")
		print(f"Speed:     {self.gps['speed']} km/h")
		print(f"Delay:     {self.gps['delay']}")

		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;66;245;99m")
		sys.stdout.write("\n" + '='*(ts-2) +" Progress " + '='*(ts-2)+"\n")
		sys.stdout.write("\033[000m")
		self.dynamic_progress_bar(self.trackLine['postreno'])
		print("\n")

		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;245;179;66m")
		sys.stdout.write("\n" + '='*ts +" Stops " + '='*(ts-1)+"\n")
		sys.stdout.write("\033[000m")

		if len(self.stops) == 0:
			print("   No stops information....")
		for stop in self.stops:
			print(f" - {stop['description'].title():40s} Arrival time: {stop['orario']}")
