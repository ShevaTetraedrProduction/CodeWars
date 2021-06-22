def expanded_form(num):
    num = str(num)
    return ' + '.join(j + '0' * ((len(num) - 1 - i)) for i, j in enumerate(num) if int(j))

test.assert_equals(expanded_form(12), '10 + 2');
test.assert_equals(expanded_form(42), '40 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');