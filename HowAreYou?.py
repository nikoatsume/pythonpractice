print("Hello:)")
user_name = input("What is your name? ")

print(f"Welcome, {user_name}!")

user_mood = input("How are you feeling today? ")

happy = "happy"
sad = "sad"
tired = "tired"
anxious = "anxious"
frustrated = "frustrated"
homesick = "homesick"
depressed = "depressed"
insecure = "insecure"

if user_mood == happy:
	print("Good:) Enjoy it.")
if user_mood == sad:
	print("I'm sorry:( Take care of yourself today. Express your needs and boundaries clearly and firmly. Most importantly, do something that brings you joy:)")
	print("** I recommend knitting:)")
if user_mood == tired:
	print("Eat and rest as needed:) Nobody knows what your body needs more than you.")
if user_mood == anxious:
	print("First, meditate and reflect on the source of your anxiety. Let go of all that you can't control. Smoke a joint, if necessary:)")
if user_mood == frustrated:
	print("Take a moment. Breathe. Frustration is a valid emotion, but it is inherently unproductive. You are a solver. Is this something you can solve? If not, is it worth your energy?")
if user_mood == homesick:
	print("Call home:)")
if user_mood == depressed:
	print("Meditate. Prioritize rest and relaxation. Avoid junk. Exercise gives free endorphins! I know this sucks, but you've survived this storm before. What chance does depression have when matched against you?")
if user_mood == insecure:
	print("You define your value. No one else.")
user_extra = input(f"Are you having any other emotions, {user_name}? ")

end_program = "no"

if user_extra == end_program:
	print(f"Have a good day, {user_name}!")

while user_extra != end_program:
	print(f"Hm. Let's try again. How are you feeling today, {user_name}?")
	user_mood = input()
	
	




		
