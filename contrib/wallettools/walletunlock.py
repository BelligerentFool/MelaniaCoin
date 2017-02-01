from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:26197")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
