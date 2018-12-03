from django.shortcuts import render

# Lightning Network
from lightning import LightningRpc

# Bitcoin
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def index(request):
    # Bitcoin RPC Credentials (you need to change these)
    rpc_port="8332"
    rpc_user="user82ue99fwo3049f7c8a8d93dkall2l1l11"
    rpc_password="passwordb084b7v85f7hd06s06d06fgd01shaj"

# LIGHTNING NETWORK

    # Lightning Network Socket file (you might need to change this)
    ln = LightningRpc("/home/pi/.lightning/lightning-rpc")

    try:
        l_info = ln.getinfo()
        l = LightningViewData(True)
        l.block_height = l_info["blockheight"]
        l.version = l_info["version"]
        l.version = l.version.replace("v", "")

        l_peers = ln.listpeers()
        l.peer_count = len(l_peers["peers"])

        l_funds = ln.listfunds()
        l.channel_count = len(l_funds["channels"])
    except:
        l = LightningViewData(False)


# BITCOIN

    b = BitcoinViewData(True)

    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
        b_conn_count = rpc_connection.getconnectioncount()
        if b_conn_count > 0:
            b.online = True
    except Exception as e:
        b.running = False

    if b.running == True:
        try:
            b.block_height = rpc_connection.getblockcount()
            b_network_info = rpc_connection.getnetworkinfo()
            b.peer_count = b_network_info["connections"]
            b.version = b_network_info["subversion"]
            b.version = b.version.replace("/", "")
            b.version = b.version.replace("Satoshi:", "")
        except Exception as e:
            b.message = str(e)


# RETURN VIEW DATA

    return render(request, 'dashboard/index.html', {'lightning': l, 'bitcoin': b})


class BitcoinViewData:
    def __init__(self, running):
        self.running = running
        self.online = False
        self.peer_count = 0
        self.block_height = 0
        self.version = ""
        self.message = ""

class LightningViewData:
    def __init__(self, running):
        self.running = running
        self.peer_count = 0
        self.channel_count = 0
        self.block_height = 0
        self.version = ""
        self.message = ""
