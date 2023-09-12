# LIFO means last in first out, we will use it in stacks

# in this scenario we are browsing websites and we are using the back button
# taking us back one website ago, from 3 - 2, and 2 - 1

browsing_session = []
browsing_session.append(1)  # 1 is the first website we are visiting
browsing_session.append(2)  # second website
browsing_session.append(3)  # third website
print(browsing_session)
browsing_session.pop()
print(browsing_session)
print("redirect", browsing_session[-1])

# we need to check if the stack is empty as well, so you can no longer use the back button

if not browsing_session:
    browsing_session[-1]  # item on the top of the stack
