# 5-8. Hello Admin: Make a list of five or more usernames, 
# including the name 'admin' . 
# Imagine you are writing code 
# that will print a greeting to each user after they log in 
# to a website . 
# 
# Loop through the list, and print a greeting to each user:

# for each item execute the following code block

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list 
# of users is not empty .
# • If the list is empty, print the message We need to find some users!
# len(usernames) return interger 0 - infinty depeding on how many items in given list
usernames = ['user1', 'user2', 'user3', 'admin', 'user4', 'user5']

if len(usernames) > 0:
  # for each item
  for current_item in usernames:
    # ask questions
    if current_item == 'admin':
      print(f"Hello {current_item}, would you like to see a status report?")
    elif current_item != 'admin':
      print(f"Hello {current_item}, thank you for log- ging in again.")
# We need to find some users!   
# otherwise
else:
  print("We need to find some users!")

  # • Remove all of the usernames from your list, and make sure the correct!
  # message is printed .



# SONIA
# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username .
# • Make a list of five or more usernames called current_users .
# • Make another list of five usernames called new_users . 
# Make sure one or two of the new usernames are also in the current_users list .
current_users = ['user1', 'nuser2', 'nuser1', 'user2', 'user3', 'user4', 'user5']
new_users = ['Nuser1', 'Nuser2', 'nuser3', 'nuser4', 'nuser5']
# DIANA
# • Loop through the new_users list to see if each new username has already been used .
# If it has, print a message that the person will need to enter a new username . 
# If a username has not been used, print a message saying that the username is available .
# SONIA
# • Make sure your comparison is case insensitive . 
# If 'John' has been used, 'JOHN' should not be accepted .
current_users = [item.lower() for item in current_users]
new_users = [item.lower() for item in new_users]

for current_item in new_users:
  if current_item in current_users:
    print(f"The username : {current_item} is already taken!")
  elif current_item not in current_users:
    print(f"The username : {current_item} is available")



# 5-11. Ordinal Numbers: Ordinal numbers indicate their position 
# in a list, such as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .
# • Store the numbers 1 through 9 in a list .
# • Loop through the list .
# • Use an if-elif-else chain inside the loop to print the proper ordinal end- ing for each number . Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line