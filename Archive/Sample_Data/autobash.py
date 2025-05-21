import subprocess
#script_path = "test.sh"
# you know that you have more than one bash script put their paths in a list
scripts = ["test0.sh", "test1.sh", "test2.sh"]
# x = 5
# # single script
# result = subprocess.run(["bash", script_path], capture_output=True, text=True)
# for script in range(x):
#  if result.returncode == 0:
#    print("Running Process ", script)
#  else:
#   # halt the program and exit because something went wrong
#   print("uh-oh something went wrong! ")
#   exit(1)


for script in range(len(scripts)):
  results = subprocess.run(["bash", scripts[script]], capture_output=True, text=True)
  if results.returncode == 0:
    print("Running Process ", script)
    print(results)
  else:
  # halt the program and exit because something went wrong
    print("uh-oh something went wrong! ")
    exit(1)