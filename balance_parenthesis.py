#With stack
def balance(parenthesis_str):
  st=[]
  _listed = list(parenthesis_str)

  l=len(_listed)
  i=0

  while i<l:
    if _listed[i]=='(':
      st.append(i)
    elif _listed[i]==')':
      if st:
        st.pop()
      else:
        del _listed[i]
        i-=1
        l-=1

    i+=1

  while st:
    del _listed[st.pop()]

  return ''.join(_listed)

a = '(((((a(b)c)((()))))()(()())))()((())(('

print(balance((a)))