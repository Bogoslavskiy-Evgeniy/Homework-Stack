from main import Stack

def check(text):
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    st = Stack()
    for i in text:
        if i in open_bracket:
            st.push(i)
        elif i in close_bracket:
            ind = close_bracket.index(i)
            if len(st.stack) > 0 and open_bracket[ind] == st.peek():
                st.pop()
            else:
                return 'Несбалансированно'
    if len(st.stack) == 0:
        return 'Сбалансированно'

print(check('(((([{}]))))'))
print(check('[([])((([[[]]])))]{()}'))
print(check('{{[()]}}'))

print(check('}{}'))
print(check('{{[(])]}}'))
print(check('[[{())}]'))

