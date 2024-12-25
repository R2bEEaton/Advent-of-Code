from helpers.datagetter import aocd_data_in
from llist import sllist

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din = int(din)

spinlock = sllist()
spinlock.append(0)

curr = spinlock.first
for i in range(1, 50000000+1):
    for _ in range(din+1):
        if curr.next is None:
            curr = spinlock.first
        else:
            curr = curr.next
    spinlock.insertafter(i, curr)
    if i % 10000 == 0:
        print(i)

aocd_submit(spinlock[1])