symbols=["""
      |
    __|
   """,
   """
     .|
    __|
   """,
   """
    |  |
    |__|
   """,
   """
    | .|
    |__|
   """,
   """
    |
    |__
   """,
   """
    |.
    |__
   """,
   """
   ___
      |
   ___|
   """,
   """
   ___
    . |
   ___|
   """,
   """
    ___
   |   |
   |___|
   """,
      """
    ___
   | . |
   |___|
   """,
   """
    ___
   |
   |___
   """,
   """
    ___
   | .
   |___
   """,
   """
    ___
       |
       |
   """,
   """
    ___
     . |
       |
   """,
   """
    ___
   |   |
   |   |
   """,
   """
    ___
   | . |
   |   |
   """,
   """
    ___
   |
   |
   """,
   """
    ___
   | .
   |
   """,
   """
    \  /
     \/
   """,
   """
    \ ./
     \/
   """,
   """
    ^
   """,
   """
    ^
    .
   """,
   """
    >
   """,
   """
    .>
   """,
   """
    <
   """,
   """
    <.
   """,
   ]
message_e=[]
message_d=input("Enter your message to be encrypted: ")
alpha="abcdefghijklmnopqrstuvwxyz"
alpha=list(alpha)
for i in message_d.lower():
    if i.isalpha():
        x=alpha.index(i)
        message_e.append(symbols[x])
    else:
        message_e.append(i)
print("----()---()----")
print("".join(message_e))
print("----()---()----")
