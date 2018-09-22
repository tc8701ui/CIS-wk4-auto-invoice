services_list = {"services":{"names":["Oil change","Tire rotation","Car wash","Car wax"],"prices":[35,19,7,12]}}
service_table = {"Oil change,":35,"Tire rotation,":19,"Car wash,":7,"Car wax,":12,"No service":0}

print("Davy's auto shop services")
for index, item in enumerate(services_list["services"]["names"]):
    print("%s -- $%d" %(item,services_list["services"]["prices"][index]))
    
service1 = input("\nSelect first service:\n")
service2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")
if service1 in services_list["services"]["names"]:
    service1 += ','
    print("Service 1: %s $%d" % (service1,service_table[service1]))
elif service1 not in services_list["services"]["names"]:
    if service1 == "-":
        service1 = "No service"
        print("Service 1: %s" % service1)
    else:
        service1 = "Not recognized"
if service2 in services_list["services"]["names"]:
    service2 += ','
    print("Service 2: %s $%d" % (service2,service_table[service2]))
elif service2 not in services_list["services"]["names"]:
    if service2 == "-":
        service2 = "No service"
        print("Service 2: %s" % service2)
    else:
        service2 = "Not recognized"
        

print("\nTotal: $%d"% int(service_table[service1]+service_table[service2]))