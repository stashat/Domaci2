while True:
    n = int(input('Unesite broj vrata i ucenika: '))
    if n >= 1 and n <= 1000000:
        sva_vrata = [False] * n
        for ucenik in range(1, n+1):
            sva_vrata[::ucenik] = map(lambda x: not x, sva_vrata[::ucenik])
        print("Otvorenih vrata od " + str(n) + " vrata i ucenika: " +
              str(sum(sva_vrata)))
        otvorena_vrata = []
        otvorena_vrata = [br_vrata+1 for br_vrata, status_vrata in
                          enumerate(sva_vrata) if status_vrata]
        print(otvorena_vrata)
        break
    else:
        print("unijeli ste broj koji nije izmedju 1 i 1,000,000")
