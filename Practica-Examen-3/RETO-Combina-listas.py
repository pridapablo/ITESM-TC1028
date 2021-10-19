def main():
  n_L1 = int(input())
  n_L2 = int(input())

  if (n_L1 <= 0) or (n_L2 <= 0):
    print("Error")
    exit()
  else:
    print("-----")
    L1 = []
    for i in range(n_L1):
      L1.append(input())

    print("-----")
    L2 = []
    for i in range(n_L2):
      L2.append(input())      

  print("-----")

  print(L1)
  print(L2)

  combo = []

  for i in range(len(L1)):
    if (i % 2) == 0:
      combo.append(L1[i])
    else: combo[i] = None

  for i in range(len(L2)):
    if (i % 2) != 0:
      combo.append(L2[i])

  print(combo)

if __name__ == "__main__":
  main()