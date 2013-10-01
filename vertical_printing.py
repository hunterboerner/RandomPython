#filename:vertical_printing.py
#author:Theron Boerner

team_names = []
input_string = ""
while input_string != "END":
  input_string = raw_input("Gimme a name \n")
  if input_string != "END":
    team_names.append(input_string)
longest_length = 0
for x in xrange(len(team_names)):
  if len(team_names[x]) > longest_length:
    longest_length = len(team_names[x])

for y in xrange(longest_length):
  for x in xrange(len(team_names)):
    try:
      print team_names[x][y] + " ",
    except IndexError:
      print "  ",
  print
print team_names