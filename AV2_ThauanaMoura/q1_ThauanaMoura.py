var = 100

check_account = lambda state : "check_account" if state == "start" else "error"

withdrawl = lambda state, value : maybe_withdrawl(value) if state == "check_account" else "error"

maybe_withdrawl = lambda value : "withdrawl" if var - value >= 0 else "withdrawl not allowed"

deposit = lambda state : "deposit" if state == "check_account" else "error"

update_account_balance = lambda state, value : var - value if state == "withdrawl" else var + value if state == "deposit" else "error"

var = update_account_balance(deposit(check_account("start")), 200) 



print(var)