import streamlit as st 


st.title("🔥 FLAMES Calculator")

a=list(st.text_input("Enter name").lower())
b=list(st.text_input("Enter second name").lower())

print(b)

for i in a.copy():
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a+b)

s="flames"
while(len(s)!=1):
    i=n%len(s)-1
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]

#d={'f':'Friends', 'l': 'Love', 'a': 'Affection', 'm': 'Marriage', 'e': 'Enemy', 's': 'Siblings'}
d = {
                'f': ('Friends', '🤝'), 'l': ('Love', '❤️'), 
                'a': ('Affection', '🥰'), 'm': ('Marriage', '💍'), 
                'e': ('Enemy', '💎'), 's': ('Siblings', '👫')
            }
if(st.button("get results")):
    st.success(d[s])
    result_text, emoji = d[s]
    st.markdown(f"""
        <div class="result-card">
            <h3 style='color: #ff4b4b;'>Result: {result_text} {emoji}</h3>
        </div>
        """, unsafe_allow_html=True)


