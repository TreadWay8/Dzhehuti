a = "18023812638912738012963812370891437328974678916239871263"
idx = 0
while a:
    if int(a[idx]) % 2 == 0:
        str(a[idx]).count(a[idx], "!")
        idx = idx + 1
    else:
        idx = idx + 1

