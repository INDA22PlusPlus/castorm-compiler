from emojis import *



INDENT = "    "
class Compiler:
    def __init__(self, data) -> None:
        self.original_data = data
        self.data = list(data)
        self.pointer = 0
        self.lines = 0
        self.count = len(self.data)
        self.result = ""
        self.indent_level = 0

    def throw(self, expected, found):
        raise SyntaxError(f"Expected Symbol: {expected}, Found: {found}. At line: {self.lines + 1}")

    def pad(self):
        for i in range(self.indent_level):
            self.result += INDENT
    def append(self, data):
        
        self.result += data

    def current_symbol(self) -> str:
        if self.EOF():
            return None
        curr = self.data[self.pointer]
        while curr not in DEFINITIONS:
            self.pointer += 1
            if self.EOF():
                return None
            curr = self.data[self.pointer]
            if curr == "\n":
                self.lines += 1
            
        return curr

    def EOF(self) -> bool:
        return self.pointer >= self.count

    def compile(self) -> str:
        while not self.EOF():
            self.expect_statement()
        return self.result

    def expect_symbol(self, symbol) -> None:
        curr = self.current_symbol()
        if curr != symbol:
            self.throw(symbol, curr)
        self.pointer += 1
    def expect_statement(self) -> None:
        self.pad()
        curr = self.current_symbol()
        if curr in ALPHABET:
            self.expect_assignment()
        elif curr in FLOW:
            self.expect_flow_control()
        elif curr == OUTPUT:
            self.expect_output()
        elif curr == None:
            return
        else:
            self.throw("statement", curr)
    def expect_assignment(self) -> None:
        self.expect_variable()
        curr = self.current_symbol()
        if curr == ASSIGNMENT:
            self.append("=")
            self.pointer += 1
            self.expect_expression()
            self.expect_terminator()
        else:
            self.throw(ASSIGNMENT, curr)
    def expect_variable(self) -> None:
        curr = self.current_symbol()
        while curr in ALPHABET:
            self.append(ALPHABET[curr])
            self.pointer += 1
            curr = self.current_symbol()
    def expect_expression(self) -> None:
        curr = self.current_symbol()
        if curr == INPUT:
            self.append("int(input())")
            self.pointer += 1
            return
        self.expect_term()
        curr = self.current_symbol()
        if curr == ADDITION:
            self.append("+")
            self.pointer += 1
            self.expect_expression()
        elif curr == SUBTRACTION:
            self.append("-")
            self.pointer += 1
            self.expect_expression()
    def expect_term(self) -> None:
        self.expect_factor()
        curr = self.current_symbol()
        if curr == MULTIPLICATION:
            self.append("*")
            self.pointer += 1
            self.expect_term()
        elif curr == DIVISION:
            self.append("//")
            self.pointer += 1
            self.expect_term()
    def expect_factor(self) -> None:
        curr = self.current_symbol()
        if curr in ALPHABET:
            self.expect_variable()
        elif curr in DIGITS:
            self.expect_integer()
        elif curr == LP:
            self.append("(")
            self.pointer += 1
            self.expect_expression()
            nxt = self.current_symbol()
            if nxt == RP:
                self.append(")")
                self.pointer += 1
            else:
                self.throw(RP, nxt)
        else:
            self.throw("*factor*", curr)
    def expect_integer(self) -> None:
        curr = self.current_symbol()
        i = ""
        while curr in DIGITS:
            i += curr
            self.pointer += 1
            curr = self.current_symbol()
        self.append(emoint_to_pyint(i))
    def expect_terminator(self) -> None:
        if self.EOF():
            return
        self.expect_symbol(NEWLINE)
        self.append("\n")
    def expect_output(self) -> None:
        self.expect_symbol(OUTPUT)
        self.append("print")
        self.expect_symbol(LP)
        self.append("(")
        self.expect_expression()
        self.expect_symbol(RP)
        self.append(")")
        self.expect_terminator()
    def expect_flow_control(self) -> None:
        curr = self.current_symbol()
        if curr == LOOP:
            self.expect_loop()
        elif curr == IF:
            self.expect_if()
        else:
            self.throw("if/while", curr)
    def expect_loop(self) -> None:
        self.expect_symbol(LOOP)
        self.append("while ")
        self.expect_symbol(LP)
        self.expect_condition()
        self.expect_symbol(RP)
        self.append(":\n")
        self.indent_level += 1
        self.expect_block()
        self.indent_level -= 1
    def expect_block(self) -> None:
        self.expect_symbol(LB)
        curr = self.current_symbol()
        while curr != RB:
            self.expect_statement()
            curr = self.current_symbol()
            if curr == None and self.EOF():
                raise EOFError()
        self.expect_symbol(RB)
    def expect_if(self) -> None:
        self.expect_symbol(IF)
        self.append("if ")
        self.expect_symbol(LP)
        self.expect_condition()
        self.expect_symbol(RP)
        self.append(":\n")
        self.indent_level += 1
        self.expect_block()
        self.indent_level -= 1
        curr = self.current_symbol()
        if curr == ELSE:
            self.expect_symbol(ELSE)
            self.append("else:")
            self.indent_level += 1
            self.expect_block()
            self.indent_level -= 1
    def expect_condition(self) -> None:
        self.expect_term_bool()
        curr = self.current_symbol()
        if curr == OR:
            self.append(" or ")
            self.pointer += 1
            self.expect_condition()
    def expect_term_bool(self) -> None:
        self.expect_factor_bool()
        curr = self.current_symbol()
        if curr == AND:
            self.append(" and ")
            self.pointer += 1
            self.expect_factor_bool()
    def expect_factor_bool(self) -> None:
        curr = self.current_symbol()
        if curr in BOOLS:
            self.append(BOOLS[curr])
            self.pointer += 1
        else:
            self.expect_comparison()
    def expect_comparison(self) -> None:
        self.expect_expression()
        curr = self.current_symbol()
        if curr in COMPARISONS:
            self.append(COMPARISONS[curr])
            self.pointer += 1
        else:
            self.throw("comparison", curr)
        self.expect_expression()

    def run(self) -> None:
        exec(self.compile())


import os
import sys
import codecs

with codecs.open(os.path.join(sys.path[0], sys.argv[1]), encoding="utf-8") as f:
    compiler = Compiler("".join(f.readlines()))
    try:
        compiler.compile()
        print(compiler.result)
    except SyntaxError as err:
        print("Compile Error: " + err.msg)
    except EOFError as err:
        print("Compile Error: Unexpected End Of File!")
    except Exception:
        print("Compile Error: Unknown Compile Error")
    else:
        try:
            exec(compiler.result)
        except Exception as ex:
            print("Runtime Error")