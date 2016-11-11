class client:
    def __init__(self, param):
        self.name = param
        self.send = []
        self.recieve = []


query = raw_input().split(" ")
query_client = []
clients = []
send_count = []
recieve_count = []
for i in query:
    query_client.append(i)
    clients.append(client(i))
    send_count.append(0)
    recieve_count.append(0)

s = raw_input()
while s:
    phone = s.split()
    if phone[0] in query_client:
        send_count[query_client.index(phone[0])]+=1
    if phone[1] in query_client:
        recieve_count[query_client.index(phone[1])]+=1

    s = raw_input()
result = []
for index in range(len(query_client)):
    if send_count[index] - recieve_count[index] > 1:
        result.append("1")
    else:
        result.append("0")
print " ".join(result)
