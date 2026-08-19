import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
blood_sugers = [57, 80, 98, 130, 35, 56, 87, 45, 231, 120, 79, 120]
Heartbeat = [230, 190, 240, 251, 231, 424, 123, 210, 220, 140, 130, 200]
Wrist_pulse =  [87, 120, 91, 60, 120 ,90, 98, 101, 70, 100, 151, 94]  

plt.plot([], [], color="pink", label="blood sugers", linewidth=5)

plt.plot([], [], color="red", label="haert beat", linewidth=5)

plt.plot([], [], color="aqua", label="wrist  pulse", linewidth=5)

# hospital information in plot:
plt.stackplot(month, 
    blood_sugers,
    Heartbeat,
    Wrist_pulse, 
    colors=["pink", "red", "aqua"])

plt.legend()
plt.title("hospital information")
plt.xlabel("month")
plt.ylabel("amount")

plt.show()

blood_sugers = list(filter(lambda x: x > 110, blood_sugers))
Heartbeat = list(filter(lambda x: x > 100, Heartbeat))
Wrist_pulse = list(filter(lambda x: x > 90, Wrist_pulse))
plt.plot(blood_sugers, color="pink", label="blood sugers")
plt.plot(Wrist_pulse, color ="red", label="wrist pulse")
plt.plot(Heartbeat, color="aqua", label="heart beat")

plt.legend()
plt.title("The patient's critical condition")

plt.show()




